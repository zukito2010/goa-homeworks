//1) use slicing on array 3 times
let arr1 = new Array(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20);
let slice1 = arr1.slice(1,8);
let slice2 = arr1.slice(-2,-9);
let slice3 = arr1.slice(-5);
console.log(arr1)
console.log(slice1);
console.log(slice2);
console.log(slice3);

console.log(' ');
//2) return exact time of right now
let date = new Date();
console.log(`${date.getFullYear()}/${date.getMonth() + 1}/${date.getDate()}/${date.getHours()}/${date.getMinutes()}/${date.getSeconds()}`);

console.log(' ');
//3) password generator
let symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789!@#$';
let yourpass = [];
for (let i = 0; i<12;i++){
    yourpass.push(`${symbols[Math.floor(Math.random()*65)]}`);
}
console.log(yourpass.join(''))