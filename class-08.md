# LAYOUT CSS
In this chapter we are going to look at how to control where each element sits
on a page.
### Blocks level element vs in-line level element
 * CSS treats each HTML element as if it is in its own box.
 * This box will either be a block-level box or an inline box.
    * block level elements take full width, that means they don't allow any box to stack before and after it on the same page e.g. h tags, header tag ...
    * inline level element : take the content width and height of elements and don't accept height, width, margin or padding attributes and inline elements stack next to each others e.g. image, a tags.

### Controlling the Position of Elements
  * each element on the page has a normal position, this position controlled by the box model properties such as margin, padding, border and content as well as display property.
  *  there is also another property called position, and following are the values of position.
- static - it's the default position of elements on page. 
- relative - position the element relatively to it's original position, for example when i set  `position: relative` and give it `right: 200;` it will move the element from it's right `200px` to the left. 
- absolute - position element related to closest parent has relative position, so when i set value `right:200` it will be away from the right of it's parent `200px`
- fixed : position element fixed on the page, even on scroll.
- z-index - each element has z-index by default, the position of element depend on the x and y of the page.
   * also they have z-index which means closer or far from user.
   * the last element has the higher z-index value and keep going lower up to the first element. 
- float : float element to far right or far left.
- clear : i use it after float, to clear the mess float created, and clear added on the first element after the property use float.
### Creating Multi-Column Layouts with Floats :
- width
- float
- margin

### Layout Grids :
Composition in any visual art (such as design, painting, or photography) is the placement or arrangement of visual elements — how they are
organized on a page. Many designers use a grid structure to help them position items on a page, and the same is true for web designers.
### CSS Frameworks :
CSS frameworks aim to make your life easier by providing the code for common tasks, such as creating layout grids, styling forms, creating.
### Multiple Style Sheets :
- @import
- link
### Summary LAYOUT
1- `<div>` elements are often used as containing elements.
to group together sections of a page.
2- Browsers display pages in normal flow unless you specify relative, absolute, or fixed positioning.
3- The float property moves content to the left or right
of the page and can be used to create multi-column layouts. (Floated items require a defined width.)
4- Pages can be fixed width or liquid (stretchy) layouts.
5- Designers keep pages within 960-1000 pixels wide,  and indicate what the site is about within the top 600 pixels (to demonstrate its relevance without scrolling).
6- Grids help create professional and flexible designs.
7- CSS Frameworks provide rules for common tasks.
8- You can include multiple CSS files in one page.