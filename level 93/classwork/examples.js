// arrow functions:

const add = (a,b) =>{
    return a+b;
};

const subt = (a,b) =>{
    return a-b;
};

const mult = (a,b) =>{
    return a*b;
};
// shorthand property names:
const title = "Atomic Habits";
const author = "James Clear";
const pages = 320;

const book = { title, author, pages };
console.log(book);

const namee = "Luna";
const level = 42;
const isOnline = true;

const player = { namee, level, isOnline };
console.log(player);

const x = 100;
const y = 200;
const z = 300;

const coordinates = { x, y, z };
console.log(coordinates);

// Template literals:

const sayHello = (namee) => {
    return `Hello ${namee}!`;
};

const a = 'dasdas';

console.log(`bla bla bla  ${a}`);

let u = 10;
let i = 5;

console.log(`${u+i} equals to ${u} + ${i} `);

// parameter defaults:

function divide(a=1,b=1){
    return a/b
}

function congrats(pers='nameless'){
    return `congratuulation ${pers}`
}

function animalname(animalName='max'){
    return animalName
}

// rest/spread:

const classmates = (...rest) => {
    return `you have ${rest.length()} classmates`
}

const fruits = ["🍎", "🍌", "🍇"];
const moreFruits = [...fruits];

const numbers = [4, 7, 2, 9];

const max = Math.max(...numbers);
console.log(max);