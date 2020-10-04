function isPositive(a) {
    if (a === 0) {
        throw new Error('Zero Error')
    } else if (a < 0) {
        throw new Error('Negative Error')
    }
    return 'YES'
}

function foo() {
    return
    {
        bar: "test"
    }
}

console.log(foo())
console.log("done")