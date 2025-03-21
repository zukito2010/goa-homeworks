// Promise - in js is an object that represents the eventual completion (or failure) of an asynchronous operation and its resulting value.

// 2)
function resolveData(num) {
    return new Promise((resolve, reject) => {
        console.log(`Checking if ${num} is even...`);

        setTimeout(() => {
            if (num % 2 === 0) {
                resolve(`${num} is even.`); 
            } else {
                
            }
        }, 2000);
    });
}
resolveData(10) 
    .then(message => console.log("Success:", message))
    .catch(error => console.error("Error:", error));


// 3)
function rejectData(num) {
    return new Promise((resolve, reject) => {
        console.log(`Checking if ${num} is even...`);
        setTimeout(() => {
            if (num < 0) {
                reject("Error: Negative number cannot be processed"); 
            } else {
                reject(`${num} is rejected!`); 
            }
        }, 2000);
    });
}

rejectData(7)  
    .then(message => console.log("Success:", message))
    .catch(error => console.error("Error:", error));





// 4)
function isEvenNumber(num) {
    return new Promise((resolve, reject) => {
        console.log(`Checking if ${num} is even...`);
        setTimeout(() => {
            
            if (num % 2 === 0) {
                resolve(`${num} is even.`);
            } else {
                reject(`${num} is odd.`);
            }
        }, 1500); 
    });
}

isEvenNumber(10)
    .then(message => console.log("Success:", message))
    .catch(error => console.error("Error:", error));

isEvenNumber(7)
    .then(message => console.log("Success:", message))
    .catch(error => console.error("Error:", error));

