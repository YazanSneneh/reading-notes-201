# JavaScript error messages && debugging
 * as a developer most of the time i will spend time dealing with errors.
 * and in order to handle errors am should use errors messages from console of browser or terminal where I like to read it or not.

## types of errors i will be dealing with:

### syntax error : 
* when i run javascript code, the v8 engine parse the code and check for syntax errors before they construct an abstract syntax tree.
* when syntax  error found, there will be message in console say  `error type : syntax error`.
* e.g.  JSON.parse({'key':'value'})  ===> message syntax error similar to this `Uncaught SyntaxError: Unexpected token o in JSON at position 1`.

### reference error : 
  * when i try to use a variable not defined i receive this error.
  * it means i am trying to use variable that is not refering to a value inside the memory.
  * it also happen when i try to use a variable before it's declaration like `let and const`.
  * to solve it declare it before using it.


### range error:
* it happen when i try to access index in array like `-1`, because array start from `0`.
* for example 
```
 let arr = []
 console.log(arr.length -1)
```
### Type errors
* type errors happen when i try to perform incompatable code with the variable type.
* for example run number method or array method on variable hold *undefined* value.
* to solve this just make sure to declare the variable correctly.


## Debugging in JavaScript:
 * one way to console.log **variable** or the **expected error** i want to check.
 * other way is to use breakpoint can  be achieved by putting a debugger statement in your code in the line you want to break.
 * this is handy when i want to debug huge cycles for specific values.
 * example the breakpoint will point stop when the index reaches 40.
 * I can do it in **Node.js** as well by open debug tab and configure it like this.
 * I can run the debugger by pressing F5.

# Call stack
* the call stack is the way my program has been implemented until the point where i will get error.
