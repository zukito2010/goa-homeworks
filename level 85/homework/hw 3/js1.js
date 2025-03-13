export function calculate(a, b, operation) {
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

export function filter(arr, callback) {
    let result = []; 
    for (let i = 0; i < arr.length; i++) {
        if (callback(arr[i])) { 
            result.push(arr[i]); 
        }
    }
    return result; 
}

