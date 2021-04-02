# Java Basics
 
 
## Variables
This section discusses this relationship
*  variable naming rules and conventions.
*  basic data types (primitive types, character strings, and arrays), default values, and literals.

### variables kinds in java.
* there are 4 variables kinds in java:
  * Instance fields:
    * it's non-static method (which means declaring without using static keyword).
    * it hold the state of each unique object initiated from the class.
    * declare syntax: **<span style="color:blue;"> int</span> num = 5;**
  * Class variables:
    * these variables belong to the class itself.
    * they are declared using **static keyword**.
    * static variables are unique across the class, meaning that static keyword tell compiler there is only 1 copy of this variable and it's the original copy.
    * conceptually, when i want to declare a static variable meaning all instances share the same state, for example: cars have 4 wheels so i will declare a static variable hold the number of wheel state.
    * decleration syntax: **<span style="color:blue;"> static int</span> wheels = 4;**.
  * Local variables:
    * they are declared inside methods.
    * they are called variables and they hold the temporary state of the method.
    * they live inside curly braces of method (the local scope).
    * since it's locally declared, it's invisble outside of the method, meaning the class can't access it.
    * declare it similar to fields : **<span style="color:blue;"> int</span> num = 5;**.
  * Parameters: 
    * parameters are variables not fields belong to method as well.
    * they are declared inside method parentheses.
### Naming.
* any programming langauge has it's own rules of naming variables.
* in java the following rules are:
   * **variables are case sensetive**.
   * **variables can start with letters, underscore(_) or dollar sign($)**, however naming convention always should start with letters.
   * White space is not permitted.
   * **subsequent can be letters underscore and dollar sign**, however when choose a variable name should be full name like **degree**, **mean** instead of abbreviations **d** and **m**, this will make code more readable and understood and self documented.
   * **variable name can't be keyword or reserved words**.
   * when variable name contain more than one full word, for example **gearRation**, should always be written in **camelCase**, which is **first word begin with small letter** and **next words capital letters**.

## Datatypes
* java is strong typed langauge, that means I can't use variable before they are declared.

* before I talk about variables i will explain a little cool beautiful story happen behind the scene.
  * bit is the smallest measurement unit in memory.
  * a **byte** is equal to **8bits** in the memory.
  * memory divided into bytes and it's called regester(each regester = byte).
  * when i say variable int equal to 4 bytes means it reserve 4 regesters.
  * so when i say variable type allocate 1 byte means it allocate 8 bits, and short allocate 2 byts means 16 bit, int size 32 bits and long 64 bits.
  * to calculate the range of datatype chosen use following forumla ( range: [-2<sup> numberOFBits -1 </sup>, (2 <sub> numberOfBits -1 </sup> ) -1 ]).
  * **Note: to know which datatype to use you should think how to not waste memory, so when i need small number i would go with byte, or if want more i would pick short and i might want to pick long if i need to use very large number.**
  * **again: you only ned to think that you should not waste memeory, because if I alocate long which is 8 bytes it will reserve 64 bits while all i need is short which is 2 bytes and it's 16 bits.**

* Primitive datatypes in Java:
  * byte (1 byte), it take numbers.
  * short (2 bytes), it take numbers.
  * int (4 bytes), it take numbers.
  * long(8 bytes), it take numbers.
  * double( 8 bytes),it take numbers with decimal values.
  * float (4 bytes), it take numbers with decimal values.
    * to use float, i will have to cast, so to cast there are 2 ways to do it in java:
     1. `float num = (cast)5.44;`
     2. `float num = 5.44f;`
  * char (2 bytes).
  * boolean (1 byte).
  * **Note: in addition I can declare a String datatype, it lives between double quotation `"some string here"`**.
      * **String** is a real type, not primitive:
      * use strings in java I can do it two ways:
        1. `String str = new String('this is my string');`.
        2. `String str2= 'this is a string without cosntructor';`.
      * string concatination java:
      * I use (+) operator to combine strings: `String str3 = str + str2;`.


## Expressions, Statements, and Blocks

### Expressions statement
 * construct made up of variables, operators, and method invocations, that evaluates to a single value.
 * for example :
   * `int x = 2+2; ` it will evaluate to 4 which is a single value.
   * example 2 functions:
```
function sum(int[] numbers){
    int result = 0;
    for(int number : numbers){
        resutl +=number;
    }
    return result;
}

int sumResult = sum({1,2,3,4,5}); // whatever happen it will evaluate to single value.
```
  * example 3: operators or logical operators:
    * `boolean result = true || false; // will evaulate to single value.`
    * `boolean result = 3>5;`;

* **Note: Control Flow Statements** for loops and if statement will not evaluate to single statement so it's not expression statement.

### Statements
* statement forms a complete unit of execution. The following types of expressions can be made into a statement by terminating the expression with a semicolon (;).

### Blocks
 a 0 or more statements grouped together, lives between curly braces.
 * for example: **classes are blocks of code**, **Methods are blocks of code**.

## Control Flow Statements
* the normal flow of the program is: from top to bottm, left to right.
  * top to bottm: the interpreter will read code line by line in order from top to bottm.
  * left to right: in each line currently interpreter reading, it will read from left to right.
* **however conditionals can break and control and modify the normal flow of the program, how?**
  * I have conditional statement `if(){ code here..}`, the code will not be executed,
     unless the condition provided is true.
  * if condition is false then program will skip the lines of code. 
* java uses booleans to evaluate conditional statements.
* true or false are the returning result, the code will be executed.
* example:
```
int x= 5;
int y= 5;
 if(x == y){
  System.out.println('they are equal'); 
}
```
* since they are equal the result will evaluate to true, therefore the code will be executed.
if x = 5 and y=6 then the result will be false thus code will not be executed.

###  decision statements
it tell the program what should do if the statement evaluate to true or false.
#### if statements, else and if else
* **if** block, will be executed when condition provided evaluate to true.
* **else** block is executed when program evaluate to false.
```
if(true){
   execute code here....
}else{
   execute code if condition is not true.   
}
```
* else if, when I expect more than one condition to be true but each one execute it's own block, look at example:
```
 int testscore = 76;
        char grade;

        if (testscore >= 90) {
            grade = 'A';
        } else if (testscore >= 80) {
            grade = 'B';
        } else if (testscore >= 70) {
            grade = 'C';
        } else if (testscore >= 60) {
            grade = 'D';
        } else {
            grade = 'F';
        }
        System.out.println("Grade = " + grade);
    }
}
```
* **if - else** statements doesn't have to be in several lines with {}, if can be used in one line, or without the {}, for a single line statment:
1. if else without {}:
```
  if (a == b)
      System.out.println("Another line Wow!");
  else
      System.out.println("Double rainbow!");

```
2. a single line statment:
```
   a ==b? executed code if true(if part) : executed code if false(else part).
```
### loop statements
* loop statement allow me to run piece of code more than once.
* There are 2 types of loops for loops and while loops.

#### for loops:
* i use for loop when i know the end of the loop (or at least i can the program), for example i give user 5 attempts to enter correct password.
* syntax for(int i= 0; i<5; i++){ code statements here....}; 
    1. first part: is the loop start and current iterate number, and it will always compiler read it first.
    2. second part: as long as the comprasion operator evaluate to true the code inside braces will run, and it get's executed 2nd.
    3. third part: when the current round is finished this block get executed.

* **important note about for loop:** first part and second part will be executed before the loop start,
   and third part will be executed after the round finished.

#### forEach:
  * it's a shorthand version of for loop.
  * it's used when i want to iterate over array.
  * for (int element : arrName){ execute code on element};
  * example :
 ```
  int[] nums = {1,2,3,4,5};
   
   for (int num : nums){
     System.out.println(num);
  };
 ```
#### While loop and do white:
  * I use it when I don't know how many times i need to iterate, for example a user want to enter password.
  * syntax  `while(condition) {code ....};`
  * as long as the condition evaluate to true, the while loop keep running.
  

2.1 do while:
  * It's the while loop but do while exist because i might want to execute code inside at least once.
  * syntax:  `do { code ...} while(condition);`


### Branching Statements
#### break
* break is used when i want to break the iteration statement before it's finished based on a condition.
* so basically let's say my for loop will iterate 50 times, and i tell it to exit loop if it exceed 20 times.
* example:
```
  for(int i=0; i<5; i++){ 
    if(i>2){
      break;   // loop when i = 0, 1,2
   };
 };
  ```
#### continue:
* i use it when i want to skip executing code based on condition, for example i want for loop to keep iterating to the end, but on 5th iteration it should not execute.
* example:
```
   for(int i=0; i<5; i++){ 
     if(i>2){
       continue; // skip executing when i > 2
   };
 };
 ```

 # Reddit thread on compiling
 * computer language is 0,1 which means 0 there is no electrical signal while 1 there is elictrical signal.
 * so the computer only understand 0 and 1.
 * in order for us humans to instruct computer to do something we should communicate with it.
 * now high level langauges such as java, c++ or even c# and humanic langauges that allow us to write instructions to computer.
 * these instuctions grouped together called a program that live inside a file.
 * when I write a java code, the source code will be saved in **.java** extention.
 * when i click on run the compiler will read the extention and understand there is java program live inside so it will be treated as java program.
 * the compiler will check for syntax error and if code is clean from syntax errors, then it will generate abstract tree.
 * now the computer still can't understand the java code since it's language is 0 and 1.
 * so the generated abstract tree will be passed down to program called **assembly** which is considered **low level langauge** (assembly is translator who can understand both the abstract tree generated file and the 0, 1 langauge).
 * it will communicate with generated code and generate 0, 1 code and deliver it to **computer cpu**.
 * now the **0 and 1 origin sory**, there are things called **transistors** inside the computer stacked next to each others, they looks like wires contain **keys** and when there is signal(1 in computer langauge) a key of responsible transistor will close and allow electrical signal to pass.
 * if there is no signal(0) key will open and will not allow singal to pass. 
 * the computer will read instructions and generate **.exe** file which is executable code.
* and write the output on screen ^_^.
# Reading Java Documentation
* this is basically a tutorial about how to deal with java documentation.
* first things first, why do i have to do it in the first place?
  * documentation provide everything with details and it's the source of everything.
* java on it's own contain more than 5k libraries so if I want to search for a method i will have to learn how to navigate, read and understand the documentation.
* so to do so, navigate to index link from navigation bar.
* on **top of page there will be letters**, **choose letter** **match the first letter of your searching term** e.g. you want to find **println** method then pick **p**.
*  **Ctrl+f** will popup a search bar.
*  type your search term.
*  list will be viewed where that term exist and in which library in java.
*  choose matching characterstics for your term and click on link in the sentence.
*  you will be navigated to a page expalin everything about it.
*  **congrates.**