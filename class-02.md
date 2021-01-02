# Text
  * tags provide extra meaning and allow browsers to show users the appropriate structure for the page.
  * Structural markup: the elements that you can use to describe both headings and paragraphs.
  * Semantic markup: which provides extra information; such as where emphasis is placed in a sentence.

#### Headings
  * HTML has 6 levels of heading from h1 to h6.
  * the most important heading and the biggest heading is `<h1></h1>` and there is only h1 in the page and it's usually the title of the webpage.
  * these headings arranged from most important to least important, which means the least important heading on the page is `<h6></h6>`.
  
#### Paragraphs
  * paragraphs are consist of 1 sentence or more.
  * To create a paragraph add the content between p tag like so `<p>this is a paragraph</p>`

#### Bold & Italic
  * b tag : `<b> </b>`.
     * Make content between b tag appear **bold**, bold means what's between the b tag looks **dense**.
  * i tag : `<i> </i>`
     * make the content between the `<i> </i> ` tag italized like and looks like swaying *THIS IS AN EXAMPLE OF ITALIZED*.
   
#### Superscript & Subscrip
  * The `<sub>` element is used to contain characters that should be subscript.
  * The `<sup>` element is used to contain characters that should be superscript such as the suffixes of dates or mathematical concepts like raising a number to a power such as 22.

#### Line Breaks & Horizontal Rules
  * `<br/>`
     * if you wanted to add a line break inside the middle of a paragraph you can use the line break tag `<br />` to show it on new line.
  * `<hr/>` 
     * create thin herozintal line and divide content or section on the page.
 
## Semantic Markup
 There are some text elements that are not intended to affect the structure of your web pages but they do add extra information to the pages — they are known as semantic markup.

#### Strong & Emphasis
   * `<Strong>`
     * it give the same strucutre as the `<b>` tag but `<strong>` tell browser this is important text
   * Emphasis : `<em>`
     *  indicates emphasis that subtly changes the meaning of a sentence.
   
#### Quotations : `<blockquote>`
     * The `<blockquote>` - element is used for long quotes.
     * The `<q>` - element is used for short quotes.

#### Abbreviations & Acronyms
     * `<abbr>` - used to add acronym e.g. `<abbr title ='doctor'> Dr </abbr>`.

#### Author Details
     * `<address>` -  use: to contain contact details for the author of the page, like below.
        ```<address> 
            <p><a href="mailto:homer@example.org"> homer@example.org</a></p>
            <p>742 Evergreen Terrace, Springfield.</p>
        </address>```

# Understanding CSS: Thinking Inside the Box
   * The key to understanding how CSS works is to imagine that there is an invisible box around every HTML element.
   * CSS Properties Affect How Elements Are Displayed.
   * there are 3 ways to use css internal, inline and external.

#### BLOCK & INLINE ELEMENTS
      * **Block level elements** - elements take full width of the parent box and high of the content, example of block elements are `<div>, <header>, <h1>, <p>`.
      * **Inline level elements** - elements take the height and with of the content, example of inline elements are `<img>, <a>` tags.

### CSS Selectors
   * there are many ways css allow me to target elements.
   * the list of these elements are : 
      * **universal selector** - apply to all elements on the page - `*{ css rules...}`
      * **type selector** - match element name - `h1{css rules...}`
      * **class selector** - any element match target class - ` .link{css rules...}`
      * **ID Selector ** - match element with ID - `#id{css rules...}`
      * **child** - match child element that directly inside parent - `header > h1 {css rules...}`
      * **descendant** - all elements inside matched element - `main section{css rules...}`
      * **Adjacent Sibling** - match element sibling next to element - `h1+p{css}`
      * **General Sibling** - Matches an element that is a sibling of another, although it does not have to be the directly preceding element - `h1~p {}`

#### Inheritance 
   When we apply some of css properties to the parent, all elements inside that element will inherit the property.

# Basic JavaScript Instructions
   * **Script** : A script is a series of instructions that a computer can follow one-by-one. 
   * Each individual instruction or step is known as a statement.
   * **Comments** You should write comments to explain what your code does.
       * Single line comments ` // this is single line comment`.
       * multi line comment ` /* this is how i write multi line comment*/`.
    * **Variables** - variables are like bags i use them to store data so i can use later, and give it a name so i know where i hide my data.
       * declare variable : `var varName = value;`
       * we call them variables because the values can be changable.
       * **RULES FOR NAMING VARIABLES** - there are 6 rules.
        1. camelCase naming - each first letter in words should be capital `var userName`.
        2. names contain numbers, letters, $ sign and _ but not - .
        3. Keywords should not be used.
        4. variable name should not start with numbers.
        5. variables are case sensetive.
        6. name should start with letter, dollar sign or _.
#### DATA TYPES
   1. NUMERIC DATA TYPE - numbers ` var num = 5  var num = 5.2`
   2. STRING DATA TYPE - text and writtin between single or dbl quotation - `var name ='Yazan'`
   3. BOOLEAN DATA TYPE - bool either `var bool =true` or `var bool = false` values.

##### ARRAYS
  * arrays are special type of data types and used to store list of items so save ourselves the naming.
  * items in array should be related to each others.
  * array helpful when we dont know exactly how many item we gonna need.
  * **Create array**
    * var arrName = [val1, val2, val3] example:
    * `var colors = ['red','green','blue']`
  * each item in array has an index reference to the location of item in memory.
  * index start from 0, for example `'red` index is 0
  * to access the first item in the array : `alert(colors[0])`.
  * to update item on specefic index `colors[0] = 'yellow'`.
  * use the value of item, in example of print blue : `alert(color[2])`

### conditionals and loops
  * the normal flow of the program is to read scripts from top to bottom and left to right to the last statement.
  * conditional statements change the flow of the program.
    * conditionals provide a piece of code might run in the flow or not based on condition.
    * example of conditionals is if statement and switch statements.

####  switch statement.
    * it's conditional statement, i provide it several conditions.
    * if statement might be complex, switch make it easier to interact with.
    * it take one expression.
    * check expression with conditions provided.
    * syntax:
       ``` switch(expression){
            case condition:
               script;
               break; // to break out of statement
            default: // i provide it default case, it's basically the else in if
                script
       } ```
#### loops 
  * loops also effect the normal flow of the program.
  * loops allow piece of code run many times until condition is true.
  * example of loops are **for loop** and **while loop**
  * the different between for loop and while loop is
    * for loops will keep running to the end, for example count from 1 to 10
    * while loop: in while loop we don't know how many times will the program run so it will keep running until the condition is true, for example user password input is incorrect, until user input correct value.
