// 1)
const arr1 = [4+2,'2','7-1',true,'6.0',1,7,6.0];

for (let i of arr1){
    if (i == 6){
        console.log(i)
    }else{
        console.log('not six')
    }
}
console.log('____________________________________________________________________');

for (let i of arr1 ){
    if (i===5){
        console.log('my six')
    }else if (i==5) {
        console.log('not my six')
        
    }else{
        console.log('not six')
    }

}
const arr = [1,2,3];

for (let i of arr){
    console.log(i)
}

// 2)

let deString = 'abcdef';

for (let i in deString){
    console.log(i);
}
console.log('_');

for (let i in deString){
    console.log(deString[i]);
}

console.log('_');

for (let i in deString){
    if (deString[i] == 'a'){
        console.log(deString[i]);
    }
    else {
        console.log(deString[i] + ' is not an a')}
}

// 3)
const subst = (a,b) =>{
    return a-b
}

const add = (a,b) =>{
    return a+b
}
const mult = (a,b) =>{
    return a*b
}
