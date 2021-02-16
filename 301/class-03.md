# Templating
   * a technique to render client-side view templates with Javascript by using a JSON data source.
   * template is HTML markup, with added templating tags that will either insert variables or run programming logic.
   * template engine then replaces variables and instances declared in a template file with actual values at runtime.
   * convert the template into an HTML file sent to the client.

## Mustache 
   * logic-less template syntax. It can be used for HTML, config files, source code — anything. 
   * It works by expanding tags in a template using values provided in a hash or object.
   * often referred to as “logic-less” because there are no if statements or loops.
   * mustache.js is an implementation of the mustache template system in JavaScript.
   * an example : 
```
    Mustache.render(“Hello, {{name}}”, { name: “Sherlynn” });
      // returns: Hello, Sherlynn
```

# Flexbox
  * Flexbox Layout provide effecient way to layout elements.
  * main idea behind the flex layout is to give the container the ability to alter its items’ width/height (and order) to best fill the available space.
  * the flexbox layout is direction-agnostic as opposed to the regular layouts.

  **Note: Flexbox layout is most appropriate to the components of an application, and small-scale layouts, while the Grid layout is intended for larger scale layouts.**
  * flexbox is a whole module and not a single property, meaning applied on group of elements a container and it's children.
  * Some of properties are meant to be set on the container.
  * Some of properties are meant to be set on the children.
  * **some of properties for container :**
      * **display**: flex.
      * **flex-direction**: row | row-reverse | column | column-reverse;
      * flex-wrap: nowrap | wrap | wrap-reverse;
      * **flex-flow**:a shorthand for the flex-direction and flex-wrap properties, which together define the flex container’s main and cross axes. The default value is row nowrap.
      * **justify-content** : justify-content: flex-start | flex-end | center | space-between | space-around | space-evenly | start | end | left | right ... + safe | unsafe.
      * **align-items**: stretch | flex-start | flex-end | center | baseline | first baseline | last baseline | start | end | self-start | self-end + ... safe | unsafe.
   * **some of properties for children:**
      * **order** : the order property controls the order of how many items will be on one line.
      * **flex-grow** : item to grow if necessary.
      * **flex-shrink** :  flex item to shrink if necessary.
      * **flex-basis** : defines the default size of an element before the remaining space is distributed.
      * **flex** : shorthand for flex-grow, flex-shrink and flex-basis combined
