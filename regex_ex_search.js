const re = /learn/;
const str1 = 'Today, we\'ll learn about regular expressions.';
const str2 = 'Tomorrow, we\'ll write regular expressions '
    + 'and learn some complex expressions.';
const str3 = 'We\'re all done now!';

console.log(str1);
console.log('A search for', re, 'returns', str1.search(re), '\n');
console.log(str2);
console.log('A search for', re, 'returns', str2.search(re), '\n');
console.log(str3);
console.log('A search for', re, 'returns', str3.search(re));