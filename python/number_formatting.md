# Formatting Numbers for Printing in Python
## Precision
- formatting a floating point number to a given level of precision:
  - To specify a level of precision, we need to use a colon ( : ).
  - followed by a decimal point.
  - along with some integer representing the degree of precision.
  - place this inside the curly braces for an f-string, after the value we want to format.

```python
x = 4863.4343091          # example float to format

print(f"{x:.6}")          # output: 4863.43
```
- As we can see, our very long float got shortened down to just 6 figures.
- If we specify fewer figures than we have in the integer portion of the float, we end up with an exponent representation instead: `4.86e+03`
- **how do we specify 3 decimal places?**
  - just need to add an **f** after number of decimal numbers i want.
  - example:
```python
x = 4863.4343091

print(f"{x:.3f}")  # 4863.434
```

## Separators
- seperators are used with large numbers for example 1000000
- they seperate the number to make it easier to read : 1000 000
- how to use them ?
    - add the seperator after ( : ).
    - example: `print(f'{x:,}') # 1,000,000` 
    - it can work with floats as well: `print(f" {x:,.3f}")`

## Percentages
- I can format the number to render as percintage, or add percentage after my number i do the following.
- i swtich f(that stands for fixed) and add percentage(%)
- example:
```python
questions = 30
correct_answers = 23

print(f"You got {correct_answers / questions :.2%} correct!")
# You got 76.67% correct!
```
- When formatting a number as a percentage, the level of precision always refers to the number of digits after the decimal point.