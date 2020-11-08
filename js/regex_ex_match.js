var re = /see (chapter \d+(\.\d)*)/i;
//  matches: 
// see 
// () -> remembers the match
// chapter 
// \d -> digit
// + at least 1
// () -> group 2
// \. escaped dot
// \d digit
// * preceding item 0 or more. 

// matches: chapter number.number, or chapter number

// does not talk about greedy or lazy regexes

var str = 'For more information on regular expressions, see Chapter 3.4.5.1 and CHAPTER 2.3';

console.log(str.match(re));