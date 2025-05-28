// 1)
const myPromise = new Promise((resolve) => {
    resolve("Hello, Promise!");
  });
  
myPromise.then(message => {
    console.log(message); 
});

// 2)
let num1 = 5
let num2 = 10
const myPromise2 = new Promise((resolve, reject) => {
    if (num1>num2) {
      resolve("It worked!");
    } else {
      reject("Something went wrong.");
    }
  });
myPromise2
  .then(result => {
console.log(result);
})
  .catch(error => {
console.error(error); 
});
// 3)
const twoSec = new Promise((resolve,reject) => {
    setTimeout(() => {
        resolve('even this two seconds felt like two centuries');
    },2000);
});

twoSec.then(msg => {
    console.log(msg)
})
// 4)
const fiftyFifty = new Promise((resolve, reject) => {
    const randomNum = Math.floor(Math.random() * 2); 
    if (randomNum) {
        resolve('Success!');
    } else {
        reject('Failed!');
    }
});

fiftyFifty
  .then(result => {
    console.log(result); 
  })
  .catch(error => {
    console.error(error); 
  });

// 5)
const fiveTimesTwo = new Promise((resolve, reject) => {
    resolve(5);
  });
  
fiveTimesTwo
.then(number => {
    return number * 2;
})
.then(number => {
    return number * 2; 
})
.then(number => {
    return number * 2; 
})
.then(result => {
    console.log("Final Result:", result); 
})
.catch(error => {
    console.error("Error:", error);
});

// 6) 
const fetching = new Promise((resolve, reject) => {
    setTimeout(() => {
        resolve("successfully fetched");
    }, 1000);
});

fetching
.then(response => {
    console.log(response);
})
.catch(error => {
    console.error("Error:", error);
});