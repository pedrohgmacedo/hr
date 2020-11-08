# Template

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Page Title</title>
    <link rel="stylesheet" href="css-file-path" type"text/css">
    <style>
      /* Write CSS styles here */
    </style>
  </head>
  <body>
    <script src="js-file-path" type="text/javascript">
      /* Write JS code here */
    </script>
    <button id="buttonIdentifier" class="buttonStyleClass">Click Me</button>
  </body>
</html>
```

# css

ID Selector:

````css
#myButtonId { /* Set the background color to a shade of green */ background:
#4FFF8F; /* Center-align the text */ text-align: center; /* Set the cursor to be
a pointer */ cursor: pointer; } # modifying button ```js let clickMeButton =
document.createElement("button"); clickMeButton.id = "myButton";
clickMeButton.innerHTML = "Click Me 2"; clickMeButton.style.background =
"green"; document.body.appendChild(clickMeButton); let otherButton =
document.getElementById("myButton"); clickMeButton.innerHTML = "This is my new
label text";
````

class selector:

```css
.myStyleClass {
  /* Set the background color to a shade of green */
  background: #4fff8f;
  /* Center-align the text */
  text-align: center;
  /* Set the cursor to be a pointer */
  cursor: pointer;
}
```

# Click events

The flow is: get element by id, then on this element set property onclick, or some other propety

Using `onclick`:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Page Title</title>

    <style>
      .buttonClass {
        color: #4caf50;
      }
    </style>
  </head>

  <body>
    <!-- This puts a button with the id 'button id' on our page. -->
    <button id="buttonId" class="buttonClass">I am a button!</button>

    <script>
      /* This assigns the element with id 'buttonId' to 'btn' */
      var btn = document.getElementById("buttonId");

      /* This sets the action to perform on a click event */
      btn.onclick = function () {
        /* This changes the button's label */
        btn.innerHTML = "You clicked me!";
      };
    </script>
  </body>
</html>
```

Using `addEventListener`:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Page Title</title>

    <style>
      .buttonClass {
        color: #4caf50;
      }
    </style>
  </head>

  <body>
    <!-- This puts a button with the id 'button id' on our page. -->
    <button id="buttonId" class="buttonClass">I am a button!</button>

    <script>
      /* This assigns the element with id 'buttonId' to 'btn' */
      var btn = document.getElementById("buttonId");

      /* This sets the action to perform on a click event */
      btn.addEventListener("click", function () {
        /* This changes the button's label */
        btn.innerHTML = "You clicked me!";
      });
    </script>
  </body>
</html>
```
