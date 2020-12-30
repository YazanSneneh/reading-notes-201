# HTML Links 
   * Links allow elements to navigate user from webpage to another or navigate between section in the same webpage.
   * to create links use a tags, for example `<a href='link to the page '>page title</a>`
   * target attribute: allow me to open link in a new tab or new window and it take many values, for example the _target value `<a href='link' target='_blank'> </a>`
#### Email Links :
   * mailto : allow me to send emails via `<a>` tag.
   * usage : ` <a href='mailto:email@gmail.com'> Email me <a> `;

## Summary LINKS :
- Links are created using the <a> element.
- The <a> element uses the href attribute to indicate the page you are linking to.
- If you are linking to a page within your own site, it is best to use relative links rather than qualified URLs.
- You can create links to open email programs with an email address in the "to" field.
- You can use the id attribute to target elements within a page that can be linked to.

# LAYOUT CSS
In this chapter we are going to look at how to control where each element sits
on a page and how to create attractive page layouts.
### Blocks level element vs *i*n-line level element
CSS treats each HTML element as if it is in its
own box. This box will either be a block-level
box or an inline box.
   * block level elements take full width, that means they don't allow any box to stack before and after it on the same page e.g. h tags, header tag ...
   * inline level element : take the content width and height of elements and don't accept height, width, margin or padding attributes and inline elements stack next to each others e.g. image, a tags.

### Positioning :
- static - it's the default position of elements on page.
- relative - position the element relatively to it's original position.
- absolute - position element related to closest parent has relative position.
- fixed : position element fixed on the page.
- z-index - each element has z-index by default.
- float : float element to right or left.
- clear : i use it after float, to clear the mess float created.
### Creating Multi-Column Layouts with Floats :
- width
- float
- margin

### Layout Grids :
Composition in any visual art (such as design, painting, or photography) is the placement or arrangement of visual elements — how they are
organized on a page. Many designers use a grid structure to help them position items on a page, and the same is true for web designers.
### CSS Frameworks :
CSS frameworks aim to make your life easier by providing the code for common tasks, such as creating layout grids, styling forms, creating.
### Multiple Style Sheets :
- @import
- link
### Summary LAYOUT
1- `<div>` elements are often used as containing elements.
to group together sections of a page.
2- Browsers display pages in normal flow unless you specify relative, absolute, or fixed positioning.
3- The float property moves content to the left or right
of the page and can be used to create multi-column layouts. (Floated items require a defined width.)
4- Pages can be fixed width or liquid (stretchy) layouts.
5- Designers keep pages within 960-1000 pixels wide,  and indicate what the site is about within the top 600 pixels (to demonstrate its relevance without scrolling).
6- Grids help create professional and flexible designs.
7- CSS Frameworks provide rules for common tasks.
8- You can include multiple CSS files in one page.

# FUNCTIONS & OBJECTS & METHODS
#### WHAT IS A FUNCTION?
Functions let you group a series of statements together to perform a
specific task. If different parts of a script repeat the same task, you can
reuse the function (rather than repeating    the same set of st atements).
#### How To Declare a functions:
To create a function you give it a name and then write the statement needed to achieve its task
inside the curly braces this is known as function declaration.
### CALLING A FUNCTION
Having declared the function,you can then execute all of the statements between
its curly braces with just one line of code. This is known as calling the function.
### DECLARING FUNCTION
S THAT NEED INFORMATION Sometimes function needs specific information to perform its task.
In such cases, when you declare the function you give it parameters. Inside the function, the parameters act like variables.
### CALLING FUNCTIONS THAT NEED INFORMATION When you call a function that has parameters,
you specify the values it should use in the parentheses that follow its name.
The values are called arguments, and they can be provided as values or as variables.
### GETTING A SINGLE VALUE OUT OF A FUNCTION Some functions return information to the code that called them.
For example, when they perform a calculation, they return the result.
### GETTING MULTIPLE VALUES OUT OF A FUNCTION Functions can return more than one value using an array.
For example, this function calculates the area and volume of a box.
#### ANONYMOUS FUNCTIONS & FUNCTION EXPRESSIONS :
Expressions produce a value. They can be used where values are expected.
If a function is placed where a browser expects to see an expression,
(e.g., as an argument to a function), then it gets treated as an expression.
### IMMEDIATELY INVOKED FUNCTION EXPRESSIONS :
This way of writing a function is used in several different situations.
Often functions are used to ensure that the variable names do not conflict
with each other (especially if the page uses more than one script).
### VARIABLE SCOPE :
The location where you declare a variable will affect where it can be used
within your code. If you declare it within a function, it can only be used
within that function. This is known as the variable's scope.
### HOW MEMORY & VARIABLES WORK :
Global variables use more memory. The browser has to remember them
for as long as the web page using them is loaded. Local variables are only
remembered during the period of time that a function is being executed.
 
# Pair Programming
## Reasons for Pair Programming :
1. Greater efficiency
2. Engaged collaboration
3. Learning from fellow students
4. Social skills
5. Job interview readiness
6. Work environment readiness
### How does pair programming work?
While there are many different styles, pair programming commonly involves two roles: the Driver and the Navigator.
### Why pair program?
   * Pair programming touches on all four skills: developers explain out loud what the code should do, listen to others’ guidance, read code that others have written, and write code themselves.
   * Many companies that utilize pair programing expect to train fresh hires from CS-degree programs on how they operate to actually deliver a product.
   * Code Fellows graduates who are already familiar with how pairing works can hit the ground running at a new job, with one less hurdle to overcome.
