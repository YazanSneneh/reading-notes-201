# Images
  *There are many factors to consider when choosing image for the webpage regardless of why including image:
    * attractive image.
    * choose the right size for the image.
    * choose the right format for the image.
    * optimize the image for the performance.
  * A picture can say a thousand words, and great images help make the difference between an average-looking site and a really engaging one.
  * It is good practice to create a folder for all of the images the site uses.
  * it's good to place image in `<figure>` tag to stand out when needed.
  * 
  
#### add image for the website
  * the tag `<img>` allow me to add image to website.
  * img tag take `src ='distination'` attribute.
  * `alt=''`  in case the image not loaded, alt tag provide text tell what is this image.
  * Height & Width of Images specify the size of the image (to keep it responsive don't add height).

#### Three Rules for Creating Images :
  * Save images in the right format: png, jpeg or gif.
  * Save images at the right size, if image is smaller than height and width it will appear very poor and low resolution.
  * Use the correct resolution, use higher image resolution so it be attractive.

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
    ```<address> 
            <p><a href="mailto:homer@example.org"> homer@example.org</a></p>
            <p>742 Evergreen Terrace, Springfield.</p>
    </address>```

# COLOR
  The color property allows you to specify the color of text inside an element.
  exmaple  element{ color:red;}
#### three common ways in which you can indicate your choice of colors
   You can specify any color in CSS in one of three ways:
     1. rgb values.
        These express colors in terms of how much red, green and blue are used to make it up. For example: rgb(100,100,90)
     2. hex codes. 
        hex codes These are six-digit codes that represent the amount of red, green and blue in a color. preceded by a pound or hash # sign. For example: #ee3e80
     3. color names.
        There are 147 predefined color names that are recognized by browsers. For example: DarkCyan.
##### background color
   * CSS treats each HTML element as if it appears in a box, and the background-color  property sets the color of the background for that box.
   * You can specify your choice of background color in the same three ways you can specify foreground colors.
#### opacity
   * CSS3 introduces the opacity property which allows you to specify the opacity of an element and any of its child elements. and any of its child elements. The value is a number between 0.0 and 1.0.

## SUMMARY
   * Color not only brings your site to life, but also helps convey the mood and evokes reactions.
   * There are three ways to specify colors in CSS: RGB values, hex codes, and color names.
   * Color pickers can help you find the color you want.
   * It is important to ensure that there is enough contrast between any text and the background color (otherwise people will not be able to read your content).
   * CSS3 has introduced an extra value for RGB colors to indicate opacity. It is known as RGBA.
