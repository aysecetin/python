# Arguments

- An argument in a function is a value that you pass into the function when you call it. To add arguments to a function we write them inside the parenthesis ():

```py
def function_name(arg1, arg2, ...):
    code
```
- We can name the arguments as we want and we can write as many arguments as we need.

- To call a function and pass arguments to it we write:

```py
function_name(value1, value2, value3, ...)
```
- Passing too many arguments to a function that is expecting less arguments will cause the program to fail

**Example of usage:**

```py
def is_even(number):
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")

for i in range(15, 34):
    is_even(i)
for i in range(153, 219):
    is_even(i)
```

- Here we have a function called is_even that accepts one argument called number and print if the number is even or odd. Then we call the function twice: one time for all the numbers between 15 and 34, Second time for all numbers between 153 and 219.


## Challenge

- Write a program that gets two inputs, numbers. The input numbers are the arguments of the below function. 

Create a function that gets two arguments, calculates the product of them and prints it, name the function however you like.

Call the function with the input numbers.

***Note! In your code, write the function before it's call/execution statements.***

