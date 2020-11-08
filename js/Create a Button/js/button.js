// id = btn
// width = 96px
// height = 48px
// font-size = 24px

let b = document.createElement('button')
b.innerHTML = "0"
b.id = "btn"

b.addEventListener('click', increment)

function increment(event) {
    event.srcElement.innerHTML = (parseInt(event.srcElement.innerHTML) + 1)
}

document.body.appendChild(b)