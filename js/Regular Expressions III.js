// Task

// Complete the function in the editor below by returning a RegExp object, , that matches every integer in some string .

// Constraints

// The length of string  is  .
// It's guaranteed that string  contains at least one integer.
// Output Format

// The function must return a RegExp object that matches every integer in some string .

let s = "102, 1948948 and 1.3 and 4.5"

function regexVar() {
    let re = /\d+/g
    return re
}


console.log(regexVar().test(s))
