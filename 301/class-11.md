# EJS
 * a template engine for nodejs.
 * it use javascript language.
 * it allow me to create dynamic webpages.
 * it basically allow me to do following : 
      * inject variables to html page.
      * allow me to render array of objects.
      * it give me ability to make a conditional render.
      * it allow me to create a layout.
      * it allow me to create partials.


### Using EJS
  1. inside terminal `npm install ejs`.
  2. then navitage to project folder and set view engine to use ejs.
      * `app.set('view engine', 'ejs') // tell it i am using ejs` 
      * `app.set('views', __dirname+ 'views') // tell app that views inside views folder in the first parameter, and it's living inside the path inside the second parameter`.

  3. create a file in views folder with extention .ejs : `index.ejs`.
  4. write html inside it.
  5. create a route and send that file on matched url, the reason it will work because i configured my application to use it earlier.

```
a.get('/home',(req,res)=>{
    res.render('index')
})
```

### INJECT VARIABLES.
 * the `.render()` method take 3 parameters: fileName, object and callback function.
 * the object recieve data:  `render('index', {name: 'yazan'})`
 * inside index.ejs: ` <h1> I am  <%= name %></h1>`.

### control flow: 
* i can write either for loops over list of items or create if statement.
* inside object again : {arr: ['yazan','Anna','Halo']}.
* inside index.ejs : 
```
    <% for(let i =0; i<arr.length; i++){ %>
           <li> <%= arr[i]%> </li>
          
    <% } %>
```
* if statement is the same structure:
* wrap <%%> around flow.
* wrap <%=%> around injected variable.

### Layout.
 * it help me to create the main layout of the website, for example i have header file inside every page in the website, nav as well as footer.
 * the body is the only changeable part of the webpage.
 * using layout will help me add this layout and only change the body.
 * it's not native model inside my ejs, express or node.js which means i have to download that paackage.
 * to download it `npm install express-ejs-layouts`
 * to use it require it `const expressLayouts = require('express-ejs-layouts')`
 * app.use(expressLayouts).
 * create a **route** for **home page** and a **route** for **about page**.
 * inside **views folder**, create `layout.ejs`.
 * write header, nav, footer.
 *  add body like so : ` <%- body %>` and automatically all routes will be handles inside the layout file.
 * run app and see the different.

### Partials.
  * partials works similar to layout but the different is we create resuable code instead of writing it over and over (it has nothing to do with the layout).
  * for example i create code and want it to run in more than one page inside the body.
  * in this case partials will come in handy.
  * unlike partials they are inside the ejs native module.
  * to use them just create a folder name it partials.
  *  create file want to resue and write html inside of it.
  *  go back to file want to **resue** the file.
  *   add this line : <%- include('partials/partialFile.ejs')%>