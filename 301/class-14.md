# Database Normalization
 * it's a process where we organize databases to tables.
 * each table serve one purpose and do one thing.
 * **why we would do this ? **, for 3 reasons: 
    * avoid repititve data.
    * avoid endless database data modification.
    * simplify queries.

 * The stages of organization are called normal forms.
 * there are three normal forms most databases adhere to using.
 * each form improve the database to satisfy normalization objectives.

## Normalizations Stages
 * data in this image before normalization :[database](https://www.codeproject.com/KB/database/832221/2bd01c59-ee13-4b57-8e0e-ef4bb44c164a-r-700.Png).
 * The first thing to notice is this table serves many purposes including:
    * Identifying the organization’s salespeople.
    * Listing the sales offices and phone numbers.
    * Associating a salesperson with a sales office.
    * Showing each salesperson’s customers.

#### Data Duplication and Modification
   1. for each SalesPerson, have listed both the SalesOffice and OfficeNumber. This information is duplicated for each SalesPerson.
   2. Duplicated information presents two problems :
      * It increases storage and decreases performance.
      * It becomes more difficult to maintain data changes, for example if i wanto to update officenumber i have to do it for each record

#### Insert 
   * I can't add new record until I know information for the entire row.
   * I can't insert new office because to do it.
   * I cannot record a new sales office until I also know the sales person. **Why?** Because in order to create the record, we need provide a primary key.
  
#### Deletion 
 * Deletion of a row can cause more than one set of facts to be removed, for example:
    if john quite his job then all data wil be removed along with him.

#### Search Issues
  * In the SalesStaff table, if I want to search for a specific customer such as **Ford**, you would have to write a query like:  
```
SELECT SalesOffice
FROM SalesStaff
WHERE Customer1 = ‘Ford’ OR
      Customer2 = ‘Ford’ OR
      Customer3 = ‘Ford’
```
 * it would never be the case if ford is in customer table.
 * 
## Definition of Normalization
 * There are three common forms of normalization: 1st, 2nd, and 3rd normal form.
 *  The forms are progressive, meaning that to qualify for 3rd normal form, a table must first satisfy the rules for 2nd normal form, and 2nd normal form must adhere to those for 1st normal form. 
 * summarize the various forms:
   * First Normal Form – The information is stored in a relational table and each column contains atomic values, and there are not repeating groups of columns.
   * Second Normal Form – The table is in first normal form and all the columns depend on the table’s primary key.
   * Third Normal Form – The table is in second normal form and all of its columns are not transitively dependent on the primary key.