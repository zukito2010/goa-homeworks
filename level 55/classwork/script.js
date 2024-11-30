const form = document.getElementsById('form');
form.addEventListener('submit', function(e) {
    e.preventDefault();
})
console.log(form.elements.input.value)