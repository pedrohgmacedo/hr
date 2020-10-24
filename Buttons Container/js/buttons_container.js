// id = btn
// width = 96px
// height = 48px
// font-size = 24px

function create(d, num) {
    let b = document.createElement('button')
    b.innerHTML = `${num}`
    b.id = `btn${num}`
    b.className = "buttonClass"
    b.addEventListener('click', rotate)
    d.appendChild(b)
}


function rotate(event) {
    let btn1 = document.getElementById("btn1")
    let btn2 = document.getElementById("btn2")
    let btn3 = document.getElementById("btn3")
    let btn4 = document.getElementById("btn4")
    let btn5 = document.getElementById("btn5")
    let btn6 = document.getElementById("btn6")
    let btn7 = document.getElementById("btn7")
    let btn8 = document.getElementById("btn8")
    let btn9 = document.getElementById("btn9")

    let b1 = btn1.innerHTML
    let b2 = btn2.innerHTML
    let b3 = btn3.innerHTML
    let b4 = btn4.innerHTML
    let b7 = btn7.innerHTML
    let b6 = btn6.innerHTML
    let b8 = btn8.innerHTML
    let b9 = btn9.innerHTML

    btn1.innerHTML = b4
    btn2.innerHTML = b1
    btn3.innerHTML = b2
    btn4.innerHTML = b7
    btn7.innerHTML = b8
    btn6.innerHTML = b3
    btn8.innerHTML = b9
    btn9.innerHTML = b6
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

main()