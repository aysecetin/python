# Output 🤓

- We have already seen how to output something but let's recap.

⇨ In programming it's often called "printing" to output something.

⇨ In Python to print something to the screen we use print()

***For example,***
```py
print("Hello")
```
The above example prints "Hello" to screen.

⇨ Recall that you must enclose what you want to print with "" or with '', it is a string inside the print().

## Output With Variables 

⇨ As of now we learned how to print simple strings, but sometimes we need to insert variables values into the string.

***For example:***

```py
age = 10
print("His age is: age")
```
- This will print "His age is: age" instead of "His age is: 10"
to make it work we will use the f string f"":

```py
age = 10
print(f"His age is: {age}")
```

- This prints "His age is: 10"

**Before the quotation marks "" we add the letter f and inside the string wherever we put parenthesis {} it will insert the value of what is written inside it.**
