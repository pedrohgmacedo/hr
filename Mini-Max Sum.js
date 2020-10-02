function removeNSmallest(arr, n){
    if (n == 0) {
        return arr
    }

    return removeNSmallest(removeMin(arr) , n-1)
}

function removeNLargest(arr, n){
    if (n == 0) {
        return arr
    }

    return removeNLargest(removeMax(arr) , n-1)
}

function removeMin(arr){
    return arr.filter((el, ind, arr) => {
        return (ind !== arr.indexOf(Math.min(...arr)))
    })
}

function removeMax(arr){
    return arr.filter((el, ind, arr) => {
        return (ind !== arr.indexOf(Math.max(...arr)))
    })
}


function sum(arr) {
    return arr.reduce( (acc, curr) => acc+curr)
}