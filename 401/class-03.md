# Maps, primitives, File I/O
## Primitives vs. Objects

* in java I can create object corresponding to each primitve datatype.
* for example `int, char double` are primitives but i can declare them as objects using `Integer, Double Character`
* The wrapper class allow me to create these corresponding objects.
* I need them because sometimes.
* To consider working with objects I have 2 things to put in mind:
  * The amount of memory size i have to work with.
  * The application performance I am trying to achieve.
* Primitives impact on memory.

   |Type|Primitive|
   | ---|---------|
   |int| 16 bit | 
   |char| 8 bit | 
   |short| 16 bit | 
   |long| 32 bit | 
   |double|32 bit | 
   |float| 16 bit | 
   |boolean| 16 bit |
   [No reference i built it myself]()

#### memory and Performance
* Variables of these types live in the stack therefore they are accessed fast in memory.
* The reference types are objects, they live on something called heap in memory and it's reference variable in stack and are relatively slow to access.
* this will consume huge memory thus will make proccess slower.

#### Default Values primitive vs Wrapper Class
* all wrapper objects default is `null` value.
* as for primitives, each type will contain default value when it's declared. e.g. `int = 0,char \u0000` etc..
* as for wrappers variables they are initialized to `null`.

#### Usage
* because primitives are much faster we should use them always, but there are cases i will need to use wrappers.
* Java langauge does not allow using primitves on collections. 

# Exceptions
* Java use **expections** to handle errors.
* Exceptions in java are events occur during the execution of a program and interrupt the execution and crash the application.
* **throwing exception** is when a method run and error happen, it will create an object (called exception object) contain information about the event and then send it to the runtime system.
* Example from [java documentaion](https://docs.oracle.com/javase/tutorial/essential/exceptions/definition.html):  ![Exampe](https://docs.oracle.com/javase/tutorial/figures/essential/exceptions-callstack.gif).
* The **runtime search** for method handler to handle error, when it find it, it invoke a method which is the exception handler, then give it the information of error.
* **exception handler** method handler a block of code handle the exception ( catch the exception).
* [Java documentation on handling error](https://docs.oracle.com/javase/tutorial/essential/exceptions/definition.html) ![Java documentaion](https://docs.oracle.com/javase/tutorial/figures/essential/exceptions-errorOccurs.gif).

#### try and catch
* a code that throw exception should be in try and catch statement.
* the code should be in the `try` block and it catch the error and deliver it to exception.
* the `catch` block receive an object from `Exception` class will tell the runtime system what to do with the error.
* if catch fail to deal with the error it will throw error thus app crash.
* `catch(Class object){}` in params section i either specifiy object from specific class like `NullPointerException` or i use `(Execption excep)` which is the general class
* the `Final` block contain a statement should be executed wherether the error occurs or not.

###  Kinds of Exceptions
* checked exception: when user try to open file that does not exist it will throw me error: 
  * `java.io.FileNotFoundException`.
* second kind of exception is the error.
  *  The unsuccessful read will throw `java.io.IOError`.
* runtime exception: application usually cannot catch them, indicate programming bugs, such as logic errors or improper use of an API.
    * If a logic error causes a null to be passed to the constructor, the constructor will throw `NullPointerException`.
    * `try{}catch(){}final{}` [Check Java Documentation to see how they work as explain above](https://docs.oracle.com/javase/tutorial/essential/exceptions/handling.html)

#### Advantages of Exceptions
1. Separating Error-Handling Code from "Regular" Code.
2. Propagating Errors Up the Call Stack.
3. Grouping and Differentiating Error Types.
[Java Documentation](https://docs.oracle.com/javase/tutorial/essential/exceptions/handling.html).

# Scanner
* format inputs and translate them to tokens, then translate token according to it's type.
* I use object scanner to take input from user.
* to use it first i have to include it.
  * `import java.utl.Scanner;`
  * `Scanner scan = new Scanner();`
* Scanner support all datatypes expect for `char, bigIntger, BigDecimal`.