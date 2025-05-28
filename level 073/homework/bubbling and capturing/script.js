// 2) Hoisting - js feature that makes every function that is not an anonymous, go to the top of the code, when we run the code.(so arrow functions do not have hoisting while functions that use keyword 'function' have.)

// 3) bubbling and capturing test
const child = document.getElementById('child');
const parent = document.getElementById('parent');

parent.addEventListener('click', e => {
    console.log('i am a PARENT');
}, true);// if 3rd parameter of addevetnlistener is true it will go from parent to its youngest child but if its false it will go from that parent to its parent and so on and so on.

child.addEventListener('click', e => {
    console.log('i am a CHILD');
});


