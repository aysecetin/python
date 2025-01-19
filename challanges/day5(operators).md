# Logical Operators Part 1 

- Logical operators are used to check combinations of comparisons that return True or False.
 
- For example the following statement contains two comparisons: 
 
⇨ Is 5 greater than 3 and lesser than 6?

Operator | Meaning                              | Example
---------|--------------------------------------|-----------
and   	 |  And - True if all operands are True	| a and b
or	     |  Or - True if any operand is True	  |  a or b
not	     |  Not - True if the operand is False  | 	not a
 

- Let's see some examples,


⇨5 is bigger than 3 and 1 equals 1,

```py
b1 = (5 > 3) and (1 == 1) # holds true
```
**Explanation:** All of the operands are True, so b1 will hold True (and operation is True if both operands are True) .

 

⇨5 is not equals 4 or five equals 2,
```py
b2 = not 5 == 4 or 5 == 2 # holds true
```
**Explanation:** The first operand (5 != 4) is True so b2 is also True (or operation is True if either one of the operands is True)

 

⇨1 is not equals 1 or false,

```py
b3 = not 1 == 1 or False # holds false
```
**Explanation:** All of the operands are False, so b3 will hold False (or operation).

 

⇨not (3 bigger than 4),

```py
b4 = not (3 > 4) # holds true
```
**Explanation:** The operand is False, so b4 will hold True (not operation).

 

⇨not (5 bigger than 10 or 5 bigger than 1),

```py
b5 = not (5 > 10 or 5 > 1) # holds false
```
**Explanation:** 5 > 10 or 5 > 1 is True (one of the operands is True), so in total b5 is False (not operation).



## Challenge
- You are given a code, Replace the question marks of the variables b1 and b2 so that b3 holds True.

## Solution
```py
# Type your code below
b1 = True
b2 = False
b3 = b1 or b2
# Don't change the line below
print(f"b3 = {b3}")
```
