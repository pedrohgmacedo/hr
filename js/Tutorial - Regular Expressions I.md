const re1 = /ab+c/;

const re = new RegExp('ab+c');;

// syntax
// new RegExp(pattern[, flags])

// regex literal:
// /pattern/flags

# character sets:

[abcd] will match the set {a,b,c,d}
[^abcd] anything but the set

# alteration

The symbol | matches one thing or the other. a|b either a or b

// Character classes:
// enclose within square brackets: matches any
// [a-f] will match any lowercase a through f
// [^a] will match any not a
// predefined: \<letter>
// . matches any single character, except line terminators
// \d: digit
// \D: non digit
// \w: word single alphanumeric including underscore
// \W: non word
// \s: whitespace, space, tab, form feed, line feed
// \S: non whitespace
// ^: beginning of input
// $: end of input.
// \b: zero-width word boundary, such as between letter and space
// \B: zero-width non-word boundary, such as between two letters or between two spaces

// grouping and back references:
// (a) matches and remembers the match. It's called a capturing group
// (?:a) matches but does not remember the match. It's called a non capturing group.
// \n: n is a non positive integer. It's a back reference to capturing group

# Quantifiers:

a*: mathces preceding item a, 0 or more times
a+: matches the preceding item a, 1 or more times
a?: matches the preceding item a, 0 or 1 times
a{n}: matches exactly n occurrences of preceding item a
a{n,} matches at least n occurrences
a{n,m} matches at least n and at most m occurrences of preceding item a.
<quantifier>? makes a quantifier lazy. by default its greedy

# Assertions: 

^ asserts at beggining of string
& asserts the end
()\1, where \1 matches the most recent of whats in capturing group 1 
a(?=b) matches a if a is followed by b.
a(?!b) matches a only if a is not followed by b

# Methods: 

Regexes work with regex methods `test` and `exec`, and string methods `match`, `search`, `split`, `replace`.

Test: searches for a match, and returns true of false. 
exec: searches for a match, and returns a result array or null. 

    