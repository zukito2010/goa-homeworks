const products = document.getElementById('products');


const fetchData = async () => {
    try{
        const storeItems = await fetch('https://fakestoreapi.com/products');
        const jason = await storeItems.json();
        jason.forEach(e => {
            products.innerHTML += `
            <div>
                <img src="${e.image}" alt="${e.title}">
                <h2>${e.title}</h2>
                <p>${e.description.substring(0, 100)}...</p>
                <p class="price">$${e.price}</p>
            </div>`
                
        });
    }catch (err){
        console.error(err);
    }
}


fetchData();







// fetch('https://fakestoreapi.com/products')
//     .then(res => res.json())
//     .then(products => {
//         const container = document.getElementById('products');
//         container.innerHTML = '';

//         products.forEach(product => {
//         const item = document.createElement('div');
//         item.className = 'product';
//         item.innerHTML = `
//             <img src="${product.image}" alt="${product.title}">
//             <h2>${product.title}</h2>
//             <p>${product.description.substring(0, 100)}...</p>
//             <p class="price">$${product.price}</p>
//         `;
//         container.appendChild(item);
//         });
//     })
//     .catch(err => {
//         document.getElementById('products').innerHTML = 'Failed to load products.';
//         console.error(err);
// });

