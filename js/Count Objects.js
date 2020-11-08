function countObjects(s) {
    return s.reduce((acc, curr) => {
        if (curr.x == curr.y) {
            return acc += 1
        }
        return acc
    }, 0)
}

let a = [{ x: 1, y: 1 }, { x: 1 }, { y: 1 }, { x: 3, y: "banadas" }]

console.log(countObjects(a))
