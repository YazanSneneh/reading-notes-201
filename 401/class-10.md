# Read: Stacks & Queues

## Stack

* Stack is a data structure type where each node point to the next node.
* Stack has 2 concepts explain everything about them.
  * **FILO** stands for first in to the stack should be the last element out of stack.
  * **LIFO** which means last element in stack should be first element out.
* All methods take  Big O(1) because I only deal with the element on top of the stack.
*  `top` is the top of the stack which is the last element has been added.
* Methods can be implemented on Stack:
  * `pop()` remove element from top of the stack.
    * when stack is empty it throw error.
    * Big O(1)
  * `push()` add element on top of the stack.
    * Big O(1)
  * `peak()` allow me to see the last element added to the stack.
    * Big O(1)
  * `isEmpty()` check if stack is empty and return true if it's empty otherwise return fasle.
    * Big O(1)

* Explination: 
  * When I push new item to stack it become the on top of the stack and the new item next value will point to the prevous top and current top will become the new top.
  ![Stack](https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Code_401/class-10/resources/images/stack1.PNG).

  [resource from Codefellows](https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Code_401/class-10/resources/stacks_and_queues.html)

## Queue
* Termonolgies of Queue:
* front is the first node in the queue.
* rear is the last element in the queue.
* Queue has 2 concepts explain what are they.
  * **FiFo** which is the first element added to the queue should be the first element to out **unlike stack**.
  * **LILO** which is the last element added to the queue should be the last element to out, that'ws why called queue.
* `enqueue()` when i add an element to the queue.
  * Big O(1)
* `dequeue()` when element is removed from the queue.
  * Big O(1)
  * it throw an error when queue is empty.
* `peak()` view the value of the node in the front.
  * it throw an expection as well.
* `isEmpty()` work similar to the stack empty return true or false.
  * Big O(1)

* explination:
 ![Queue resource from Codefellows](https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Code_401/class-10/resources/images/Queue.PNG)

 [Queue resource from Codefellows](https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Code_401/class-10/resources/stacks_and_queues.html)