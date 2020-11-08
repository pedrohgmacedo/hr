let res = document.createElement("div");
let btns = document.createElement("div");
let btn0 = document.createElement("button");
let btn1 = document.createElement("button");
let btnClr = document.createElement("button");
let btnEql = document.createElement("button");
let btnSum = document.createElement("button");
let btnSub = document.createElement("button");
let btnMul = document.createElement("button");
let btnDiv = document.createElement("button");


res.id = "res";
btn0.id = "btn0";
btn1.id = "btn1";
btnClr.id = "btnClr";
btnEql.id = "btnEql";
btnSum.id = "btnSum";
btnSub.id = "btnSub";
btnMul.id = "btnMul";
btnDiv.id = "btnDiv";

btn0.innerHTML = "0";
btn1.innerHTML = "1";
btnClr.innerHTML = "C";
btnEql.innerHTML = "=";
btnSum.innerHTML = "+";
btnSub.innerHTML = "-";
btnMul.innerHTML = "*";
btnDiv.innerHTML = "/";


document.body.style.width = '33%';

res.style.backgroundColor = "lightgray";
res.style["font-size"] = '20px';
res.style["border"] = "solid";
res.style["height"] = "48px";

btn0.style.backgroundColor = "lightgreen";
btn0.style["color"] = "brown";

btn1.style["background-color"] = "lightgreen";
btn1.style["color"] = "brown";

btnClr.style["background-color"] = "darkgreen";
btnClr.style["color"] = "white";

btnEql.style["background-color"] = "darkgreen";
btnEql.style["color"] = "white";

btnSum.style["background-color"] = "black";
btnSum.style["color"] = "red";

btnSub.style["background-color"] = "black";
btnSub.style["color"] = "red";

btnMul.style["background-color"] = "black";
btnMul.style["color"] = "red";

btnDiv.style["background-color"] = "black";
btnDiv.style["color"] = "red";

[btn0, btn1, btnClr, btnEql, btnSum, btnSub, btnMul, btnDiv].forEach(el => btns.appendChild(el));

document.body.append(res);
document.body.append(btns);

let fuckTypescript = btns.querySelectorAll("*");

fuckTypescript.forEach(el => {
    el.style["width"] = '25%';
    el.style["height"] = '36px';
    el.style["font-size"] = '18px';
    el.style["margin"] = '0';
    el.style["float"] = 'left';
});

let stack = {};
stack.var1 = [];
stack.var2 = [];
stack.op = "not";

document.getElementById("btn1").onclick = function () {
    if (stack["op"] == 'not') {
        stack["var1"].push("1");
        stack["op"] = ("not");
        res.innerHTML = `${stack["var1"].join("").toString(2)}`;
    } else {
        stack["var2"].push("1");
        res.innerHTML = `${stack["var1"].join("")}${stack["op"]}${stack["var2"].join("")}`;
    }
};

document.getElementById("btn0").onclick = function () {
    if (stack["op"] == 'not') {
        stack["var1"].push("0");
        stack["op"] = ("not");
        res.innerHTML = `${stack["var1"].join("").toString(2)}`;
    } else {
        stack["var2"].push("0");
        res.innerHTML = `${stack["var1"].join("")}${stack["op"]}${stack["var2"].join("")}`;
    }
};

document.getElementById("btnSum").onclick = function () {
    if (stack["op"] == "not") {
        stack["op"] = "+";
    }
};

document.getElementById("btnClr").onclick = function () {
    stack["op"] = "not";
    stack["var1"] = [];
    stack["var2"] = [];
    res.innerHTML = ``;
};

document.getElementById("btnMul").onclick = function () {
    if (stack["op"] == "not") {
        stack["op"] = "*";
    }
};

document.getElementById("btnSub").onclick = function () {
    if (stack["op"] == "not") {
        stack["op"] = "-";
    }
};

document.getElementById("btnDiv").onclick = function () {
    if (stack["op"] == "not") {
        stack["op"] = "/";
    }
};

document.getElementById("btnEql").onclick = function () {
    let op = stack["op"];
    let ls = parseInt(stack["var1"].join(""), 2);
    let rs = parseInt(stack["var2"].join(""), 2);

    if (op == "*") {
        res.innerHTML = (ls * rs).toString(2);
    }

    if (op == "/") {
        res.innerHTML = Math.floor(ls / rs).toString(2);
    }

    if (op == "+") {
        res.innerHTML = (ls + rs).toString(2);
    }

    if (op == "-") {
        res.innerHTML = (ls - rs).toString(2);
    }

    stack.var1 = res.innerHTML.split("");
    stack["var2"] = [];
    stack["op"] = "not";

};

