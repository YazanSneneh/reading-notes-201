# Section 10: Quizzler - Modularising & Organising Flutter Code
## Collections
collections in dart that i can use are lists, sets and maps

###### Lists: 
- to initialize a list I use literals to create and initialize lists.
- or I can use constructor to create lists.
- List class defines several methods for interacting with list such as adding, removing, counting and finding element inside list etc..
- create list:
  - Create an empty list `String names = [];  || var names = <String>[];`
  - create list with list literals `String names = ['Yazan','Any One '];`
  - get the first element: `names.first`
  - get last item: `names.last`
  - add to list one item: `names.add();`
  - add to list multi items: `names.addAll(['new name 1','new name 2']);`
  - remove from list: 
```dart
int removedItem = names.indexOf('Yazan');
names.removeAt();
```
- remove all items: `fruit.clear();`
- sort a list: `names.sort((one, two)=> one.compareTo(b))`
- Lists are parameterized types (generics), so I can specify the type that a list should contain:

```dart
// This list should contain only strings.
var fruits = <String>[];

fruits.add('apples');
fruits.add(5); // Error: 'int' can't be assigned to 'String'
```


###### Sets:
- A set in Dart is an unordered collection of unique items.
- Because a set is unordered, I can’t get a set’s items by index (position).
- create a list
```dart
// Create an empty set of strings.
var ingredients = <String>{};
```
- add new items toit.
```dart
// Add new items to it.
ingredients.addAll(['gold', 'titanium', 'xenon']);
assert(ingredients.length == 3);

// add new single item
ingredients.add('shit');

// Adding a duplicate item has no effect.
ingredients.add('gold');
```

- remove item from set; `fruits.remove('apples')`
- check if item exist in set: `fruits.contains('gold')`.

###### Maps:
- A map, commonly known as a dictionary or hash, is an unordered collection of key-value pairs.
- Maps associate a key to some value for easy retrieval.
- Declare a map using a terse literal syntax:
```dart
// Maps often use strings as keys.
var hawaiianBeaches = {
  'Oahu': ['Waikiki', 'Kailua', 'Waimanalo'],
  'Big Island': ['Wailea Bay', 'Pololu Beach'],
  'Kauai': ['Hanalei', 'Poipu']
};
```

- declare with traditional constructor:
```dart
// Maps can be built from a constructor.
var searchTerms = Map();

// Maps are parameterized types; you can specify what
// types the key and value should be.
var nobleGases = Map<int, String>();
```

- to add, get, and set map items use the bracket syntax.
- Use remove() to remove a key and its value from a map.
```dart
var nobleGases = {54: 'xenon'};

// Retrieve a value with a key.
assert(nobleGases[54] == 'xenon');

// Check whether a map contains a key.
assert(nobleGases.containsKey(54));

// Remove a key and its value.
nobleGases.remove(54);
```
- To check whether a map contains a key; ` containsKey()`

- Use isEmpty or isNotEmpty to check whether a list, set, or map has items:
- To apply a function to each item in a list, set, or map, you can use `forEach()`:

