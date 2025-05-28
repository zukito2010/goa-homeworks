const arr = [1,2,3];

for (let i of arr){
    console.log(i)
}
console.log('____________________________________________________________________');
const arr1 = [5,'5',true,'5.0',1,7,5.0];

for (let i of arr1){
    if (i == 5){
        console.log(i)
    }else{
        console.log('not five')
    }
}
console.log('____________________________________________________________________');

for (let i of arr1 ){
    if (i===5){
        console.log('fivee')
    }else if (i==5) {
        console.log('not my fivee')
        
    }else{
        console.log('not fivee')
    }

}
// * we can use this type of loops only for lists, sets, string etc. but can`t use for objects, numbers and booleans

// * 2)

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

// * we can use for in loops for strings and objects.(also for arrays but it is not recommended)

// * 3)

const subst = (a,b) =>{
    return a-b
}

const add = (a,b) =>{
    return a+b
}


// * 4)

const add1 = (a,b=5) =>{
    return a+b
}

console.log(subst(5,1))
console.log(add(5,1))
console.log(subst(5,))