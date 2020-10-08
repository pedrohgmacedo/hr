function modifyArray(nums) {
    return nums.map((val) => {
        return (val % 2 == 0) ? val * 2 : val * 3
        // if (val % 2 == 0) {
        //     return val * 2
        // }
        // if (val % 2 != 0) {
        //     return val * 3
        // }
    })
}

let nums = [1, 2, 3, 4, 5]
console.log(modifyArray(nums))