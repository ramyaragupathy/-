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
<br>
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
</br>
This is because max is defined in terms of >. If two objects in the list can't be compared, the maximum element can't be determined.The maximum elements in a list of strings is element that would occur last of the list were sorted alphabetically.

This works because the the max function is defined in terms of >, the greater than comparison operator. The > operator is defined for many non-numeric types; if you're working with objects that can be compared with > then you can use max on a list of the objects. For strings the standard comparison is alphabetical, so the maximum of this list is the element that appears last alphabetically.

The max function is undefined for lists that contain elements from different, incomparable types:

```
>>> max([42, 'African Swallow'])
TypeError: unorderable types: str() > int()
```
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

#### Sorting

Use `list.sort()` when you want to mutate the list, `sorted()` when you want a new sorted object back.

```
python_varieties = ['Burmese Python', 'African Rock Python', 'Ball Python', 'Reticulated Python', 'Angolan Python']
print(sorted(python_varieties,reverse=True)) # Returns a new list
python_varieties.sort() # Mutates the existing list
```

### Sets
Python includes several data structures other than lists for storing collections, and one of them is perfectly suited for storing unique elements: sets.

Sets are collections of unique elements without any particular ordering. We can create a set from a list like this:
```
>>> country_set = set(countries)
>>> len(country_set)
196
```

You can add elements to sets, but you don't use the append method like lists, instead sets have the add method:

`country_set.add("Florin")`
Sets also have a pop method, just like lists. When you pop an element from a set a random element is removed (remember that sets, unlike lists, are unordered so there is no "last element").

You can iterate over a set using a for loop in the same manner that you can iterate over a list.

We iterate over sets like this:
```
>>> colors = set(['Pthalo Blue', 'Indian Yellow', 'Sap Green'])
>>> for color in colors:
...    print(color)
...
Indian Yellow
Sap Green
Pthalo Blue
```
Notice that the for loop didn't print the colors in the same order they were inserted into the set. Sets don't track ordering the way lists do, so iterating over them produces values in an arbitrary order. Sets are not sortable but they are mutable.

### Dictionaries

Rather than storing single objects like lists and sets do, dictionaries store pairs of elements: keys and values. In this example we define a dictionary where the keys are element names and the values are their corresponding atomic numbers.

`elements = {'hydrogen': 1, 'helium': 2, 'carbon': 6}` <br>
We can look up values in the dictionary using square brackets enclosing a key:<br>
```
>>> print(elements['carbon'])
6
```
<br>

We can also insert new values into the dictionary with square brackets:<br>

```
>>> elements['lithium'] = 3
>>> print(elements['lithium'])
3
```
<br>
Dictionary keys are similar to list indices: we can select elements from the data structure by putting the index/key in square brackets. Unlike lists, dictionaries can have keys of any immutable type, not just integers. The element dictionary uses strings for its keys. However, it's not even necessary for every key to have the same type!

We can check whether a value is in a dictionary on the same way we check whether a value is in a list or set with the `in` keyword.
<br>
```
if 'mithril' in elements:
    print("That's a real element!")
else:
    print("There's no such element!")
```
<br>
Dicts have a related method that's also useful, `get`. `get` looks up values in a dictionary, but unlike square brackets, `get` returns `None` (or a default value of your choice) if the key isn't found. If you expect lookups to sometimes fail, get might be a better tool than normal square bracket lookups.<br>

```
>>> elements.get('dilithium')
None
>>> elements['dilithium']
KeyError: 'dilithium'
>>> elements.get('kryptonite', 'There\'s no such element!')
"There's no such element!"
```
<br>
Dicts store key value pairs, and when we loop over them we iterate through the keys:
<br>

```
Beatles_Discography = {"Please Please Me": 1963, "With the Beatles": 1963, 
    "A Hard Day's Night": 1964, "Beatles for Sale": 1964, "Twist and Shout": 1964,
    "Help": 1965, "Rubber Soul": 1965, "Revolver": 1966,
    "Sgt. Pepper's Lonely Hearts Club Band": 1967,
    "Magical Mystery Tour": 1967, "The Beatles": 1968,
    "Yellow Submarine": 1969 ,'Abbey Road': 1969,
    "Let It Be": 1970}

for album_title in Beatles_Discography:
    print("title: {}, year: {}".format(album_title, Beatles_Discography[album_title]))

```
<br>

We can use the key album_title to get to each value in the the dict: Beatles_Discography[album_title].

#### A Dictionary of Dictionaries
Let's revisit the elements dictionary,

`elements = {'hydrogen': 1, 'helium': 2, 'carbon': 6}` 
<br>

This dictionary maps element names (strings) to their atomic numbers (ints). But what if we wanted to store more information about each element, like their weight and symbol? We can do that by adjusting the dictionary so that it maps element names (strings) to a dictionary that stores that collection of data:
<br>
```
elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H'},
            'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He'}}
```
<br>
We can look the information about an entry in this nested dictionary in the same ways we did before, with square brackets or the get method:
<br>
```
>>> print(elements['helium'])
{'number': 2, 'symbol': 'He', 'weight': 4.002602}
>>> print(elements.get('unobtainium', 'There\'s no such element!'))
There's no such element!
```
<br>
We can look up specific information from the helium dictionary like this:
<br>
```
>>> print(elements['helium']['weight'])
4.002602
```
<br>
This code is first looking up the key "helium" in the elements dictionary, producing the helium dictionary. The second lookup, ['weight'] then looks up the "weight" key in that helium dictionary to find helium's atomic weight.

### Tuples

Python provides another useful built-in type: tuples. Tuples are used to store related pieces of information. Consider this example involving latitude and longitude:
<br>
```
>>> AngkorWat = (13.4125, 103.866667)
>>> print(type(AngkorWat))
<class 'tuple'>
>>> print("Angkor Wat is at latitude: {}".format(AngkorWat[0]))
Angkor Wat is at latitude: 13.4125
>>> print("Angkor Wat is at longitude: {}".format(AngkorWat[1]))
Angkor Wat is at longitude: 103.866667
```
<br>
Tuples are similar to lists in that they store an ordered collection of objects which can be accessed by their indexes (for example AngkorWat[0] and AngkorWat[1]). Unlike lists, tuples are immutable. You can't add and remove items from tuples, or sort them in place.

#### Why Tuples?
Why do we have tuples if they're like lists with less features? Tuples useful when you have two or more values that are so closely related that they will always be used together, like latitude and longitude coordinates.

Tuples can be used to assign multiple variables in a compact way:
<br>
```
>>> dimensions = 52, 40, 100 
>>> length, width, height = dimensions 
>>> print("The dimensions are {}x{}x{}".format(length, width, height))
The dimensions are 52x40x100

```
<br>
Notice that the values assigned to the tuple dimensions aren't surrounded with parentheses as previous examples were. The parentheses are optional when making tuples, and programmers frequently omit them if parentheses don't clarify the code.

#### Tuple Unpacking
In the second line, three variables are assigned from the content of the tuple dimensions. This is called tuple unpacking. You can use tuple unpacking to assign the information from a tuple into multiple variables without having to access them one by one and make multiple assignment statements.

In this example, if we won't need to use dimensions directly, we could shorten those two lines of code into a single line that assigns three variables in one go! 
<br>

`length, width, height = 52, 40, 100`

## Loops

### For loop

![image](https://user-images.githubusercontent.com/12103383/34332666-8e47452c-e959-11e7-828a-435d33cd6965.png)

(1) The for keyword signals that this is a for loop.</br>
(2) The rest of the line specifies what we're iterating over. names is the list that this for loop iterates over. name is this loop's iteration variable. The body of the for loop will be executed once for each element in names, and the iteration variable name can be used in the loop's body to refer to the element that the loop is currently processing.</br>
(3) The body of a for loop is indented four spaces, and is run once for each element in the list.</br>
A note about naming You can name iteration variables however you like. This example demonstrates a common pattern though, the list names has a plural name ending in "s", and the iteration variable is the singular word with no "s". Naming lists and iteration variables in this style makes it easier for other programmers to understand what the different variables are for.

### While loop

For loops are an example of "definite iteration" meaning that the loop's body is run a predefined number of times. A for loop over a list executes the body once for each element in the list. A for loop using the range function will execute the number of times specified by the range function call. This differs from "indefinite iteration" which is when a loop repeats an unknown number of times and ends when some condition is met.

![image](https://user-images.githubusercontent.com/12103383/34333197-fb082f54-e95f-11e7-9027-6d28e07efae9.png)


(1) The while keyword indicates that this is a while loop <br>
(2) Next is a test expression, in this example sum(hand) <= 21. If this expression is true, the loop's body will be executed. The test expression is evaluated again after the loop's body runs. This process of checking the test expression and running the loop repeats until the expression becomes false. <br>
(3) The loop's body is indented with four spaces. The loop's body should somehow modify one of the variables in the test expression. If the value of the test expression never changes, the result is an infinite loop! In this example the loop's body appends numbers to the hand list, which increases the value of sum(hand). <br>

## Variable Scope

While in many or most other programming languages variables are treated as global if not otherwise declared, Python deals with variables the other way around. They are local, if not otherwise declared. when you define variables inside a function definition, they are local to this function by default. This means that anything you will do to such a variable in the body of the function will have no effect on other variables outside of the function, even if they have the same name. This means that the function body is the scope of such a variable, i.e. the enclosing context where this name with its values is associated. 

All variables have the scope of the block, where they are declared and defined in. They can only be used after the point of their declaration. 
<br>
```
egg_count = 0

def buy_eggs():
    egg_count += 12 # purchase a dozen eggs

buy_eggs()
```
<br>

This function will throw an `UnboundLocalError`. Python doesn't allow functions to modify variables that aren't in the function's scope.
