# Break

- The break statement stops the loop instantly when it's encountered.

**For example,**

```py
for i in range(10): 
    if i == 6:
        break
    print(i)
```

- In the following example the loop iterates regularly until it reaches number 6. Then the program enters the if statement and executes the break statement. This exits the loop immediately. The output is:
```py
0
1
2
3
4
5
```

## Challenge

- You are given a code that prints the numbers from 1 to 10 (including).
  
- Your task is to add if and break statements so that only the numbers from 1 to 5 will be printed, the loop will exit before printing the numbers from 6 to 10.

## Solution
```py
for i in range(1, 11):
    if i == 6:
        break
    print(i)
```
 
# Continue

- The continue statement stops the current iteration and continues to the next iteration. For example:

for i in range(3, 9):
    if i == 5:
        continue
    print(i)
The loop will iterate through all of the numbers. when it will reaches i=5 it will skip that iteration and continue to the next one. The output is:
```py
3
4
6
7
8
```
- Notice, number 5 is not in the output.

## Challenge

- You are given a code which prints the numbers from 1 to 20 (including).

- Your task is to add if and continue statements so that only the even numbers will be printed (2, 4, 6, ...). 

```py
for i in range(2, 21,):
    if i % 2 == 1:
        continue
    print(i)
```
**Output**
```
2
4
6
8
10
12
14
16
18
20
```
## Recap Challenge #1

- Factorial is a mathematical operation.

- Factorial of n is the product of all positive integers less than or equal to n.

**Examples,**

○ Factorial of 3: 6 = 1 * 2 * 3

○ Factorial of 6: 720 = 1 * 2 * 3 * 4 * 5 * 6

○ Factorial of 2: 2 = 1 * 2


## Challenge

- Write a program that receives one input, an integer, calculates the factorial of the input and prints it.

- For example, for input 5, the output should be 120 because 1 * 2 * 3 * 4  * 5 = 120.

## Solution 

```py
# Factorial Calculation
num = 5  # Example number
res = 1  # Initialize the result

for i in range(1, num + 1):
    res *= i  # Multiply res by i in each iteration

# Print the result after the loop
print(res)
```
