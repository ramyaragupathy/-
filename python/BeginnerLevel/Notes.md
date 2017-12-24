## Variables

![image](https://user-images.githubusercontent.com/12103383/34285713-b1137828-e701-11e7-8cfe-2ad594697351.png)

## Print

`print` is a built-in function in Python, and you’ll come across more of those later on. Function calls in Python always have a pair of parentheses attached, and if there are any arguments, they go inside the parentheses. So the print function syntax requires a set of parentheses and the argument is put inside the parentheses. As you’ve already seen, if you put a variable here, the thing that gets printed is the value of that variable, not the variable name.

Note: in Python 2, users didn’t need to use parentheses for printing, but in Python 3 they are required, so don’t miss them!

```
>>> print manila_pop
  File "<stdin>", line 1
    print manila_pop
                    ^
```                    
           
`SyntaxError: Missing parentheses in call to 'print'`


## Functions

![image](https://user-images.githubusercontent.com/12103383/34293031-19bf0d66-e729-11e7-81e0-0994b59a4fb8.png)

### Function Header
(1) The def keyword indicates that the code that follows is a function definition.</br>
(2) Following def is the name of the function, in this case cylinder_volume. This needs to be one word, with no gaps - that's why this one has an underscore.</br>
(3) The first line of a function definition has one final element, the arguments the function expects (the rules for function names are the same as the rules for variable names). The arguments of a function are values passed in when the function is called; they are used in the body of the function. The arguments are separated by commas and placed in a pair of parentheses. If you write a function that doesn't take arguments, then use an empty pair of parentheses, (). The first line of the function definition ends with a colon, :.
### Function Body
(4) The body of the function is indented by four spaces. The function body is where the function does its work. In the body we can refer to the argument variables and define new variables. The pi variable that we define here is a local variable, meaning that it can only be used within the body of the cylinder_volume function. Attempting to access the variable anywhere else would cause an error. </br>
(5) The return keyword is used to get results out of the function. The value of the expression that follows return is the output of the function. </br>
(6) In this example we return the value of an expression, the formula for the volume of a cylinder. Note that radius ** 2 is calculated before the rest of the expression because exponentiation comes before multiplication in the mathematical order of operations. (That said, it never hurts to add a pair of extra brackets- especially in expressions involving a lot of mathematical operations, where it can become confusing which operation is performed first. Returning height * pi * (radius ** 2) would have been just fine.) Rather than returning the value as it is calculated, an alternative technique would be to calculate the volume earlier in the function body, and then store it in a variable named volume. That would allow us to return volume. </br>

There is one further technique for making functions more readable, **documentation strings (also called "docstrings")**. Docstrings are a type of comment used to explain the purpose of a function, and how it should be used.

Docstrings are surrounded by triple quotes, """. The first line of the docstring is a brief explanation of the function's purpose. If you feel that this is sufficient documentation you can end the docstring at this point, single line docstrings are perfectly acceptable. If you think that the function is complicated enough to warrant a longer description, you can add a more thorough paragraph after the one line summary.

The next element of a docstring is an explanation of the function's arguments. Here you list the arguments, state their purpose, and what types the arguments should be. A more thorough explanation of docstring conventions at https://www.python.org/dev/peps/pep-0257/.

## Conditional Expression



![image](https://user-images.githubusercontent.com/12103383/34324299-893f8ccc-e893-11e7-9f93-cd992b17afcc.png)

(1) The if keyword indicates that this line is a conditional expression.
(2) Following if is phone_balance < 10, the condition to be checked. This part is a boolean expression - an expression that evaluates to either True or False.
(3) The conditional expression (or "if statement") ends with a colon.
(4) This line is followed by an indented block of code, in this case:
```
 phone_balance += 10   
 bank_balance -= 10
 ```
This indented block of code will be executed if the boolean expression evaluates to True. If the boolean expression evaluates to False, the indented block will not be executed.
