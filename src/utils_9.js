// Simple calculator module
class Calculator {
    add(a, b) {
        return a + b;
    }
    
    subtract(a, b) {
        return a - b;
    }
    
    multiply(a, b) {
        return a * b;
    }
    
    divide(a, b) {
        if (b === 0) {
            throw new Error('Cannot divide by zero');
        }
        return a / b;
    }
}

module.exports = Calculator;


// Update 11
function newFunction11() {
    return 11;
}


// Update 13
function newFunction13() {
    return 13;
}
