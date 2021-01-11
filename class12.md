# chartjs
  * **JavaScript plugin** that **uses HTML5’s canvas** element to **draw the graph onto the page**.
  * used to display data visually
  * They’re easier to look at and convey data quickly.
  * makes using all kinds of bar charts, line charts, pie charts and more, incredibly easy.
 
### how to use chart ? 
   1. The first thing we need to do is download Chart.js.
   2. Copy the Chart.min.js out of the unzipped folder and into the directory you’ll be working in.
   3. Create a new html page and import the script:
      ```<script src='Chart.min.js'></script>``` in head section.

#### Drawing a line chart
  1. create a canvas element in our HTML.
  2. add this to the body of our HTML page:
      ```<canvas id="buyers" width="600" height="400"></canvas>```.
  3. Next, Write a script that will retrieve the context of the canvas.
  4. add this to the foot of your body element:
      ```<script> var buyers = document getElementById('buyers').getContext('2d'); new Chart(buyers).Line(buyerData); </script>```

   5. We can actually pass some options to the chart via the **Line method**.
   6. Inside the same script tags we need to create our data.
   7. it’s an object that contains labels for the base of our chart and datasets to describe the values on the chart.
           ```var buyerData = { 
      labels : ["January","February","March","April" "May","June"],
         datasets : [ 
        {
         fillColor : "rgba(172,194,132,0.4)",
         strokeColor : "#ACC26D",
         pointColor : "#fff",
         pointStrokeColor : "#9DB86D",
         data : [203,156,99,251,305,247]
         }
     ] 
 }```
# canvas
  * canvas is a tag like img tag, it's used to drow inside it.
  * canvas doesnt have src attribute or alt, but only have width and height.
  * we can use canvas to drow shapes.

### drawing text 
  Drawing text
The canvas rendering context provides two methods to render text:

```fillText(text, x, y [, maxWidth])
Fills a given text at the given (x,y) position. Optionally with a maximum width to draw.
strokeText(text, x, y [, maxWidth])
Strokes a given text at the given (x,y) position. Optionally with a maximum width to draw.
```
