function isman(isman){
    return isman ? 'man shoes' : 'woman shoes';

}

console.log(isman(true));

let a = 'animal' ;

function ishuman(i){
    return i ? 'human food' : 'animal food';

}

console.log(ishuman(false));


function fiveOrZero(n){
    var ing = 'm'
    return n ? 5 : 0;
}


console.log(fiveOrZero(true));
console.log(fiveOrZero(null));

let namee = document.getElementById('name');
let email = document.getElementById('email');
let password = document.getElementById('password');
const forma = document.getElementById('forma');

forma.addEventListener('submit', (e) =>{
    e.preventDefault();

    console.log(namee.value);
    console.log(email.value);
    console.log(password.value);
})

if (true && 5>4){
    console.log(true);
}

if (false && true){
    console.log('i wont show up');
}

if (false && false){
    pass;
}

//                                                                          ?            :                                                           
// ternery operator - is just like if else but inputs are true and false   if true ... else ...

// && - is and operator it returns true if every statement is true connected by && operator else false

if (true) {
    var m = "var";
    let n = "let";
    const o = "const";
    
    console.log(m); 
    console.log(n); 
    console.log(o); 
}
console.log(m)
// others wont work
