# Transforms
  * css3 provide us new ways to position and layout elements on the screen.
  * css3 introduce **transforms** which is a property provide us ways to change, resize and position elements.
  * there are 2 settings for transfor property, 2 **dimensions and 3 dimentions ** and each one has it's own properties and values.
  * transform support by browser is **not great**, meaning not supported by all browsers and **not supported** by many **previous browser versions**.


## Transform Syntax
  * include the transform property followed by the value.
  * element{transfor: property}
    **Example:** 
    ```
    div{
      transform: scale(1.5)
    }
    ```
  *  to gain the best support across all browsers.
     ```
      div {
        -webkit-transform: scale(1.5);
        -moz-transform: scale(1.5);
        o-transform: scale(1.5);
        transform: scale(1.5);
     } 
     ```
   
### 2D Transforms & 3D Transforms
 * Two-dimensional transforms work on the x and y axes, known as horizontal and vertical axes.
* three dimentional work on x axes, y axes as well as z axes.
* and everything apply to 2d works similar to 3rd, so i won't include it in read.
* to know more about 3rd this link will help when needed [3D and 2D transforms](https://learn.shayhowe.com/advanced-html-css/css-transforms/)
##### 2D Rotate
* rotation allow me to rotate element from 0 to 360 degree.
   * positive degree will rotate clockwise.
   * negative degree will rotate counter clockwise.
* the center of the element is the default value of rotation 50% 50%, meaning **50% down from x** and **50% coming from y**.
* **transform: rotate(20deg)**
* pixels or percentages, do not apply here.
##### Scale
  * change the appeared size of an element. 
  * The default scale value is 1.
  *  any value between **.99** and **.01** makes an element appear smaller while any value **greater than or equal to 1.01 **makes an element **appear larger**.
  *   **scaleX value scale the width** of an element while the **scaleY value scale the height** of an element.
  * **transform: scale(1.1)**
  * pixels or percentages, do not apply here.
  

##### 2D Translate
  *  translate value works a bit like that of relative positioning.
  * push and pull an element in different directions without interrupting the normal flow of the document.
  * **translateX** value change the position of an element on the horizontal axis.
  * **translateY** value change the position of an element on the vertical axis.
  * unlike scale (scaleX()) to specify x and y i can declare them in the same function.
  * transform : **translate**(**X**px, **Y**px)


##### SKEW
  * skew, is used to distort elements on the horizontal axis, vertical axis, or both.
  * Use the skewX value distorts an element on the horizontal axis.
  * skewY value distorts an element on the vertical axis.
  * distort an element on both axes the skew value is used **declare** the x axis value first, **followed by a comma**, then the y axis value.
  * The distance calculation of the skew value is measured in units of **degrees**.
  * pixels or percentages, do not apply here.
  * **transform: skew(5deg, -20deg);**

#### SHORTHAND
transform: rotate() scale() translate() skew()

##### Transform Origin
   * default transform origin is the dead center of an element,both 50% horizontally and 50% vertically.
   * If two values are specified, the first is used for the horizontal axis and the second is used for the vertical axis.
   * **transform-origin: 0 0;**.
   * **transform-origin: 100% 100%;**.
   * **transform-origin: top left;**
   * **transform-origin: 20px 50px;**

# Transitions & Animations
  * transitions allow developer to modify behaviour of element when state change i can control state change, meaning : hover, active are states (from pseudo class).
  * transition only work when state change.
  * Animations within CSS3 allow the appearance and behavior of an element to be altered in multiple keyframes.
  * animations can set multiple points of transition upon different keyframes.

### Transitions
 * As mentioned element must have a change in state, and different styles must be identified for each state.
 * he easiest way for determining styles for different states is by using the :hover, :focus, :active, and :target pseudo-classes.
 * There are four transition related properties in total, including transition-property, transition-duration, transition-timing-function, and transition-delay.
 * not all of them required when specify transition.
 * example : 
 ```
 .box {
  background: #2db34a;
  transition-property: background;
  transition-duration: 1s;
  transition-timing-function: linear;
}
.box:hover {
  background: #ff7b29;
  } 
  ```

##### shorthand
 transition : background 1s linear 
