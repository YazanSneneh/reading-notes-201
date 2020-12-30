# Lists
  * we can create 3 types of lists in html.
  * You can put a second list inside an `<li>` element to create a sublist or nested list.

#### Ordered lists
  * Lists where each item in the list is numbered.
  * Use it to create set of steps in order.
  * type attribute used to change type of list from number to another type like characters or roman numbers etc...
  * To create this type of lists use `<ol> </ol>` and items goes in between.
  * `<li></li>` indicate an item in the list.
  * Example :
    ``` <ol>
     <li> step 1 </li>
     <li> step 2 </li>
     <li> step3 3</li>
    </ol> ```
 
#### Unordered lists
  * Lists that begin with a bullet point.
  * type attribute change list type from bullet to something else like sequare or circle etc...
  * `<ul> </ul>` indicate order list.
  * `<li></li>` indicate an item in the list.
  * Example :
    ``` <ol>
     <li> item 1 </li>
     <li> item 2 </li>
     <li> item 3</li>
    </ol> ```

#### Definition lists 
  * Let of terms along with the definitions for each of those terms.
  * `<dl></dl>` use it to create definition list.
  * `<dt> </dt>` to create term.
  * `<dd> </dd>` used to create definition for term.
  * Example :
    ``` <dl>
     <dt> term 1 </dt>
     <dd> difintion for term 1 </dd>
     <dt> term 2</dt>
     <dd>definition for term 2</dd>
    </ol> ```

# Boxes
 * every html element lives inside a box.
 * these boxes have properties determine the total width and height of the box on the page.
 * these properties are:
   * height : take the content height if it's not determine.
     * css rule : `height : 200px` 
   * width : it depend on content if width rule not determined.
     * css rule `width: 200px`; 
   * padding : is the white space between box and content, and to determine where to space:
     * padding-top : white space from above.
     * padding-bottm: white space from below.
     * padding-right: white space from right.
     * padding-left: white space from left.
     * padding: i use it to combine paddings e.g. `padding: top right bottom left` or i can write pair value to give top + bottom and left + right `padding : x y`
   * margin: the white space between element and it's siblings, everything applied to padding applied to margin.
   * border : every element has border by default and it's a framework surround element, everything applied to padding also applied to border.
      * i can specify color and style of border.
      * example `border: 2px solid yellow` 
 * to determine the width and the high of the box:
   * Total width = margin-y (y is margin on right and left) + padding-y + width + border-y.
   * Total height = margix-x (x is margin top and bottom) + padding-x + border-x + width.
 * sometimes the size of the content define the high and width of the box.
 
#### Min-width, Max-width, min-height max-height
   * i use min-width to specify the minimum width should the box take when user change screen size, also screen users size differ.
   * max-width the same as the min but the opposite.
   * min-height also the same as the min-width.
   * max-width the same as the min-width as well.

#### overflow
  * sometimes box become smaller than content.
  * overflow rule allow me to specify how the content will behave inside the box.
  * values are:
    * hidden: it hide the content exceeded box size.
    * scroll : add scroll bar to the box so i can view entire content inside box.

####  switch statement.
    * it's conditional statement, i provide it several conditions.
    * if statement might be complex, switch make it easier to interact with.
    * it take one expression.
    * check expression with conditions provided.
    * syntax:
       ``` 
       switch(expression){
            case condition:
               script;
               break; // to break out of statement
            default: // i provide it default case, it's basically the else in if
                script
       } 
       ```

### COERCION
   * when type math operation javascript expect 2 numbers.
   * javascript will dynamically convert non expected number to number.
     * example string will be converted to number, `'5'*5 = 25`
     * another example : `' 5 ' / 5 = 1`
     * example 3 : `'text' / 5 = NaN`
     * example 4 : `5 + 5 = 55`.
   * the example 4 result happen because + sign contactinate strings and automatically convert any value to string.
#### truthy and fasly values
  * because of COERCION every datatype can be treated as true or false.
  * falsy values treated as false while truthy values treated as true.
  * falsy values are : 0, '', false, NaN, variable with no value, undefined.
  * truthy values are :number not 0, not empty string, var with value.