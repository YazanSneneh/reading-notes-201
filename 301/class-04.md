# Regular expressions (regex or regexp)
 * extract information from any text by searching for one or more matches of a specific search pattern. 
 * **Fields of application** : from validation, parsing/replacing strings, passing through translating data to other formats and web scraping, searching for items etc...

 * **NOTE : One of the most interesting features is that once you’ve learned the syntax, you can actually use this tool in (almost) all programming languages **.
 * **Basic topics:**
    * Anchors — ^ and $ : 
    | Anchors      | explination                                       |
    | ------------ | ------------------------------------------------- |
    | ^The         | matches any string that starts with The           |
    | end$         | matches a string that ends with end               |
    | ^The end$    | exact string match (starts and ends with The end) |
    | roar         | matches any string that has the text roar in it   |
    | class04-read |                                                   |

    * Quantifiers — * + ? and {}:
        | Quantifiers | explination                                             |
        | ----------- | ------------------------------------------------------- |
        | abc*        | matches a string that has ab followed by zero or more c |
        | abc+        | matches a string that has ab followed by one or more c  |
        | abc?        | matches a string that has ab followed by zero or one c  |
        | abc{2}      | matches a string that has ab followed by 2 c            |
        | abc{2,}     | matches a string that has ab followed by 2 or more c    |
        | abc{2,5}    | matches a string that has ab followed by 2 up to 5 c    |
        
    * Character classes — \d \w \s and .
    | Character classe | explination                                                       |
    | ---------------- | ----------------------------------------------------------------- |
    | \d               | matches a single character that is a digit                        |
    | \w               | matches a word character (alphanumeric character plus underscore) |
    | \s               | matches a whitespace character (includes tabs and line breaks)    |
    | .                | matches any character                                             |

## Flags
 * A regex usually comes within this form /abc/, where the search pattern is delimited by two slash characters /.
 * At the end we can specify a flag with these values (we can also combine them each other):
   * **g** (global) does not return after the first match, restarting the subsequent searches from the end of the previous match
   * **m** (multi-line) when enabled ^ and $ will match the start and end of a line, instead of the whole string
   * **i** (insensitive) makes the whole expression case-insensitive (for instance /aBc/i would match AbC).

# Responsive Layouts with CSS Grid
   * CSS grid lets us not only arrange elements in a row or a column, but in multiple rows and columns.
   * Grid gives us control over how wide or narrow each of the ‘grid cells’ get.
   * **Note : Often when we put images in a responsive grid layout like this we come across the problem of the images stretching out of proportion, `object-fit:cover; ` help me here**.
   * **Note:** float, display: inline-block, display: table-cell, vertical-align and column-* properties have no effect on a grid item.
   * **display:grid;** Defines the element as a grid container and establishes a new grid formatting context for its contents.
