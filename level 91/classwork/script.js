const searchInput = document.getElementById('search');
const userCardTemplate = document.querySelector('[data-user-template]');
const main = document.getElementById('main');
const myForm = document.getElementById('myForm')

myForm.addEventListener('submit', e => {

    e.preventDefault(); // prevent page reload

    const query = searchInput.value.trim();
    if (!query) return;

    // Clear old results
    main.innerHTML = '';

    fetch(`https://www.googleapis.com/books/v1/volumes?q=${query}`)
        .then(res => res.json())
        .then(data => {
            if (!data.items) {
                main.textContent = 'No books found!';
                return;
            }

            data.items.forEach(book => {
                const card = userCardTemplate.content.cloneNode(true).children[0];
                const info = book.volumeInfo;

                const title = card.querySelector('.book-title');
                const authors = card.querySelector('.book-author');
                const description = card.querySelector('.book-description');
                const pages = card.querySelector('.book-pages');
                const img = card.querySelector('.book-img');

                title.textContent = `Title: ${info.title || 'N/A'}`;
                authors.textContent = `Authors: ${info.authors?.join(', ') || 'N/A'}`;
                description.textContent = `Description: ${info.description || 'N/A'}`;
                pages.textContent = `Pages: ${info.pageCount || 'N/A'}`;
                img.src = info.imageLinks.thumbnail;

                card.classList.add('cards');
                main.appendChild(card);
            });
        })
        .catch(error => {
            console.error('Fetch error:', error);
            main.textContent = 'Something went wrong.';
        });
});