const form = document.getElementById('myform');

function formSubmit() {
    const name = form.elements.name;
    const email = form.elements.email;
    const password = form.elements.password;
    const gender = form.elements.gender;
    const country = form.elements.country;
    const terms = form.elements.checkbox;

    let isValid = true;

    if (name.value.trim() =='') {
        name.style.borderColor = 'red';
        isValid = false;
    } else {
        name.style.borderColor = '';
    }

    if (email.value.trim() == '') {
        email.style.borderColor = 'red';
        isValid = false;
    } else {
        email.style.borderColor = '';
    }

    if (password.value.trim() == '') {
        password.style.borderColor = 'red';
        isValid = false;
    } else {
        password.style.borderColor = '';
    }

    if (gender.value == '') {
        gender.style.borderColor = 'red';
        isValid = false;
    } else {
        gender.style.borderColor = '';
    }

    if (country.value == '') {
        country.style.borderColor = 'red';
        isValid = false;
    } else {
        country.style.borderColor = '';
    }

    console.log('Name: ' + name.value);
    console.log('Email: ' + email.value);
    console.log('Password: ' + password.value);
    console.log('Gender: ' + gender.value);
    console.log('Country: ' + country.value);
    console.log('Terms accepted: ' + terms.checked);

    form.reset();
}

form.addEventListener('submit', function (e) {
    e.preventDefault();
    formSubmit();
});