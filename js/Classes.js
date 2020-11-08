function Polygon(sides) {
    this.sides = sides
    this.perimeter = perimeter
}

function perimeter() {
    return this.sides.reduce((acc, val) => acc + val, 0)
}

let p = new Polygon([3, 3])
console.log(p.perimeter())
