const form = document.getElementById('myform');

function formSubmit() {
    const name = form.elements.name.value;
    const email = form.elements.email.value;
    const password = form.elements.password.value;

    console.log('Name: ' + name);
    console.log('email: ' + email);
    console.log('password: ' + password);

    form.reset();
}

form.addEventListener('submit', function(e){
    e.preventDefault();
    formSubmit();
})