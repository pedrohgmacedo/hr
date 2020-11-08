# Example 1 - increment by 1

```html
<!DOCTYPE html>
<html>
  <head>
    <style>
      .buttonContainer {
        width: 148px;
      }

      .buttonContainer > .buttonClass {
        width: 72px;
        height: 48px;
        font-size: 16px;
      }
    </style>
  </head>

  <body>
    <div id="btns" class="buttonContainer">
      <button id="btn1" class="buttonClass">1</button>
      <button id="btn2" class="buttonClass">2</button>
      <button id="btn3" class="buttonClass">3</button>
      <button id="btn4" class="buttonClass">4</button>
    </div>

    <script>
      document.getElementById("btn1").onclick = function () {
        document.getElementById("btn1").innerHTML++;
      };

      document.getElementById("btn2").onclick = function () {
        document.getElementById("btn2").innerHTML++;
      };

      document.getElementById("btn3").onclick = function () {
        document.getElementById("btn3").innerHTML++;
      };

      document.getElementById("btn4").onclick = function () {
        document.getElementById("btn4").innerHTML++;
      };
    </script>
  </body>
</html>
```

# Single function for all buttons

## Onclick

```html
<!DOCTYPE html>
<html>
  <head>
    <style>
      .buttonContainer {
        width: 148px;
      }

      .buttonContainer > .buttonClass {
        width: 72px;
        height: 48px;
        font-size: 16px;
      }
    </style>
  </head>

  <body>
    <div id="btns" class="buttonContainer">
      <button id="btn1" class="buttonClass">1</button>
      <button id="btn2" class="buttonClass">2</button>
    </div>

    <script>
      function action(e) {
        var btn = e.srcElement;

        /* Get the clicked element's innerHTML */
        document.getElementById(btn.id).innerHTML++;
      }

      /* Set each button to call action(e) when clicked */
      document.getElementById("btn1").onclick = action;
      document.getElementById("btn2").onclick = action;
    </script>
  </body>
</html>
```

## Event Listener

```html
<!DOCTYPE html>
<html>
  <head>
    <style>
      .buttonContainer {
        width: 148px;
      }

      .buttonContainer > .buttonClass {
        width: 72px;
        height: 48px;
        font-size: 16px;
      }
    </style>
  </head>

  <body>
    <div id="btns" class="buttonContainer">
      <button id="btn1" class="buttonClass">1</button>
      <button id="btn2" class="buttonClass">2</button>
    </div>

    <script>
      /* Parameter 'e' is the click Event */
      function action(e) {
        var btn = e.srcElement;

        /* Get the clicked element's innerHTML */
        document.getElementById(btn.id).innerHTML++;
      }

      /* Add a click event listener that calls action(e) when clicked */
      document.getElementById("btn1").addEventListener("click", action);
      document.getElementById("btn2").addEventListener("click", action);
    </script>
  </body>
</html>
```

# Resources and tips

## the eval function

```js
const expression = 5 + 2 - 3;
console.log(eval(expression));
```

## binary numbers to integer strings

```js
const two = "10";
console.log(parseInt(two, 2));

const three = "11";
console.log(parseInt(three, 2));

const five = "101";
console.log(parseInt);

const nine = three;
console.log(parseInt(nine, 8));
```

## Integer division

```js
const result = 3 / 2;
console.log(result);
console.log(Math.floor(result));
```
