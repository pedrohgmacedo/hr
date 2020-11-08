

class Chain {
    constructor() { }

    add(str, prop) {
        this[str] = prop
        return this
    }

    remove(str) {
        delete this[str]
        return this
    }

    printKeys() {
        console.log(Object.keys(this))
        return this
    }

    printVals() {
        console.log(Object.values(this))
        return this
    }
}

let k = new Chain()
k.add("hello", 10).add("howdy", 20).add("god", 15).printKeys().printVals().remove("hello").printKeys()
