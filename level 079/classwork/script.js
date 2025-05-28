// 1)
const user_ = { 
    name: "John", 
    address: { city: "New York", zip: 10001 } 
  };
  
  const { address: { city } } = user_;
  
  console.log(city);

console.log('__________________________________');

const person = {
    firstName: "John",
    lastName: "Doe",
    age: 50
  };

let {firstName, lastName} = person;
const numbers = [10, 20, 30];

const [a, b, c] = numbers;

const [, second, third] = numbers; 
console.log(second); 
console.log(third);  

console.log('__________________________________');

function greet({ name, age }) {
    console.log(`Hello, ${name}! You are ${age} years old.`);
  }

const user = { name: "Merabi", age: 29 };
greet(user);

console.log('__________________________________');

// 2)
let x,y,rest_;
[x,y] = [10,20,];
console.log(x);
console.log(y);
[x, y, ...rest_] = [10, 20, 30, 40, 50];
console.log(rest_);

console.log('__________________________________');
let aa,bb,cc,rest;

[aa,bb,cc] = ['zuka','luka','nika',];
[aa,bb,cc, ...rest] = ['zuka','luka','nika','genadi','qishvardi'];
console.log(rest)

let a1,b1,c1,rest1;

[a1,b1,c1] = ['zuka','luka','nika',];
[a1,b1,c1, ...rest1] = ['zuka','luka','nika','manana','qishvardi'];
console.log(rest1)

console.log('__________________________________');

// 3) 
const arr1 = [1, 2, 3];
const arr2 = [4, 5, 6];

const mergedArray = [...arr1, ...arr2];

console.log(mergedArray); 

console.log('__________________________________');

const word = "Hello";
const letters = [...word];

console.log(letters);

console.log('__________________________________');

const numbers_ = [2, 3, 4];
const newNumbers = [1, ...numbers_, 5];

console.log(newNumbers); 

console.log('__________________________________');


// The spread operator (...) is used to expand elements from arrays or objects. It helps when merging arrays, copying objects, or passing elements as function arguments. For example, [...arr1, ...arr2] merges two arrays, and {...obj} creates a copy of an object.

// On the other hand, the rest operator (...) is used to collect multiple elements into a single array or object. It appears in function parameters to gather arguments (function sum(...nums)) and in destructuring to capture remaining elements (const [first, ...rest] = arr).

// In short, spread expands data, while rest collects it.