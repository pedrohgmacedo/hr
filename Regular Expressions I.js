// return a regexp object re that matches any string s, that begin and ends with the same vowel.

let s = "abcda";

function regexVar() {
    let re = /^([aeiou]).+\1$/;
    return re;
}


console.log(regexVar().test(s));
