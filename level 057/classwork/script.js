const form = document.getElementById('myform');

function formSubmit() {
    const name = form.elements.name.value;
    const email = form.elements.email.value;
    const password = form.elements.password.value;
    const gender = form.elements.gender.value;
    const terms = form.elements.gender.value;

    console.log('Name: ' + name);
    console.log('email: ' + email);
    console.log('password: ' + password);
    console.log('gender: ' + gender);
    console.log('terms: ' + terms);
    

    form.reset();
}

form.addEventListener('submit', function(e){
    e.preventDefault();
    formSubmit();
})