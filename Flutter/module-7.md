# Section 7: Dicee - Building Apps with State

## Expanded class
- A widget that expands a child of a Row, Column, or Flex so that the child fills the available space.
- Using an Expanded widget makes a child of a Row, Column, or Flex expand to fill the available space along the main axis.
- If multiple children are expanded, the available space is divided among them according to the flex factor.
- An Expanded widget must be a descendant of a Row, Column, or Flex

##### Constructors
Expanded({Key? key, int flex = 1, required Widget child})

##### Properties
- child → Widget
  - The widget below this widget in the tree.
- flex → int
  - The flex factor to use for this child.


## TextButton class
- A Material Design "Text Button".
- Use text buttons on **toolbars, in dialogs, or inline** with other content **but offset** **from that content** with **padding** so that the **button's presence is obvious**.
- buttons do not have visible borders and must therefore rely on their position relative to other content for context.
- Avoid using text buttons where they would blend in with other content, for example in the middle of lists.
- A text button is a label child displayed on a (zero elevation) Material widget.
- The static styleFrom method is a convenient way to create a text button ButtonStyle from simple values.
  - example
```dart
TextButton(
            style: TextButton.styleFrom(
              textStyle: const TextStyle(fontSize: 20),
            )
```
- **If** the **onPressed and onLongPress** callbacks are **null**, then this **button will be disabled**, it will **not react to touch**.

##### Constructors
- TextButton({Key? key, required VoidCallback? onPressed, VoidCallback? onLongPress, ButtonStyle? style, FocusNode? focusNode, bool autofocus = false, Clip clipBehavior = Clip.none, required Widget child})

##### Properties
- autofocus → bool
  - True if this widget will be selected as the initial focus when no other node in its scope is currently focused.
- child → Widget?
  - Typically the button's label.
- enabled → bool
  - Whether the button is enabled or disabled
- style → ButtonStyle?
  - Customizes this button's appearance.
- onLongPress → VoidCallback?
  - Called when the button is long-pressed.
- onPressed → VoidCallback?
  - Called when the button is tapped or otherwise activated.


## dart:math library
- **Mathematical constants** and **functions**, plus a **random number generator**.
- To use this library in your code:
```dart
import 'dart:math';
```

##### Classes
- MutableRectangle<T extends num>
A class for representing two-dimensional axis-aligned rectangles with mutable properties.
- Point<T extends num>
A utility class for representing two-dimensional positions.
- Random
A generator of random bool, int, or double values.
- Rectangle<T extends num>
A class for representing two-dimensional rectangles whose properties are immutable.


##### Constants
- pi → const double
The PI constant.
- e → const double
Base of the natural logarithms
- ln2 → const double
Natural logarithm of 2.
- log2e → const double
Base-2 logarithm of e.
- log10e → const double
Base-10 logarithm of e.

##### Functions
- log(num x) → double
Converts x to a double and returns the natural logarithm of the value.
- max<T extends num>(T a, T b) → T
Returns the larger of two numbers.
- min<T extends num>(T a, T b) → T
Returns the lesser of two numbers.
- pow(num x, num exponent) → num
Returns x to the power of exponent.
- sin(num radians) → double
Converts radians to a double and returns the sine of the value. 
- sqrt(num x) → double
Converts x to a double and returns the positive square root of the value.

## Random Class
- A generator of **random bool, int, or double** values.
- The default implementation supplies a stream of pseudo-random bits that are not suitable for cryptographic purposes.
- Use the **Random.secure** constructor for **cryptographic purposes**.

##### Constructors
- Random([int seed ])
Creates a random number generator.
- Random.secure()
Creates a cryptographically secure random number generator. 

##### Methods
- nextBool() → bool
Generates a random boolean value.
- nextDouble() → double
Generates a non-negative random floating point value uniformly distributed in the range from 0.0, inclusive, to 1.0, exclusive.
- nextInt(int max) → int
Generates a non-negative random integer uniformly distributed in the range from 0, inclusive, to max, exclusive.
