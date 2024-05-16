document.addEventListener('DOMContentLoaded', function() {
    const searchButton = document.getElementById('searchButton');
    searchButton.addEventListener('click', searchPlant);

    const addToCartButton = document.getElementById('addToCartButton');
    addToCartButton.addEventListener('click', addToCart);

    const checkoutButton = document.getElementById('checkoutButton');
    checkoutButton.addEventListener('click', checkout);
});

function searchPlant() {
    const plantType = document.getElementById('plantType').value;

    fetch('/search_plant', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: new URLSearchParams({
            'plantType': plantType
        })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('price').innerText = `Harga: ${data.price}`;
        document.getElementById('stock').innerText = `Stok: ${data.stock}`;
        document.getElementById('bestSeller').innerText = data.best_seller;
        document.getElementById('plantInfo').style.display = 'block';

        // Tambahkan rekomendasi tanaman
        const recommendations = data.recommendations;
        const recommendationsList = document.getElementById('recommendations');
        recommendationsList.innerHTML = '';
        recommendations.forEach(recommendation => {
            const listItem = document.createElement('li');
            listItem.textContent = recommendation;
            recommendationsList.appendChild(listItem);
        });
    })
    .catch(error => console.error('Error:', error));
}

function addToCart() {
    const plantType = document.getElementById('plantType').value;
    const plantName = document.getElementById('plantType').options[document.getElementById('plantType').selectedIndex].text;

    fetch('/add_to_cart', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: new URLSearchParams({
            'plantType': plantType,
            'plantName': plantName
        })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        window.location.href = "/cart"; // Mengarahkan ke halaman keranjang belanja
    })
    .catch(error => console.error('Error:', error));
}




function checkout() {
    fetch('/checkout', {
        method: 'POST'
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
    })
    .catch(error => console.error('Error:', error));
}
