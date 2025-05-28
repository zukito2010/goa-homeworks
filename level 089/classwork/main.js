fetch('https://fakestoreapi.com/products/1') // Product with ID 1
    .then(response => response.json())
    .then(data=>{
        const productDiv = document.getElementById('product');
      productDiv.innerHTML =`
        <h2>${data.title}</h2>
        <p>${data.description}</p>
        <p class='price'>$${data.price}</p>
        <img src='${data.image}'>
       `;
    })
    .catch(error => {
        document.getElementById('product').innerHTML = 'Failed to load';
        console.log(error);
    });
