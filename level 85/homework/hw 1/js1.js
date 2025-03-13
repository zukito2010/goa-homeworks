function calculate(a, b, operation) {
    switch (operation) {
        case '+':
            return a + b;
        case '-':
            return a - b;
        case '*':
            return a * b;
        case '/':
            return b !== 0 ? a / b : 'Error: Division by zero';
        default:
            return 'Error: Invalid operation';
    }
}

function filter(arr, callback) {
    let result = []; // ახალი მასივი, სადაც შევინახავთ ფილტრირებულ მნიშვნელობებს
    for (let i = 0; i < arr.length; i++) {
        if (callback(arr[i])) {  // თუ callback ფუნქციამ დააბრუნა true
            result.push(arr[i]); // ვამატებთ ახალ მასივში
        }
    }
    return result; // ვაბრუნებთ გაფილტრულ მასივს
}


module.exports = {calculate,filter};