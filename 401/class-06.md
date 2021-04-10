# OOP 
A programming paradigm, the oop concept consider everything in life as object that contain properties and, so i can create a blueprint for objects that share same properties and behaviour.
### what is Object?
* objects are everywhere in real world example, from tinest **thing** to the largest thing I could possibly imagine.
  * for example: ad door is an object that has weight, height, width, color and it can open or close.
* in software development objects are created inside class.
* all objects has state and methods:
  * in prevous example weight, height, width are states of the object and they contain the state(value) of each object assoiciated value.
  * methods in the door object: what i can do with door is i either can open it or close it so it's more like a behvaiour so it's in method classification.
  * These methods can work in state as well, so we can't work with state directly that's why we use methods because state initated in class and each object define its state when created.
* This approach to hide state and work with it throught method is known as data encapsulation.
* This way the object is decided how the outside world should deal with it.

##### benefits of objects.
* Modularity: by creating a bluePrint I seperate the code from the source code, so I can easily create as many objects as I want from the bluePrint.
* Information-hiding: When the data is hidden, it can't be accessed from outside, and I need methods to work with it.
* debugging : If the object bluePrint I created is causing problems, i can easily edit or replace it.

Reference from my reads [Objects](class-04.md)

### What Is a Class?
* Class is a blue print for the object.
* in real world I might have many doors types with different color, size, height and so on.
* so the class is a design for the object door i was talking about.
* an example:
   1. the primitives are the state(that's how it's called when they are memebers of the class).
   2. the next 4 methods i created 3 of them to deal with and modify the state because nobody should deal with the class without them.

Reference from my reads [Classes](class-04.md)
   
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

## What Is Inheritance?
* let's say that the doors I mentioned all share height, width and weight, but some types of doors require advanced technologies to open or close, others require finger print.
* So inheritance allow me to create a new blueprint for our new born door object but instead of define height width and weight I can inherit these properties from Door class and have a new class to create for me door open with finger print.
* In OOP I can have a parent class and as many children classes as i need.
* the **parent** class also **called** the **super class**.
* syntax to inherit from super class: `public class FingerPrintDoor extends Door{}` .

## What Is an Interface?
* objects have methods that allow me to communicate with them.
* for example: In order to work or communicate with T.V I should use buttons, in that sense buttons are methods and the board is the Interface that allow me to talk to the t.v.
* interface is class that contain group of methods.
* it contains methods with empty body.
* To create an interface class use following syntax:

```
public interface myInterface{

    //  wheel revolutions per minute
    void turnTvOnOff(int newValue);

    void IncreaseVoice(int increment);

    void ChangeChannel(int newValue);

    void decreaseVoice(int decrement);
}

```

#### implement interface.
* to implement interface i need a class.
* that class **should contain** keyword **implements**.
* that class I can have anything I want, but there is a catch.
* The catch is I **must** implement all methods in the **interface class** or i will get error.
* Syntax:

```
public class App implements {
   void turnTvOnOff(int newValue){
       return 0;
   }

    void IncreaseVoice(int increment){
       return 0;
   }

    void ChangeChannel(int newValue){
       return 0;
   }
    void decreaseVoice(int decrement){
       return 0;
   }

}
```

## What Is a Package?
* package is group of classes logically do common work.
* I should think of packages like I am grouping my classes for organizing them.
* **Why I need packages?** java is OOP language which means everything should be class, I might use hundreds of class so it's wise to **package** them.


##### Questions and Exercises: Object-Oriented Programming Concepts
* Real-world objects contain _properties_ and _methods_.
* A software object's state is stored in _class_.
* A software object's behavior is exposed through _methods_.
* Hiding internal data from the outside world, and accessing it only.
* through publicly exposed methods is known as data _encapsolation_.
* A blueprint for a software object is called a _class_.
* Common behavior can be defined in a _Parent class_ and inherited into a _child class_ using the _extends_ keyword.
* A collection of methods with no implementation is called an _interface_.
* A namespace that organizes classes and interfaces by functionality is called a _package_.
* The term API stands for _Application programming Interface_?