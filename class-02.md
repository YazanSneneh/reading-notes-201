# Text
  * tags provide extra meaning and allow browsers to show users the appropriate structure for the page.
  * Structural markup: the elements that you can use to describe both headings and paragraphs.
  * Semantic markup: which provides extra information; such as where emphasis is placed in a sentence.

#### Headings
  * HTML has 6 levels of heading from h1 to h6.
  * the most important heading and the biggest heading is `<h1></h1>` and there is only h1 in the page and it's usually the title of the webpage.
  * these headings arranged from most important to least important, which means the least important heading on the page is `<h6></h6>`.
  
#### Paragraphs
  * paragraphs are consist of 1 sentence or more.
  * To create a paragraph add the content between p tag like so `<p>this is a paragraph</p>`

#### Bold & Italic
  * b tag : `<b> </b>`.
     * Make content between b tag appear **bold**, bold means what's between the b tag looks **dense**.
  * i tag : `<i> </i>`
     * make the content between the `<i> </i> ` tag italized like and looks like swaying *THIS IS AN EXAMPLE OF ITALIZED*.
   
#### Superscript & Subscrip
  * The `<sub>` element is used to contain characters that should be subscript.
  * The `<sup>` element is used to contain characters that should be superscript such as the suffixes of dates or mathematical concepts like raising a number to a power such as 22.

#### Line Breaks & Horizontal Rules
  * `<br/>`
     * if you wanted to add a line break inside the middle of a paragraph you can use the line break tag `<br />` to show it on new line.
  * `<hr/>` 
     * create thin herozintal line and divide content or section on the page.
 
## Semantic Markup
 There are some text elements that are not intended to affect the structure of your web pages but they do add extra information to the pages — they are known as semantic markup.

#### Strong & Emphasis
   * `<Strong>`
     * it give the same strucutre as the `<b>` tag but `<strong>` tell browser this is important text
   * Emphasis : `<em>`
     *  indicates emphasis that subtly changes the meaning of a sentence.
   
#### Quotations : `<blockquote>`
     * The `<blockquote>` - element is used for long quotes.
     * The `<q>` - element is used for short quotes.

#### Abbreviations & Acronyms
     * `<abbr>` - used to add acronym e.g. `<abbr title ='doctor'> Dr </abbr>`.

#### Author Details
     * `<address>` -  use: to contain contact details for the author of the page, like below.
        ``` 
        <address> 
            <p><a href="mailto:homer@example.org"> homer@example.org</a></p>
            <p>742 Evergreen Terrace, Springfield.</p>
        </address>
        ```
# Understanding CSS: Thinking Inside the Box
   * The key to understanding how CSS works is to imagine that there is an invisible box around every HTML element.
   * CSS Properties Affect How Elements Are Displayed.
   * there are 3 ways to use css internal, inline and external.

#### BLOCK & INLINE ELEMENTS
      * **Block level elements** - elements take full width of the parent box and high of the content, example of block elements are `<div>, <header>, <h1>, <p>`.
      * **Inline level elements** - elements take the height and with of the content, example of inline elements are `<img>, <a>` tags.

## CSS Selectors
      * there are many ways css allow me to target elements.
      * the list of these elements are : 
        
        Selector | Meaning | Example
        -----------------------------
        universal selector | apply to all elements on the page | `*{ css rules...}`
        -----------------------------
        type selector | match element name | `h1{css rules...}`
        -----------------------------
        class selector | any element match target class |` .link{css rules...}`
        -----------------------------
        ID Selector | match element with ID | `#id{css rules...}`
        -----------------------------
        child | match child element that directly inside parent | `header > h1 {css rules...}`
        -----------------------------
        descendant | all elements inside matched element | `main section{css rules...}`
        -----------------------------
        Adjacent Sibling | match element sibling next to element | `h1+p{css}`
        -----------------------------
        General Sibling | Matches an element that is a sibling of another, although it does not have to be the directly preceding element | `h1~p {}`
        -----------------------------