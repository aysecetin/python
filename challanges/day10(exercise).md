
# _Recap Challenge_


## Challenge

⇨ Write a program that gets input from the user, his age.

⇨ The program will output (print) the number of missing years till 120 (in a specific format, shown below).

⇨ For example, for input 25, the expected output is "95 years till 120".

## Solution 
```py
# Get user input
age = int(input())

# Calculate the missing years till 120
years_till_120 = 120 - age

# Output the result in the specified format
print(f"{years_till_120} years till 120")
```

## Challenge

⇨ Write a program that gets an input from the user, a number, 1 or 0.

⇨ The program will output "T" if the input is 1 and "F" otherwise.

⇨ Remember! you can cast the input to number using int()

## Solution

```py
num = int(input())

if num == 1:
  print("T")
elif num == 0:
  print("F")

