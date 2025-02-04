/**
 * @param {string[]} tokens
 * @return {number}
 */
var evalRPN = function (tokens) {
    let myStack = []
    for (let token of tokens) {
        if (token === "+") {
            let a = myStack.pop()
            let b = myStack.pop()
            myStack.push(a + b)
        }
        else if (token === "-") {
            let a = myStack.pop()
            let b = myStack.pop()
            myStack.push(b - a)
        }
        else if (token === "*") {
            let a = myStack.pop()
            let b = myStack.pop()
            myStack.push(b * a)
        }
        else if (token === "/") {
            let a = myStack.pop()
            let b = myStack.pop()
            myStack.push(Math.trunc(b / a))
        } else {
            myStack.push(parseInt(token))
        }
    }
    return myStack.pop()
};