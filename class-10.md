# Errors handling and debugging 
   * Programming is like problem solving: you are given a puzzle and not only do you have to solve it, but you also need to create the instructions that allow the computer to solve it.

   * The error messages that a browser gives look cryptic at first, but they can help you determine what went wrong in your JavaScript and how to fix it.

### why understand how js executed?
   * understand how the language work, help developer :
      * write good code. 
      * debug code.
      
### where js code run ?
   * javascript code is executed inside environment (a program) that can read and understand js code, such as the browser (that we been using so far) or different environment such as node.js(environment allow me to write js code out of the browser).
   * each browsers use different js engines(the programs that understand js code), chrom use v8 engine (the fastest).

#### javascript engine
  it's the host that accept my js code and run it, it contain parser, syntax tree.

  ![inside the maze v8 engine ](media/javascript%20engine.png)

   1. parser : parse the syntax of my js code and check for syntax error.
      * if there is error will send error message.
      * if correct will generate an **abstract tree**.
   2. Abstract tree convert generated tree into machine code.
   3. machine code is the code the computer understand and execute.


### Execution Stack
   * it's basically in which order the code executed.
[watch this awesome video for clear picture](media/4.%20Execution%20Contexts%20and%20the%20Execution%20Stack.mp4)

#### execution context
   * the execution context is a object where the code executed.
   * **default execution context** is for code and functions that not inside any functions.
   * default execution context is associated with the window object, which is why when we create anything gets attached to window object, it means when i declare variable and give it a name like this `myVar = 2` or like this `window.myVar` is the same.
   
#### how executuon context work ?
* when we call a function is create for it new execution object.
  
* execution context consist of 3 properties.
    * **Vatiable object**, it contain all variable, function and function arguments declrations.
    * Scope Chain.
    * this keyword declration.
* it happen in two phases:
   * **Creation Phase**
   *  **Execution Phase**

  1. **Creation Phase** :
    * Create a variable object.
    * create scope chain.
    * detrimine **this** keyword value.
  2. **Execution Phase** :
    * the script inside the function is run line by line.

* **Variable Object** :
   * when object is created it will create **argument object**, it contain all arguments have been passed to the function.
   * it scan for functions declration and create a property for each function that **point to the function**.
   * it scan for variable declration and create a property for each variable and set it to undefined.

# Hoisting 
   * last 2 steps in variable object ( function and variable scan) commonly known as **hoisting**.
   * it means variables and functions are created before the function start to execute.
   * the reason we get variable undefined because it's set to undefined.
   * the reason I can use function because property has been created that point to the function, which means it refer to it's location in memory.
  
# Scope Chain
  * Scope in js answer the question where the variables can be seen and accessed.
  * the default scope is the **global scope** (the file scope).
  * when function is created, there will be scope created for that function(**local scope**)
  * the lexical scope is the parent scope of the child function, e.g. let's say I have function declared inside function declared inside global scope.
    * the child function can see the parent declrations up to the default scope.
    * the parent scope can't see the child scope declrations.
  * **Important note** in other programming languages when a for loop or if statement declared it will have it's own scope. **This is not in javaScript**.
  * **Important Note** because of lexical scope child function can see parent variable declration **because it's declared inside of that parent**, it means on execution if i call a function not part of lexical scope can't see the variables inside the parent scope.
  
# This Keyword
  * object context like I mentioned earlier consist of 2 phases: creation and execution.
  * The this keyword assigned a value on call so it's attached to the execution phase.
  * on **regular function** call **this keyword** refer to the **windows object** or the **default object.**
    * example : ``` console.log(this)```  will return object window. 
  * on **methods inside object**, it refer to the **object itself**. ``` var yazan = {
         name: 'yazan',
         age: 29}
         myMethod : function(){
            console.log(this)
         } ``` will output the object yazan
   * **note** if i create an object and declare a normal function inside of it, and console this, it will return the windows object.
   * 
# Debugger Object
  * Debugging is about deduction: eliminating potential causes of an error.
  