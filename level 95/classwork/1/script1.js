const form = document.getElementById("form");

form.addEventListener("submit", (e) => {
  e.preventDefault();

  const name = form.elements.name.value;
  const email = form.elements.email.value;
  const pass = form.elements.pass.value;
  const person = {
    name: name,
    email: email,
    password: pass
  };
  let count = localStorage.length + 1;

  while (localStorage.getItem(`person${count}`)) {
    count++;
  }

  localStorage.setItem(`person${count}`, JSON.stringify(person));
  alert(`Saved as person${count}!`);

  form.reset();
});