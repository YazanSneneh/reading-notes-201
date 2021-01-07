# Errors handling and devbugging 
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
#### execution context
   * the execution context is a box where the code executed.
   * **default execution context** is the global execution context, code not inside function.
   * default execution context is for code and functions that not inside any functions.
   * default execution context is associated with the window object, which is why when we create anything gets attached to window object, it means when i declare variable and give it a name like this `myVar = 2` or like this `window.myVar` is the same.
   * when we call a function is create for it new execution function.
   
[watch this awesome video for clear picture](media/4.%20Execution%20Contexts%20and%20the%20Execution%20Stack.mp4)

