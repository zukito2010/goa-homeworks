const inp = document.getElementById('inp');
const myForm = document.getElementById('myForm');
const mainDiv = document.getElementById('main');
let i = 0;

for (let x = 0; x < localStorage.length; x++) {
  const key = localStorage.key(x);
  const value = localStorage.getItem(key);

  if (!isNaN(key)) {
    addTaskToPage(key, value);
    if (+key >= i) i = +key + 1;
  }
}

myForm.addEventListener('submit', (e) => {
  e.preventDefault();

  const task = inp.value.trim();
  if (task === '') return;

  localStorage.setItem(i, task);
  addTaskToPage(i, task);

  inp.value = '';
  i++;
});


function addTaskToPage(key, value) {
  const taskDiv = document.createElement('div');
  taskDiv.innerHTML = `
    <h4>Task: ${value} <button data-key="${key}">Delete</button></h4>
  `;

  const deleteBtn = taskDiv.querySelector('button');
  deleteBtn.addEventListener('click', () => {
    localStorage.removeItem(key);
    taskDiv.remove();
  });

  mainDiv.appendChild(taskDiv);
}