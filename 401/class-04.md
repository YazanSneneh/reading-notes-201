# Read: 04 - OOP

## Lesson: Object-Oriented Programming Concepts
 * object oriented programming and the real world.
### what is Object
* objects are everywhere in real world example, from tinest **thing** to the largest thing I could possibly imagine.
  * for example: ad door is an object that has weight, height, width, color and it can open or close.
* in software development objects are created inside class.
* all objects has state and methods:
  * in prevous example weight, height, width are states of the object and they contain the state(value) of each object assoiciated value.
  * methods in the door object: what i can do with door is i either can open it or close it so it's more like a behvaiour so it's in method classification.
  * These methods can work in state as well, so we can't work with state directly that's why we use methods because state initated in class and each object define its state when created.
* This approach to hide state and work with it throught method is known as data encapsulation.
*  This way the object is decided how the outside world should deal with it.

##### benefits of objects.
* Modularity: by creating a bluePrint I seperate the code from the source code, so I can easily create as many objects as I want from the bluePrint.
* Information-hiding: When the data is hidden, it can't be accessed from outside, and I need methods to work with it.
* debugging : If the object bluePrint I created is causing problems, i can easily edit or replace it.

### What Is a Class?
* Class is a blue print for the object.
* in real world I might have many doors types with different color, size, height and so on.
* so the class is a design for the object door i was talking about.
* an example:
   1. the primitives are the state(that's how it's called when they are memebers of the class).
   2. the next 4 methods i created 3 of them to deal with and modify the state because nobody should deal with the class without them.
   
```
public class Door {
    double height = 0.0;
    double weight = 0.0;
    double width = 0.0;

    void changeHeight(int newValue) {
         height = newHeight;
    }

    void changeWidth(int newValue) {
         width = newWidth;
    }

    void changeWeight(int increment) {
         weight = newWeight ;   
    }

    void open(int decrement) {
         System.out.print("Open!");
    }

      void close(int decrement) {
         System.out.print("Close!");
    }
}

```

## Binary, Decimal and Hexadecimal Numbers

### Decimals
 * I can identify the decimal numbers when i either see, dot they are to the left of the dot, example : `21.0`
   * lets say i have 2 numbers after dot to the left, each number exist in position.
   * as i move to left the position increase 10 times to prevous one, example : 1 position is 10, the 2 position is 100, if there is 3rd number the position is 1000.
* Bases : the decimal system based on numbers from 0 to 9 (count with ur hands and you will count all your fingers).
  *  so lets say i count from 0 to 9, but i also want to count 10 in addition, number in index of 10s will start again from 0 and the index of 100's will increase one and as i increase and run out of symbols i will add 1 more to the left index and reset the current one to be 0.

#### Counting with Different Number Systems
* other systems are working the same.
* binary, hexadecimal or octal.
* the binary base is 2 wich means i have only 2 symbols : 0 and 1.
* hexa is 16 symbols.
* octal 8 symbols.