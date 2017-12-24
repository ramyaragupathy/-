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

### Return statements

As soon as `return` is executed in a function, execution will leave that function. Every return is a possible exit from the function.

```
def cylinder_surface_area(radius, height, has_top_and_bottom):
    side_area = height * 6.28 * radius
    if has_top_and_bottom:
        top_area = 3.14 * radius ** 2
        return 2 * top_area + side_area
    else:
        return side_area
```

## Conditional Expression



![image](https://user-images.githubusercontent.com/12103383/34324299-893f8ccc-e893-11e7-9f93-cd992b17afcc.png)

(1) The if keyword indicates that this line is a conditional expression.</br>
(2) Following if is phone_balance < 10, the condition to be checked. This part is a boolean expression - an expression that evaluates to either True or False.</br>
(3) The conditional expression (or "if statement") ends with a colon.</br>
(4) This line is followed by an indented block of code, in this case:
```
 phone_balance += 10   
 bank_balance -= 10
 ```
This indented block of code will be executed if the boolean expression evaluates to True. If the boolean expression evaluates to False, the indented block will not be executed.

### if-elif-else
```
def garden_calendar(season):
    if season == "spring":
        print("time to plant the garden!")
    elif season == "summer":
        print("time to water the garden!")
    elif season == "autumn" or season == "fall":
        print("time to harvest the garden!")
    elif season == "winter":
        print("time to stay indoors and drink tea!")
    else:
        print("I don't recognize that season")
 ```
 
 The `else` keyword is always followed by a colon and doesn't need a boolean expression - it is simply what happens when the boolean expression from the if statement is False. `if` and `elif` statement always requires a conditional expression.
 
 
## Data Structures

### Lists
- zero based indexing: first element in the list is located at index 0 rather than index 1
- negative indexes: The index -1 refers to the last element of the list, -2 to the second to last, and so on.
- Slicing list


![image](https://user-images.githubusercontent.com/12103383/34324455-d4ea46ca-e899-11e7-8171-27572d08e544.png)
_end element excluded_

- `list` is a type, like `string`, `float` and `int`. Of the types we've seen, lists are most like strings: both types support indexing, slicing, the `len` function and the `in` operator. So, how are lists different from strings? The obvious difference is that strings are sequences of letters, while list elements can be any type of object. A more subtle difference is that lists can be modified, but strings can't be.

![image](https://user-images.githubusercontent.com/12103383/34324499-5ddf8ca0-e89b-11e7-97c9-690a8810bde8.png)

#### max(some_list)
Returns the greatest element of the list. How the greatest element is determined depends on what type objects are in the list. The maximum element in a list of numbers is the largest number.The maximum elements in a list of strings is element that would occur last of the list were sorted alphabetically.

This works because the the max function is defined in terms of >, the greater than comparison operator. The > operator is defined for many non-numeric types; if you're working with objects that can be compared with > then you can use max on a list of the objects. For strings the standard comparison is alphabetical, so the maximum of this list is the element that appears last alphabetically.

The max function is undefined for lists that contain elements from different, incomparable types:
```
>>> max([42, 'African Swallow'])
TypeError: unorderable types: str() > int()
```
This is because max is defined in terms of >. If two objects in the list can't be compared, the maximum element can't be determined.The maximum elements in a list of strings is element that would occur last of the list were sorted alphabetically.

This works because the the max function is defined in terms of >, the greater than comparison operator. The > operator is defined for many non-numeric types; if you're working with objects that can be compared with > then you can use max on a list of the objects. For strings the standard comparison is alphabetical, so the maximum of this list is the element that appears last alphabetically.

The max function is undefined for lists that contain elements from different, incomparable types:

>>> max([42, 'African Swallow'])
TypeError: unorderable types: str() > int()
This is because max is defined in terms of >. If two objects in the list can't be compared, the maximum element can't be determined.


#### Join

![image](https://user-images.githubusercontent.com/12103383/34324598-d41017a2-e89e-11e7-998f-9107567b1f56.png)


The join takes a list as an argument, and returns a string consisting of the list elements joined by a separator string. In this example we use the string \n as the separator so that there is a newline between each element.

We can also use other strings (instead of '\n') with .join For instance:
```
>>> names = ["García", "O'Kelly", "Davis"]
>>> "-".join(names)
"García-O'Kelly-Davis"
```

Also note thatjoin will trigger an error if we try to join anything other than strings. For example:
```
>>> stuff = ["thing", 42, "nope"]
>>> " and ".join(stuff)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: sequence item 1: expected str instance, int found
```

