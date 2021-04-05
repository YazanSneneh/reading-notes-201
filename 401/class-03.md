# Maps, primitives, File I/O

## Primitives vs. Objects
pros and cons of using Java primitive types and their wrapped counterparts.

#### Java Type System
* java allow us to declare primitives in 2 ways.
  * the normal way.
  * declaring it using wrappers.
* objects contain a value of each primitive element.
* Java wrappers are objects store primitive inside of it.
* The process of converting a primitive type to a reference one is called autoboxing, the opposite process is called unboxing.

#### Single Item Memory Footprint
* primitives allocate this much of memory when i declare each type:
  * boolean – 1 bit 
  * byte – 8 bits 
  * short, char – 16 bits
  * int, float – 32 bits
  * long, double – 64 bits
* Primitaves using wrapper:
  * It turns out that a single instance of a reference type on this JVM occupies 128 bits except for Long and Double which occupy 192 bits:
    * Boolean – 128 bits 
    * Byte – 128 bits
    * Short, Character – 128 bits
    * Integer, Float – 128 bits
    * Long, Double – 192 bits.
  * single variable of Boolean type occupies as much space as 128 primitive ones, while one Integer variable occupies as much space as four int ones.

#### memory and Performance
* arrays of the primitive types long and double consume more memory than their wrapper classes Long and Double.
* Variables of these types live in the stack and hence are accessed fast in memory model.
* The reference types are objects, they live on something called heap in memory model and are relatively slow to access.
* this will consume huge memory thus will make proccess slower.

#### Default Values
* as for primitives, each type will contain default value when it's declared. e.g. int is 0, bool is 0 etc..
* as for wrappers variables they are initialized to null.

#### Usage
* because primitives are much faster we should use them always, but there are cases i will need to use wrappers.

# Scanner
* format inputs and translate them to tokens, then translate token accoding to it's type.
* I use object scanner to take input from user.
* to use it first i have to include it.
  * `import java.utl.Scanner;`
  * `Scanner scan = new Scanner();`
* Scanner support all datatypes expect for `char, bigIntger, BigDecimal`.

# Exceptions
* exceptions are events, java use it when we run program and it disturp the flow of the program 
* java use exceptions to handle errors and exceptional events.
* When an error occurs within a method, the method creates an object and hands it off to the runtime system. 
* when i run a program and it throw error, the runtime search for object handler to handle error, when it find it, it invoke an object which is the exception handler, then give it the information of error and it's type
#### try and catch
* program can catch exceptions by using a combination of the try, catch, and finally blocks
* The try statement should contain at least one catch block or a finally block and may have multiple catch blocks
    * try block is where i write code, and where might error occur.
    * when error catched by the handler i added. it will stop the program execution and implement the catch block.
    * the catch block contain code and it receive a variable as parameter, this paramter contain information about the error itself.
### The Three Kinds of Exceptions
* checked exception: when user try to open file that does not exist it will throw me error : 
  * `java.io.FileNotFoundException`.
* second kind of exception is the error.
  *  The unsuccessful read will throw `java.io.IOError`.
* runtime exception: application usually cannot catch them, indicate programming bugs, such as logic errors or improper use of an API.
    * If a logic error causes a null to be passed to the constructor, the constructor will throw `NullPointerException`

#### Advantages of Exceptions
1. Separating Error-Handling Code from "Regular" Code.
2. Propagating Errors Up the Call Stack
3. Grouping and Differentiating Error Types.