const _ = require('lodash')

function useLodash(obj) {
    return _.reduce(obj, (acc, curr) => acc + curr, 0)
}

let k = {
    'a': 1,
    'b': 3,
    'c': 4,
}

let res = useLodash(k)
console.log('end')