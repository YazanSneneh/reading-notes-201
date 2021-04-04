# Read: 02 - Arrays, Loops, Imports

## Packages and Import
 * package is collection of classes grouped together.
 * the package name should be the same as the parent directory.

#### Package declaration
 * package decleration is on top of the file before any thing and it's optional.
 * below it i can import stuff and thse statements allow me to use classes from other packages.

#### Package declaration syntax
 * to declare a package first i type `package packageName;`.
 * Imports comes after package decleration.
 * then i can define class to work on.

#### Imports
* i have 3 ways to import classes.
  * USING WILD CARD.
    * `import java.swing.*; ` this line of code uses wild card star which means import everything, but hey i can only use 1 class.
  *  using class name.
     *  i import it similar to wild card but with name `import java.Math;`.
  *  declare and use it inside code.
     *  `javax.swing.SomeMethod();`.

#### Common imports
 most imported packages are: 
 * `import java.awt.*;`  Common GUI elements.
 * `import java.awt.event.*;`	The most common GUI event listeners.
 * `import javax.swing.*;`	More common GUI elements. Note "javax".
 * `import java.util.*;` Data structures (Collections), time, Scanner, etc classes.
 * `import java.io.*;`	Input-output classes.

## Loops
* loop statement can interpret and altr the normal flow of the program.
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

## Arrays
* Arrays are variables container, that means it contain more than 1 variable.
* it contains as many variables as i store in it.
* java start assigning indexes from 0, meaning when i have array of size 5 data will be stored at indexes from 0 to 4 (count them it's 5).
* to refer to a variable or target a variable i have to use indexes.

* to declare an array I should use following: 
  * int[] arr;
* to make an array with specific length: 
  * int[] arr = new int[5];
* to get the length of array i use property
  *  arr.length;
* **shortcut**, i can create array and assign values to indexes at the same line.
     int[] arr = {1,2,3,4,5,6};

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