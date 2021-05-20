# Implementation: Hash Tables
- Hash tables are data structure that use key value pair.
- Every **bucket**  in the table has the key and value pair.
- it's done by saving the key hashed into data structure and it will map to the value .
- hashed means is encode the key that will lead to a value to another format.

- hashmaps use the advantage of arrays.
- now the array access is O(1) if we know the index.
- but if we don't know index it's O(n) because we have to go throught all elements in worse case.
- so hash function take the key and return integer that can be used as index where value is stored.


### Structure
##### Hashing
hashing is used to convert the string to integer, and characteristics of that key must be deterministic which means output is determined by input and the code should always return the same integer value.
##### Creating a Hash
- hashtable is created from an array.
- write code to turn key into another format.

Example :
```java
Key = "Cat"
Value = "Josie"

67 + 97 + 116 = 280

280 * 599 = 69648

69648 % 1024 = 16

Key gets placed in index of 16.
```

- **how values are stored?**
- Each Index of the array contain buckets.
- each bucket contains one key/value pair combination.
- all buckets start with null until it contain key pair.

###### Collisions
- collision occurs when more than one key hashes to the same index in an array.
- a perfect hash will never have any collisions.
- the collision can be solved by instead of initialize it to null, instead init a linked list.
- since each index bucket now contain linked list.
- if two hashes map to the same index, they will be stored as nodes into linked list.


##### store and retrieve
- Hash maps do this to store values:
1. accept a key
2. calculate the hash of the key
3. use modulus to convert the hash into an array index
4. store the key with the value by appending both to the end of a linked list.

- Hash maps do this to read value:
1. accept a key
2. calculate the hash of the key
3. use modulus to convert the hash into an array index
4. use the array index to access the short LinkedList representing a bucket
5. search through the bucket looking for a node with a key/value pair that matches the key you were given

## Internal Methods
- Add()
- Find()
- Contains()
