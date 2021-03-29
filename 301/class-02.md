# JQUERY
JQUERY provide me methods help me to apply effects on the webpage. make it easier to apply certain actions and transitions.

all methods accept time in milesecond (1000 is 1 second) it's timing take applying the effect.

   1. hide/ show. 
            hide() : hide element from page.

            show(): show element on page.

            toggle() : if its hidden it appear, if it's seen toggle hide it.

2. fadeIn/fadeOut():
             fadeIn(): show element on screen fade in behaviour.

             fadeOut() : hide element on page fade out behaviour.

             fadeToggle() : if its hidden it appear fade in, if it's seen, hide it fade out.

3. slideDown/slideUp
           slideDown(): element appear on page from top to bottom.

           slideUp() : element disappear on page from bottom to top.

           slideToggle() : switch between slideDown and slideUp.

4. animate() : it take 2 parameters : 1 object css rules written in json format seperate by comma. and the other is time in milesecond (1000 is one second).

# Summary 
* it's a javascript library, written by someone else and I can find it in the **CDN** servers, that means if I want to incoporate it in my project:
    * I either use the CDN provided link  using `<script src ='url'> </script >`.
    *  Download the files and use it.

* Jquery allow me to write less and simpler code.
* jquery is library used for **DOM** manipulation.
* Order matter where I include Jquery file because browser read from top to bottom and left to right, and if Jquery incoporated after my app.js browser will read app.js first and see Jquery syntax therefore a syntax error, to avoid this:
    * Always use cdn before `<script src ='js/app.js'> </script >`.
    * Use `document.ready( functionHere(){  my code })`, this line means when the document that contain all the html ready this code should work and will not lead to syntax error.

## Jquery syntax:
 1. to select element using jquery i  use this syntax `$('selector')`. 
    * I can select classes`$('.class')` , id`$('#id')`, tags`$('tag')`, and so on.

2. to add event to element i use `$(' ').on('event', callback function)` or `$(' ').event(callback)`.

* class methods : 
.addClass(), .removeClass(), .toggleClass() : i can add more than 1 class as well.

* hide/show elements : 
   * hide(),show(), toggle() : hide and show element on page(apply display property).

* hide/show with fade animation: 
   * fadeIn() fadeOut toggleFade(), pop up and disappear elements on page.

* `$('<div></div>')` create element div in jquery : then i use newParent.append().

* **callback** : it's a function can be passed as parameter to another function, like functions in events or js helper functions.

## Arrow Functions
* arrow functions are another way of writing a function, they help me right less and easier functions.

  * when there is only 1 parameter passed to arrow function i can remove parentheses like so :
``` 
const fun = x=> {
         x =x+x
        console.log(x)
}
```
* when there is only 1 statement written in arrow functions i can remove curly braces along with return like so :
   `const fun = x=>  console.log(x)`
* this keyword and arrow functions: 
   * arrow functions don't bind this keyword
* When I write method for object and call it on the object then console this, it return the  object itself.
   * if i write it with regular function it will return the window object.
* on the other hand arrow functions can't bind this, so it will return the window object always.

## Pass Data by Value & by Reference
* If variables are boxes, then variable names are labels to that box. and what inside that box is data. and that box reserve a space in a room.

* So when I create a variable the name gonna be a label to the location where data live inside memory.
* Passing data **by value** means I make a copy of variable inside another variable, which means will reserve another location to store the new copy.
   * which means when I edit one, the other **will not be affected**, an example:
```
let a = 5;
let b = a;
a = 20;
console.log(b)  // 5.
```
 * Passing **data by reference** means I assign the new variable to **store the location where data live**, just like old variable, meaning when data inside these 2 variables changed from 1 variable the **original will change**, example:
```
let obj = {name: 'yazan'}
let obj2 = obj;
obj2.name = 'ali';
console.log(obj)   // {name:'ali'}
```
* **Primitive** datatypes are **passed by value** (strings, numbers, bools...)

* **Block** or complex datatype are **passed by reference** (obj, arrays and functions).

* If I use passing data by reference I sacrifice flexibility, and if I use pasing by value I sacrifice space.

**note: it's important to remember this because when you pass an object to function and change on it, it will change on original object.**