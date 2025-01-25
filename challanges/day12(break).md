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
 
