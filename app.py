from flask import Flask, render_template, request, jsonify
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
import pandas as pd

app = Flask(__name__)

# Contoh data tanaman
plants = {
    'tanamanA': {'price': 10000, 'stock': 15, 'sales': 6},
    'tanamanB': {'price': 20000, 'stock': 8, 'sales': 4},
    'tanamanC': {'price': 15000, 'stock': 20, 'sales': 10}
}

# Data transaksi tiruan
transactions = [
    ['tanamanA', 'tanamanB', 'tanamanD'],
    ['tanamanB', 'tanamanC', 'tanamanE'],
    ['tanamanA', 'tanamanB', 'tanamanC', 'tanamanE'],
    ['tanamanA', 'tanamanC', 'tanamanE'],
    ['tanamanA', 'tanamanB', 'tanamanD', 'tanamanE']
]

# Preprocessing data transaksi
df = pd.DataFrame(transactions)
df_encoded = pd.get_dummies(df, prefix='', prefix_sep='')

# Terapkan algoritma Apriori
frequent_itemsets = apriori(df_encoded, min_support=0.2, use_colnames=True)

# Buat aturan asosiasi
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.7)

# Inisialisasi keranjang belanja
cart_items = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search_plant', methods=['POST'])
def search_plant():
    plant_type = request.form['plantType']
    plant = plants.get(plant_type)

    if plant:
        return jsonify({
            'price': plant['price'],
            'stock': plant['stock'],
            'best_seller': 'Ya' if plant['sales'] > 5 else 'Tidak'
        })
    else:
        return jsonify({'error': 'Tanaman tidak ditemukan'})

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    plant_type = request.form['plantType']
    plant_name = request.form['plantName']
    cart_items.append(plant_name)
    return jsonify({'message': 'Item telah ditambahkan ke keranjang'})

@app.route('/checkout', methods=['POST'])
def checkout():
    if cart_items:
        cart_items.clear()  # Bersihkan keranjang setelah checkout
        return jsonify({'message': 'Proses checkout berhasil'})
    else:
        return jsonify({'error': 'Keranjang belanja kosong'})

if __name__ == '__main__':
    app.run(debug=True)
from flask import redirect, url_for

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    plant_type = request.form['plantType']
    plant_name = request.form['plantName']
    cart_items.append(plant_name)
    return redirect(url_for('show_cart'))

@app.route('/cart')
def show_cart():
    return render_template('cart.html', cart_items=cart_items)


