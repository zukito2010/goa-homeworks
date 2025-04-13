const form = document.getElementById("form");
const arr = [];
let bool = true;

form.addEventListener("submit", (e) => {
    e.preventDefault();

    const name = form.elements.name.value;
    const email = form.elements.email.value;
    const pass = form.elements.pass.value;

    if (arr.length === 0) {
        localStorage.setItem("users", JSON.stringify([]));
    }

    const arr2 = JSON.parse(localStorage.getItem("users"));
    console.log(arr2);

    for (let i of arr2) {
        if (email === i[1]) {
        bool = false;
        }
    }

    if (bool) {
        arr2.push([name, email, pass]);
        localStorage.setItem("users", JSON.stringify(arr2));
    } else {
        console.log("Account with this email already exists.");
    }
});