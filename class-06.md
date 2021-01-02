# Object Literals
  * lets say i have hospital and i have n number of employees working there.
  * and each employee has name, job title, salarly, department.
  * if i want to represt that programmatically,i would create variable for each one of these, and I have n numbers of employees, so i am going to heavily repeat each value n number of times.
  * it's like banging my head on wall.

### how to solve this problem ?
  * there is a concept in programming called object.
  * object literals is complex datatype in javascript.
  * object consist of attributes.
  * attributes come in key=value pair.
  * attributes can be primitve (numbers, strings,boolean) datatype, arrays or functions datatype.

### Why objects are useful ?
  * objects are effective because it help me create less repititve code.
  * it group related data in accessable way.

### how to define objects ?
  * ``` var objName = {
       key: value,
       key2:val2,
       functionKey: function(){
         code ....       
       }
   } ```
      
   * example: ``` var employeeAhmad = {
         name: 'ahmad',
         jobTitle: doctor
         salary : 800, 
         department: 'ICU'
   } ```

## how to access attributes and modify it ?
    * access attributes
      * objectName.attributeName
         * example : employeeAhmad.name;
    * modify attributes.
      * objectName.attributeName = 'new value';
         * example : employeeAhmad.name = 'Afaf';

# The Document Object Model (DOM):
   * Specifies how browsers should create a model of an HTML page.
   * How JavaScript can access and update the objects of the page while it is in the browser window.
   * The DOM is neither part of HTML, nor part of JavaScript; it is a separate set of rules. It covers two primary areas:
      * **Create the HTML page object tree**:
         *  When the browser loads a web page, it creates a model of the page in memory.
         * The DOM specifies the way in which the browser should structure this model using a** DOM tree**.
      * How to access and modify objects : 
        * defines methods and properties to access and update each object in this model.
        * Application Programming Interface (API). User interfaces let humans interact with programs.
#### THE DOM TREE IS A MODEL OF A WEB PAGE
   As I mentioned earlier, The DOM structure model of objects, it consist of elements of the webpage and store it in the memory, it's called the DOM tree.
   Example of DOM TREE : ![Structured Dom tree](https://www.w3schools.com/js/pic_htmltree.gif)
   * it consist of four parts:
      * THE DOCUMENT NODE
