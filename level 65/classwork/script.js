var arr1 = [1,2,3,4,5,6,7,8,9];

console.log('1)');
console.log(arr1);

var ppl = new Array('gia','lia','spongebob');

console.log('2)');
console.log(ppl);


var  arr2 = new Array(3);

arr2[0] = 3;
arr2[1] = 12;
arr2[2] = 653;

console.log('3)');
console.log(arr2);




console.log('4)');
console.log(arr1[0]);
console.log(ppl[1]);
console.log(arr2[2]);

console.log('5)');
console.log(arr1.slice(0))
console.log(ppl.slice(-3,-1))
console.log(arr2.slice(0,7))

console.log('6)');
function numInBetween(n){
    return Math.floor(Math.random() * (n + 1));
}
console.log(numInBetween(9));

console.log('7)');
let i = 0
while (i!= 30) {
    console.log(setInterval(i,5000))
    i++
}

console.log('8)');
const today = new Date();

const day = today.getDate();
const month = today.getMonth() + 1; 
const year = today.getFullYear(); 


console.log(`${day} ${month} ${year}`); 