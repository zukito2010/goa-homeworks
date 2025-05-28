const form = document.getElementById('myform');

function formSubmit() {
    const name = form.elements.name.value;
    const email = form.elements.email.value;
    const password = form.elements.password.value;
    const gender = form.elements.gender.value;
    const terms = form.elements.gender.checked;

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


let text = 'are you an adult?';

if (confirm(text)== true){
    text = "You are an adult";
} else {
    text = "You are not an adult";
}

console.log(text)

// confirm is like an alert function but you have to choose one of the two buttons ('ok','cancel') that returns true and false 