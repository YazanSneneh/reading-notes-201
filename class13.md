# HTML5 LOCAL STORAGE or WEB STORAGE
##Cookies
 * Cookies can be used for persistent local storage of small amounts of data.
 * But they have three potentially dealbreaking downsides:
    * included with every HTTP request, thereby slow down web application by needlessly transmitting the same data over and over.
    * Cookies are limited to about 4 KB of data — enough to slow down your application


 * What we really want is ! (writer want jinn)
   * a lot of storage space.
   * on the client side.
   * that persists beyond a page refresh.
   * and isn’t transmitted to the server.

## Local Storage
  * it’s storage native browser API allow web pages locally, within the client web browser.
  * this data kept stored inside browser even if i leave website.
  * it stay saved even if i close tab.


#### access HTML5 local Storage
  * it's based on named key/value pairs, You store data based on a named key.
  * then you can retrieve that data with the same key, The named key is a string.
  * The data can be any type supported by JavaScript.
  * data is actually stored as a string.
  *  If you want to retrieving anything other than strings, you will need to use functions like `parseInt()` or `parseFloat()`
  *  the limit of web storage is **5 mb**, it's important that everything is stored as string, in another word if i store float number so there will be much added to storage.

* **Example :** to store data inside storage 
   `localStorage.setItem("fname", "yazan");`.
*  to retrieve data stored I should use key like mentioned earlier: 
   `var data = localStorage.getItem("fname");`.
* to remove item from storage :
  * `localStorage.removeItem("fname");`

**remainder:** Name/value pairs are always stored as strings. Remember to convert them to another format when needed!