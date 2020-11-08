// id = btn
// width = 96px
// height = 48px
// font-size = 24px

function create(d, num) {
    let b = document.createElement('button')
    b.innerHTML = `${num}`
    b.id = `btn${num}`
    b.className = "buttonClass"
    d.appendChild(b)
}


function main2() {
    main()

    let btn5 = document.getElementById("btn5")

    let nums = [1, 2, 3, 6, 9, 8, 7, 4]
    const ids = [1, 2, 3, 6, 9, 8, 7, 4]

    btn5.onclick = function rotate() {
        nums.unshift(nums.pop())

        for (let i = 0; i <= 7; i++) {
            document.getElementById("btn" + ids[i]).innerHTML = `${nums[i]}`
        }
    }
}

function main() {
    let d = document.createElement("div")
    d.className = "buttonContainer"
    d.id = "btns"
    document.body.appendChild(d)

    for (let i = 1; i <= 9; i++) {
        create(d, i)
    }
}

main2()