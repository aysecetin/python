# For Loop

- Sometimes when programming it's necessary to perform same or almost the same operation a couple of times.

- To prevent writing the same thing over and over again we can use Loops.

- The for loop has the following syntax

```py
for i in range(start, end):
    code
```
- The range(start, end) determines what is the start value and what is the end value. The i will receive all values from start to end (not including end) sequentially. For example:

```py
for i in range(0, 5):
    print(i)
```
- It will execute the print statement 5 times:
```py
0
1
2
3
4
```
- We can simplify the range(0, 5) to range(5):

```py
for i in range(5):
    print(i)
 ```

- Loops have many use cases, For example let's sum all the number from 1 to 100:

```py
sum_numbers = 0
for i in range(1, 101):
    sum_numbers += i
print(sum_numbers)
```
- This will first loop through all numbers between 1 to 101 (not including 101) and sum all of them, Then it will print the sum_numbers variable

## Challange 

- Write a program that prints "Hello Coddy: " and the i value from 3 to 27 (including, 25 times in total), do it using a for loop.

- It will look like this:
```py
Hello Coddy: 3
Hello Coddy: 4
...
Hello Coddy: 27
```

## Solution

```py
for i in range (3,28)
    print("Hello Coddy:",i)
```

# While Loop

- A while loop is different from the for loop. A for loop allows us to iterate over a specific range, whereas a while loop allows us to keep iterating as long as a certain condition is met.

- To use a while loop write:
```py
while condition:
    code
```
- The code will execute only if the condition is True.

- There are many use cases where a while would solve the problem, but the for loop would not.

- For example consider this problem:

- Find the smallest power of 2 that is greater than a given number.

- To solve it we will use a while loop that will repeatedly multiply the current power of 2 by 2 until it becomes greater than the given number:

```py
number = 27
power_of_two = 1

while power_of_two <= number:
    power_of_two *= 2

print(power_of_two)
```
## Challange

- Write a program that gets one input, float number.

- Use a while loop to divide the input by 2 as long as the number is bigger or equal to 3.5.

- Print the first number that is smaller than 3.5.

``py
# Get input from the user
number = float(input())

# Continue dividing by 2 as long as the number is >= 3.5
while number >= 3.5:
    number /= 2

# Print the first number smaller than 3.5
print(number)



