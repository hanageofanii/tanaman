from flask import Flask, render_template, request

app = Flask(__name__)

# Data stok dan penjualan tanaman hias
tanaman_hias = {
    'bunga_mawar': {'stok': 10, 'terjual': 5},
    'tanaman_anggrek': {'stok': 15, 'terjual': 8},
    'tanaman_monstera': {'stok': 20, 'terjual': 10},
    'tanaman_kaktus': {'stok': 12, 'terjual': 6}
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    nama_tanaman = request.form['nama_tanaman']
    print("Nama tanaman:", nama_tanaman)  # Tambahkan ini untuk debug
    if nama_tanaman in tanaman_hias:
        stok = tanaman_hias[nama_tanaman]['stok']
        terjual = tanaman_hias[nama_tanaman]['terjual']
        return render_template('result.html', nama_tanaman=nama_tanaman, stok=stok, terjual=terjual)
    else:
        return render_template('result.html', nama_tanaman=nama_tanaman, not_found=True)

if __name__ == '__main__':
    app.run(debug=True)
