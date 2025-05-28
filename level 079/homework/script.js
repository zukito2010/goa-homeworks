console.log('1)');
const arr1 = [1,2,3,4,5];
const arr2 = [6,7,8,9,0];

let [a , b] = [arr1, arr2];
console.log([a,b]);

[a,b] = [b,a];
console.log([a,b]);

console.log('2)');

const foods = ['kebab','bacon','khinkali','khachapuri'];

let [keb,bac,...georgian] = foods;

const actors = ['Dwayne the rock Johnson', 'Scarlet Johnanson', 'Ryan Reynolds', 'Adam Sandler','Tom Cruise','Hugh Lorie','Omar Eps'];

let [rock,widow,deadpool,...rest] = actors;

console.log(rock);
console.log(widow);
console.log(deadpool);
console.log(rest);

const nums = [1,2,3,4,5,6,7,8,9,0];

let [first,second,third,...rests] = nums;

console.log(rests);
console.log('3)');

const mergedArray = [...arr1, ...arr2];

console.log(mergedArray);

const person = { name: "George", age: 19 };
const details = { job: "Janitor", country: "Germany" };

const fullProfile = { ...person, ...details };

console.log(fullProfile);
const fruits = ["🍎", "🍌", "🍇"];
const vegetables = ["🥕", "🥒", "🌽"];

const healthyFood = [...fruits, ...vegetables];

console.log(healthyFood);
