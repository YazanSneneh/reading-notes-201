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


#### Liskov subsition principle
  * Let q(x) be a property provable about objects of x of type T. Then q(y) should be provable for objects y of type S where S is a subtype of T. [Resource](https://www.digitalocean.com/community/conceptual_articles/s-o-l-i-d-the-first-five-principles-of-object-oriented-design)
  * This means that every subclass or derived class should be substitutable for their base or parent class. [Resource](https://www.digitalocean.com/community/conceptual_articles/s-o-l-i-d-the-first-five-principles-of-object-oriented-design)

#### Interface Segregation Principle
A client should never be forced to implement an interface that it doesn’t use, or clients shouldn’t be forced to depend on methods they do not use. [Resource](https://www.digitalocean.com/community/conceptual_articles/s-o-l-i-d-the-first-five-principles-of-object-oriented-design)

* when i create the interface and create a class implementation for it.
* and some of my inherited class will be forced to use it since they implement that interface.
* this voilate the interface segreation principle.
* to solve this create another interface that implement methods fit it's functionality.
* now the user won't use the old interface thus will not use it's method.

#### Dependency inversion principle 
Entities must depend on abstractions, not on concretions. It states that the high-level module must not depend on the low-level module, but they should depend on abstractions. [Resource](https://www.digitalocean.com/community/conceptual_articles/s-o-l-i-d-the-first-five-principles-of-object-oriented-design)
 
 * like principle said it should depend on abstraction not concretions.
 * to do that, i would create an interface class and force low level class to implement it.
 * a good example in this [resource](https://dzone.com/articles/the-solid-principles-in-real-life) say that it's like credit card, I go to mall and give the cashair my card, me and him know nothing about the card but he swip it and get things done.