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


// ES6 - (EmmaScript6) is updated version of ES5 which added new functions and stuff like const and let declaration.

// Scope - variables that are inside of the code block cannot be accessed from higher levels of indentation, like you can't access variable in for loop outside forloop ,but you can access outside variables from inside forloops.

let name1 = "Luke";
console.log(`Hello, ${name1}!`); 

let text = `This is 
a multiline
string.`;
console.log(text);

function greet(name) {
    return `Hello, ${name}!`;
}
console.log(greet("Nick")); 


let a = 5, b = 10;
console.log(`Sum: ${a + b}`); 


function isAdult(age){
    return 'Truly adult' ? age>=18:'child'; 
}

console.log(isAdult(19));

function getFee(isMember){
    return isMember ? '$2.00' : '$10.00';
}
  
console.log(getFee(true));
  
console.log(getFee(false));

const greeting = (person) => {
    const name = person ? person.name : "stranger";
    return `Howdy, ${name}`;
  };



true && console.log(' ')
1>2 && console.log('1 ')
1<2 && conmsole.log('2 ')