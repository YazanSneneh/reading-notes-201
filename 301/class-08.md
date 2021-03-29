# SQL
* stands for structured query language.
* allow user to query, transform and manipulate data.
* SQL used in mobile and websites.

## Relational databases
 * the model of relational database, it's like an excel spreadsheet that contain tables.
 * these tables are two-dimentional tables.
 * each table contain fixed number of columns and N number of rows.
 * for example, if I want list of most used cars model in Amman and information related to it, such as it's mode, number of wheels, number of doors, year created.
 * and we might want to know which car license is expired so we might attach that table to another.
 * then use this data to call driver to renew his license.


#### Select statement.
 * it allow me to make a query on database and bring it.
 * query refer to the data i am looking at.
 * I can make a query on 1 column, multi columns or the entire table.
 * we can think of table as instance like Dog, Bird, Car and so on.
 * it means the table contain all properties related to that entity.
 * Syntax: 
``` 
SELECT column1, column2
from TABLENAME
// i can also select the entire table using (*)

SEECT *
from TABLE
```
#### Queries with constraints
 * sometimes we need to make a query on tables have thousands of rows.
 * and it's pain in the ass to get all rows and search on what we want.
 * constrains allow me to query on table based on condtions.
 * row that satisfy condition will be in result only.
 * SYNTAX: 
  ```
SELECT column1, columns2
from TABLE
WHERE condition
   AND/OR condtion two ...
  ```