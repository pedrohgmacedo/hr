// constructor
function Rectangle(a, b) {
    this.length = a
    this.width = b
    this.perimeter = 2 * (a + b)
    this.area = a * b
}

var rect = {
    length: 2
    width: 4
}

rect.area = 2 * 8

var rect2 = new Object()
var rect3 = Object.create()


// instantiation: new Rectangle(2, 4)