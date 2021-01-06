# JS Events
  * js event trigger when user do something make it trigger.
  * for example, when user click button it send message to the user.
  * when the DOM generate the object tree, javaScript can access these elements and add events on html elements(tree object)
  * event attached to element.when user do something on element it trigger javascript code, then the code respond.

### EVENT TYPES

  * **UI EVENTS** : Occur when a user interacts with the browser's not the webpage.
    *  load  - W eb page has finished loading.
    *  scroll - when user scroll down or up.
    *  resize - Browser window has been resized.
  * **KEYBOARD EVENTS** : Occur when a user interacts with the keyboard 
    * keydown - when user click key.
    * keyup - when user release key.
    * keypress - when user click 
  * **MOUSE EVENTS** Occur when a user interacts with the mouse.
    * click - when mouse click occur, and mouse should be released.
    * dblclick - when user double click on mouse.
    * mousedown - when mouse clicked, still event will trigger even mouse is not released.
    * mouseup - when mouse get clicked and should be released.
    * mouseover - when mouse moved over the element.
  * **FORM EVENTS**
    * submit - when user submit a form using button 
    * cut - when user cut content from form.
    * copy - when user copy content from form.
    * paste - when user paste something to form
    * select - when user select text in form field.

### How Event Trigger javascript code.
    1. Select t he element node(s) you want the script to respond to.
      * select element by tag name (I select array of elements because i might have multi tags of the same kind).
      * select elememnt by class name (also array because i might have the same class on multi elements).
      * select element by class name ( i have one id only for each element).
      * query selector select 1 element.
      * query selector all (select array) 
    2. attach event to selected element.
    3. write scripts will run when event triggered.

### Three ways to bind (add) events to element.
   1. inline - i give element event as attribute and give it function to trigger (value), it uses key pair value.
   2. using dom (e.g. element.event(function)).
   3. add event listener.

### THE EVENT OBJECT
  * When an event occurs, the event object tells you information about the event, and the element it happened upon.
  * the event object passed to the function that event trigger it.
  * The event object has methods that change: the default behavior of an element and how the element's ancestors respond to the event like preventDefau1t(), that prevent the next default behaviour of the targeted element.

### EVENT DELEGATION
  * adding event listeners to a lot of elements can use a lot of memory and slow down performance.
  * adding event listeners to each element can use a lot of memory and slow down performance.
  * when i add event on element parent also affected e.g. if i add click event on link, and click on link parent node also will get clicked.
  * by targeting the parent element, add event to it, then i know which element triggered the event.
  * this way i can reduce number of event listener.

#### more on delegation 
  * WORKS WITH NEW ELEMENTS - if i add new element i dont have to add event to it.
  * SIMPLIFIES CODE - because instead of multi event listeners i add one event.


# Forms
   * form word is taking from the blank paper where person use it to fill content in specified place.
   * forms used to collect data from user.
   * forms come in handy when user want to buy online for example, or search for something.
  
### Form Controls
   * There are several types of form controls that you can use to collect information from visitors.
   * text.
   * number.
   * password.
   * radio button.
   * check box.
   * calendar.
   * upload files.
   * submit form.

### how form work ? 
   1. user fill required data.
   2. click on submit, then data travel to server for further process.
   3. The name of each form control is sent to the server along with the value the user enters or selects.
   4. The server processes the information using a programming language such ass node.js or php.
   5. server generate respond.
   6. send feedback to user.