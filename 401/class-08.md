# OOD Object Oriented Design

 ## The First 5 Principles of Object Oriented Design
* principles that take into consideration when i am designing my project is to be maintained and can grow in the future without problems or code debugging and very important for agile software development.
* the 5 principles:
  * single responsibility Principle.
  * open closed principle.
  * Liskov. substituion principle.
  * interface segeration principle.
  * dependency inversion principle.


#### single responsibility principle
  * Each class should do only one job. [Resource](https://www.digitalocean.com/community/conceptual_articles/s-o-l-i-d-the-first-five-principles-of-object-oriented-design)
      * For example lets say I want a class to calculate the area of a shape.
      * if the class calculate and output result as multi form e.g. html or json it would be violation for the **SRP**.
      * to solve this, i will first calculate the shape and create a class that handle outputing whatever recieve, the way the user want it.

#### open closed principle
   * Objects  should be open for extension but closed for modification. [Resource](https://www.digitalocean.com/community/conceptual_articles/s-o-l-i-d-the-first-five-principles-of-object-oriented-design)
   * meaning the class should be extendable but should not be modified.
   * **and example**: let's say the area calculator that accept any shape and calculateit's area, if I want to think how to do it, I will create if else statement for each shape. but what if I want to add new shape ?
     * Here I **voilate** the open closed principle.
     *  so to **solve** this I will **create** class for each **shape** and claculate the area in each class.
     * now the code can be **expanded** **without modification**.
     *  when i want to add a new shape I will create a class for that shape.