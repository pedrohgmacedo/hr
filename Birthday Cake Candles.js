function countTallestSlow(candles){
    return candles.reduce(
        (acc, curr) => {
            if (curr == Math.max(...candles)){
                return (acc+=1)
            }
            return acc
        }, 0
    )
}

function countTallestFast(candles) {
    let max = Math.max(...candles)
    return candles.filter(el => el === max).length
}

console.log(countTallestFast([4,4,3,1]))
