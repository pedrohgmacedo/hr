// Task

// Complete the function in the editor below by returning a RegExp object, , that matches any string  satisfying both of the following conditions:

// String  starts with the prefix Mr., Mrs., Ms., Dr., or Er.
// The remainder of string  (i.e., the rest of the string after the prefix) consists of one or more upper and/or lowercase English alphabetic letters (i.e., [a-z] and [A-Z]).
// Constraints

// The length of string  is  .
// Output Format

// The function must return a RegExp object that matches any string  satisfying both of the given conditions.

// https://blog.codinghorror.com/regular-expressions-now-you-have-two-problems/
let s = "Mr.x";

function regexVar() {
    let re = /^(Mr|Mrs|Ms|Dr|Er)(\.)(\w)+$/;
    // /^(a|e|i|o|u).*\1$/
    return re;
}


console.log(regexVar().test(s));
