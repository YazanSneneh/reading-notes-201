# Beginner Python Course
- **to execute python program from terminal**: type following
  - **python3** name_of_file.py.
  - basically anything ends with .py is a python file.


#### A Python editor
- currently Repl.it is good.

## Strings and numbers
- numbers are in python are integers and floats.
    - **int** represent integers.
    - **float:** present numbers contain decimal values.
    - **strings:** present literal characters and they can be numbers or symbols.
      - strings wre written in either single or double qutations, but i can't mix the wrapped string with both single and double.
    - I can't add strings and numbers, but i can add strings to strings.


## Variables
-Variable names can contain underscores (_), numbers, and letters. They cannot start with a number.

#### Output and Input
- to print something to console i use **print(anything)**.
- to ask user to input something i use :
  - myVar = **input(type something motherfucker).**.
  - input always gets string back from user, so i have to convert numbers using special methods for casting.
    - **int(myStringNumber)**
  - to add them to string i have to convert them to string using **str(numberValToString)**.
- **String formatting:** I can use f string to interpolate variable inside string.
  - example: f"string {variable}" 

##### comments in python.
- *#* is used to create comment

## Lists in python.
- we use them to store many things and we want to be able to easily use that group of things.
- penefits of lists:
  - it's hard to access and manipulate values.
- the use of square brackets denotes a list, and inside it we can place many values. 
  - Each value is separated from other values by commas.
- example: 
  - friends = ["Rolf", "Bob", "Anne"]
- We still can access individual items like so:
  - my_friend = friends[1]
- **What can we store in a list?**
  - You can store anything you want in a list.
  - it is generally recommended that lists only store one type of thing per list.
-  we used the **len()** function. If we put our list inside the brackets, it tells us the length of the list—or how many elements are in it.
   -  **len(friends)**
- You can put lists inside lists:
```python
friends = [["Rolf", 24], ["Bob", 30], ["Anne", 27]]

print(friends[0][1])  # 24
print(friends[1][0])  # Bob
```

##### add things to a list?
- append(the thing)
- friends.append("Jen")
-  you can .append() anything you want—since a list can contain any type of element.
-  example:
```python
friends = ["Rolf", "Bob", "Anne"]
friends.append(["Hello", "World"])

print(friends)  # ["Rolf", "Bob", "Anne", ["Hello", "World"]]
```

#### remove things from a list?
- .remove(the thing)
```python
friends = ["Rolf", "Bob", "Anne"]
friends.remove("Bob")

print(friends)  # ["Rolf", "Anne"]

```
- **Note:**  if you have a list of lists, you'll need to tell .remove() everything the exact thing you want to delete.

#### copy a list?
- **.copy()**
- in python if i want to copy list from another list i would naturally assing it like so listCopy = listOriginal.
  - because arrays are storing by reference if i change on listCopy, i will also update on original one.
- however, to solve this i use **.copy()** method.
```python
friends = ["Rolf", "Bob", "Anne"]

listCopy = listOriginal.copy()
friends_abroad.remove("Bob")
```

#### Lists in lists
- if i copy a list that contain other lists inside, and update list living inside copied list, it will update the original list.
- because i only copied the outer list but inside lists are the same.
- so it will result to update outer lists because i updated the inner lists.
- **Solution:**
  - I must be careful when it come to cpying a list.
  - so in order to solve this i simply create a new list instead of copying or modifying the original list.

## If statements
- conditional is an expression that evaluates to either True or False.
- example: `print(5 == 5)  # True 1`

#### if statement in python
```python
learning_programming = True

if learning_programming:
    print("You're awesome!")
```
#### The if statement is comprised of four parts:
1. The if keyword, first of all.
2. The conditional, which must evaluate to True for the body to run.
3. A colon ( : )
4. In the next line and indented, the body of the if statement.

## INFO: What is indentation?
- Indentation means adding some spaces in front of the line.
- Usually in Python when we want to indent the body of an if statement, we use 4 spaces.
- Python needs indentation in order to work

### compound if statement
- it's chaining to the if statements.
- if a user want to check if user input value for example is more than one hundred will do something, and if it's less than 100 hundered will do something, in this case python will check first condition and if it's true it will execute the body, then check the second condition because i have another if statement, however noway both are true at the same time, so python sovlve it by chaining if statement.
- **elif** allow me to chain if statement with another condition so when one is true, will be executed then python ignore the rest of if statements.
```python
condition_value = true

if condition_vlue:
    do somrthing...
elif condition_Value:
    do something...
elif condition_Value:
    do something..
elif condition_Value:
    do something...
else:
    default value evaluate to all other remaining conditions.
```

### Truthyness and Falsyness in Python
- **bool()** function take any expression and convert it to boolean.
- almost all values can be true, for example:
  -  bool('string ') evaluate to true.
  - bool(1) evaluate to true.
  - bool(true) eval to true.
  - bool([1,2,3]) eval to true.
- values can be false are the following:
  - bool('') false: empty body strings.
  - bool(0), bool(0.0) eval to false.
  - bool(null) eval to false.
  - bool([]) eval to false.

#### not.
- make the condition evaluate to the opposite of the boolean value, for example if i have true condition appened to not, it will become false.
- in if condition statement, in order to negate or use and, or i do following:
  - if condition and condition:
  - if condition or condition:


### Dictionaries
**- What is a dictionary?**
  - dictionary is pretty much list but it store values in key pair value.
  - each key is unique in dictionary.
  - in order to create a dictionary i define dictionary name, then = sign then curly braces and key between qutation and : then value.
  - i seperate each pair by comma.
  - example: 
```python
dictionary = {
  'key':value1,
  'key2': value2
}
```
##### Accessing a value stored in a dictionary
- to access value in dictionary i use dictionary name brackets qutation and inside them keyName:
- **example: dictionary['key']**
- to modify dictionary value i need to bring it's key and assing it's value.
  - `dictionary['key] = updatedValue`
- to add new pair to dictionary:
  - `dictionary['newKey'] = new value`

#### Adding multiple items at once
- we can add multiple pairs by using a method called **.update()**.
- i can add dictionary to another:
  - example:
```python
dict1 = {
  'instructor':'hanaa'
}
dict2 = {
  'instructor2':Tamim,
  'instructor3':yazan
}

dict1.update(dict2)
```
- I can add iteratable to dictionary that happened to be key pair value.
- list is iterable, I know it because i use for loop and while loop on it.
  - example:
```python
dict1 = {
  'instructor':'hanaa'
}
dict1.update([['student':'Yazan'], ['student2':'Rama']])
```
- I can update using keyword, example:
```python
dict1 = {
  'instructor':'hanaa'
}
dict1.update(KeyName = value, KeyName2=value2)
```
#### Copying dictionaries
- copying dictionaries is pretty much the same as lists.
- in order to copy i need to use **.copy()** method.
- and dictionaries and lists store values by reference unlike primitves.
- also, if i use copy on dictionary to copy it in another dictionary, and the original copy have dictionaries inside, i will be losing inner dictionaries values if i update the copy.
-example:
```python
friend_names_to_info = {
    "Rolf": {"name": "Rolf Smith", "age": 24},
    "Adam": {"name": "Adam Wool", "age": 30},
    "Anne": {"name": "Anne Pun", "age": 27}
}

friends_abroad = friend_names_to_info

friends_abroad["Bob"] = {"name": "Bob Sponge", "age": 20}
```

#### Use cases for dictionaries
- The main purpose of a dictionary is to allow you to easily access the values (in case of the example above, the ages) given you only know the keys (the names of friends).
- if you know the friend name you can easily find out their age by using that dictionary.
- A dictionary that maps user IDs to their details;
- A dictionary that maps blog authors to their blog addresses.
- A dictionary that maps coffee bean names to coffee bean information.
### Working with Keys and Values
#### Dictionaries and loops
- We can use the keys individually to get each value, but when we're doing a repeated action, it's generally a good idea to use a loop.
- to return keys by looping on dictionary:
```python
for student in student_attendance:
    print(student)
# output is going to be keys
```
- getting value of keys:
```python
for student in student_attendance:
    print(student_attendence[student])
# output is going to be keys
```
- there is another way to get access to keys values.
```python
for student_key,student_val in student_attendece.items():
  print(f'key is {student_key} and value is {student_val}')
```
- both ways are the same and they print all keys and values.


#### Checking for dictionary membership
- I can check for key if exist in dictionary by using keyword **in**.
- example:
```python
if 'key' in dictionary:
  print(f'theKey value is {dictionary['key']}')
else:
  print('key does not exist')
```
### Functions
#### What are functions?
 - How do you define a function?
- First comes the **def** keyword.
- The next thing is the function name.
- Then comes a set of brackets.
- Then we have ourselves a colon.
- Finally, the indented body which will run whenever we execute this function.
```python
def say_hello():
    print("Hello!")
```
- but it's important to remember to use parentheses. 
- If you try to execute the function without any parentheses, the function won't run.

#### Common pitfalls
- It's generally a bad idea to reuse the names of functions in code.
-  Don't define a new function with the same name as one that already exists.
- Doing so will make Python forget about the old function.
```python
def print():
    print("Hello, world!")

print()
print("Bye, world!")  # Error
```

#### Reusing names (unwittingly)
```python
friends = ["Rolf", "Bob"]

def add_friend():
    friend_name = input("Enter your friend name: ")
    friends = friends + [friend_name]  # Another way of adding to a list!

add_friend()
print(friends)  # Always ['Rolf', 'Bob']
```
- friends inside the function is not the same as the one that created outside of it.
- it has been redeclared inside the function.
- could also keep his existing code by using the global keyword:
```python
friends = ["Rolf", "Bob"]

def add_friend():
    friend_name = input("Enter your friend name: ")
    global friends
    friends = friends + [friend_name]  # Another way of adding to a list!

add_friend()
print(friends)  # Could be ['Rolf', 'Bob', 'Anne']
```
- or the otherway is, python can see variables outside of the function, so the better way to use it is like this
```python
friends = ["Rolf", "Bob"]

def add_friend():
    friend_name = input("Enter your friend name: ")
    friends.append(friend_name)

add_friend()
print(friends)  # Could be ['Rolf', 'Bob', 'Anne']
```
#### Using a function before defining it
- In Python we cannot use anything before we've defined it. This applies for variables, functions, and other constructs.
- This would give you an error (a NameError in fact!):
- **TIP**
range(2) gives you something Python interprets as a list: [0, 1]. That's why that for loop works.

The variable name, _, is commonly used when we need to create a variable (the for loop expects one) but we don't actually want to use it.
```python
for _ in range(2):
  print('a dick')
```

### arguments
- there are 2 types of arguments:
  - positional argument and keyword arguments.
    - positional: the function know them and assign  passed value based on position.
    - Keyword arguments: i assign value to named parameter but i need to know the parameter.
    - example:
```python
def add(x, y):
    result = x + y
    print(result)

add(x=2, y=3)  # 5
``` 
- i can mix positional and keyword arguments.
- **WARNING
Be careful when using positional and keyword arguments together! Keyword arguments must always be specified after positional arguments.**
