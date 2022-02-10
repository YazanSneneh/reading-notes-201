Implementing Simple SPA Routing Using Vanilla JavaScript
# Using CSS custom properties (variables)
- Custom properties (sometimes referred to as CSS variables or cascading variables).
- entities defined by CSS authors that contain specific values to be reused throughout a document.
- They are set using custom property notation (e.g., --main-color: black;).
- accessed using the **var()** function (e.g., color: var(--main-color);).

### Basic usage
- custom property is done using a custom property name that begins with a double hyphen (--).
- property value that can be any valid CSS value.
- best practice is to define custom properties on the :root pseudo-class.

#### var()
- function i use it to insert value, it takes two params one is name other value.
  - name is required and must start with --
  - value is optional.



# Vanilla Javascript Routes (Implementing Simple SPA Routing Using Vanilla JavaScript)
- to understand how this works, I need to understand history and location objects.

### History and Location Object
-  window.history. History contains all the browser history.
  - to access it I type history and then I’ll get the whole history object and the variety of method’s it has.
- **window.location** It contains all the information about the current location such as origin, pathname, etc.
- 
