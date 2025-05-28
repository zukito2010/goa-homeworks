document.getElementById('book-form').addEventListener('submit', async function(e){
    e.preventDefault();

    const bookInfo = document.getElementById('book-input').value.trim();
    const api = `https://www.googleapis.com/books/v1/volumes?q=${bookInfo}`;
    const booksGrid = document.getElementById('book-grid');
    const noResult = document.getElementById('no-result');

    booksGrid.innerHTML = '';
    noResult.style.display = 'none';

    try {
        const res = await fetch(api);
        const data = await res.json();



        if (!data.items){
            noResult.style.display = 'block';
            return;
        }

        data.items.forEach((item) => {
            const info = item.volumeInfo;

            const book = {
                title: info.title || 'no title available',
                authors: info.authors || 'no authors available',
                thumbnail: info.imageLinks?.thumbnail || null 
            }
            
            const card = document.createElement('div');
            
            card.innerHTML = `
            ${book.thumbnail ? "<img src='${book.thumbnail}'/>" : '<p>No image available</p>'}
            <strong>Title: </strong> ${book.title}
            <strong>Authors: </strong>${book.authors}
            `;
            const button = document.createElement('button');
            button.textContent = LocalStorage.getItem(book.title) ? 'Already added' : 'Add';

            button.addEventListener('click', () => {
                const existing = LocalStorage.getItem(book.title);

                if (existing){
                    alert('this book is already in your library');
                }else{
                    LocalStorage.setItem(book.title, JSON.stringify(book))
                    button.textContent = 'Already Added';
                }
            })



        });

    }catch (error){
        console.log(error);
    }


})