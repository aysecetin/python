
# If Statement 🤓

- If statements allow us to execute code with conditions.

For example, let's look at the following code:
```py
age = 20
status = "Child"
if age > 18:
    status = "Adult"
age += 1
```

- The above code checks whether the age variable is bigger than 18. If it is, it will set status to hold "Adult" string.

- In the end, the code will increment age by 1 whether the age is bigger than 18 or not.

 

⇨ To use an if statement we need to add a colon : at the end of the if, and everything that is inside the if is indented with 4 spaces:

```py
if condition:
    code
    code
    code
```


⇨ If the condition is True, we will enter the code block inside the if (The indented code)

## Challenge

You are given a code.
The variables a and b have missing values, fill them so that the code inside the if statement will be executed!

**Bonus: try to find more than one solution!**

## Solution

```py
a = 12
b = 11

# Don't change below this line
c = 0
if a >= b and not b < 10:
    c = 2

c += 1
print(f"c = {c}")
```
# If - Else

⇨ if allows us to execute particular code if a condition is met, but what if we want to execute something else if the condition is not met?

For that we have the else statement:
```py
age = 15
status = "None"
if age >= 18:
    status = "Adult"
else:
    status = "Young"
```
In the above example, age is smaller than 18 which means it enter the else code and status will hold "Young".

We can even make it more profound using the elif statement:

```py
age = 68
status = "None"
if age < 18:
    status = "Young"
elif age >= 18 and age <= 65:
    status = "Adult"
else:
    status = "Old"
```
Here it checks whether age is smaller than 18, if not it will continue to the next condition and check whether age is between 18 and 65. If that condition is also not met it will set status to "Old".

⇨ We can add as many elif statements as we want:
```py
if condition1:
    code
elif condition2:
    code
elif condition3:
    code
...
```

***Note that the code inside the if/elif/else must be indented***


## Challenge

⇨You are given a code which gets as input a number that indicates the wind speed and stores it in a variable named wind.

Note: we will learn in next lessons how to get input from the user, currently just don't touch the first line.

Your task is to initialize variable status based on the conditions:

"Calm" if wind is smaller than 8,
"Breeze" if wind is between 8 and 31 (including 8 and 31).
"Gale" if wind is between 32 and 63 (including 32 and 63)
"Storm" otherwise
_Check the test cases to see all the inputs and the expected outputs_

## Solution 

```py
wind = int(input()) # Don't change this line
status = "unset"
# Type your code below

if wind < 8:
    status = "Calm"
elif wind >= 8 and wind <= 31:
    status = "Breeze"
elif wind >= 32 and wind <= 63:
    status = "Gale"
else:
    status = "Storm"

# Don't change the line below
print(f"status = {status}")
```


## Challenge

- You are given a code which gets as input two numbers n1 and n2 and a character op.

***Note: we will learn in next lessons how to get input from the user, currently just don't touch the three first lines.***

 

The possible values for op are '+', '-', '/' and '*'

Your task is to set the variable result based on the conditions:

if op is '+', set result with n1 + n2.
if op is '-', set result with n1 - n2.
if op is '/', set result with n1 / n2.
if op is '*', set result with n1 * n2.

## Solution

```py
n1 = int(input()) # Don't change this line
n2 = int(input()) # Don't change this line
op = input() # Don't change this line
result = 0

if op == "+":
    result = n1 + n2 
elif op == "-":
    result = n1 - n2 
elif op == "/":
    result = n1 / n2 
else:
    result = n1 * n2 
# Don't change the line below
print(f"result = {result}")
```
