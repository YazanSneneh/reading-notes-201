# Functional Programming
  * a paradigm, a style of building the structure and elements of computer programs
  * to understand functional programming we should understand pure functions.

### pure functions
  * It returns the same result if given the same arguments.
  * it does not cause any side effect.
  * if it's **not pure** then it's using a **variable was not passed** as a parameter.
  * so **pure** functions do calculations and return value** result of passed parameter**.
  * when it also read an **external file** it's **not pure**.
  * Any function that **relies on a random number** generator **cannot be pure**, because it rely on global variable.
  * if **modify global** variable it's **not pure** function.
  * Pure functions are stable, consistent, and predictable.

##### Pure functions benefits
 * easier to test.
 * easier to deal with it.
 * it does not change original values or global value only parameters.

##### Higher-order functions
 * a function take another function as a parameter, e.g. eventListener.
 * a function return function as result.

##### Filter
 * filter array based on giving condition and return new array.
 * if we want to achieve result of filter we will use for loop nad loop over array then use if statement then push to array then return, it's called Imperative.

##### Reduce
  * it receive collection or array, and return value based on combine items.

# Refactoring JavaScript for Performance and Readability
* functions like map filter reduce etc.. make code more readable and easier to modify or deal with.
* also it reduce code.
