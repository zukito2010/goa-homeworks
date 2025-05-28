import {calculate,filter} from './js1'

console.log(calculate(6,3,'*'))

// 2)
const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const isOdd = (num) => num % 2 === 1;

const oddNumbers = filter(numbers, isOdd);
console.log('Even numbers:', oddNumbers);

