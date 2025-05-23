// function hoisting allows users to access functions before and after it is declared.
// let/const hoisting only allows users to access items after declaration just like in python.

// while using bubbling order goes from child to parents and with capturing parent is first and than comes children

let next = document.getElementById('next');
let prev = document.getElementById('prev');
let img = document.getElementsByTagName('img')[0]; // Access the first <img> element
let i = 0;

const shreks = [
    './shrek1.jpg',
    './shrek2.jpg',
    './shrek3.jpg',
    './shrek4.jpg',
    './shrek5.jpg',
];

next.addEventListener('click', () => {
    i++;
    if (i == shreks.length) { 
        i = 0;
    }
    img.src = shreks[i]; 
});

prev.addEventListener('click', () => {
    i--;
    if (i == -1) {
        i = shreks.length - 1; 
    }
    img.src = shreks[i]; 
});