# Use either type of quote to define strings. 
# concatenation
firstname = "Ramya"
lastname = "Ragupathy"
print(firstname + " " + lastname)

# escape characters
messiah = 'He\'s not the Messiah, he\'s a very naughty boy!'
print(messiah)

# string within string
pet_halibut = 'Why should I be tarred with the epithet "loony" merely because I have a pet halibut?'
print(pet_halibut)

# TODO: print a log message incorporating the strings above.
# The message should be use the same format as this one:
# "Yogesh accessed the site http://petshop.com/pets/reptiles/pythons at 16:20."
username = "Kinari"
timestamp = "04:50"
url = "http://petshop.com/pets/mammals/cats"
print(username + " accessed the site " + url + " at " + timestamp + ".")

# `len` function is similar to `print` in that we call it by passing a variable 
# as the argument inside of parentheses. `len` differs from `print` in that it 
# produces a value that can be stored in a variable. 

#todo: calculate how long this name is
given_name = "Charlotte"
middle_names = "Hippopotamus"
family_name = "Turner"

name_length = len(given_name +" "+ middle_names + " "+family_name)

driving_licence_character_limit = 28
print(name_length <= driving_licence_character_limit)

# Types & type conversions
mon_sales = "121"
tues_sales = "105"
wed_sales = "110"
thurs_sales = "98"
fri_sales = "95"

#TODO: Print a string with this format: This week's total sales: xxx

total_sales = int(mon_sales) + int(tues_sales)  + int(wed_sales) + int(thurs_sales) + int(fri_sales)
# Note that concatenation operator works only on strings
# print("This week's total sales: " + total_sales) will throw an error
# In JS you need ntoo worry about the type conversion
print("This week's total sales: " + str(total_sales))

# Operating on values using operators, functions, methods
# Methods are related to functions but unlike functions, 
# methods are associated with specific types of objects. 

# STRING METHODS
full_name = "ramya raGuPathy"

# object is a string with the value, "ramya raGuPathy", 
# and we are calling its `title` method. 
# The method returns a string in Title Case, 
# meaning that the first letter of each word is capitalized.
print(full_name.title())
# `islower` method inspects the string object it has been called with. 
# In this case the string object is ramya raGuPathy". 
# `islower` then returns a bool that indicates 
# whether the string object consists of lowercase letters.
print(full_name.islower())

## Vowel Count example

prophecy = "And there shall in that time be rumours of things going astray, and there will be a great confusion as to where things really are, and nobody will really know where lieth those little things with the sort of raffia work base, that has an attachment…at this time, a friend shall lose his friends’s hammer and the young shall not know where lieth the things possessed by their fathers that their fathers put there only just the night before around eight o’clock…"
vowel_count = 0

# TODO: set the value of vowel_count to be the number of vowels in prophecy

# convert the entire stirng to lower case
prophecy = prophecy.lower()
print(prophecy)
# `count` method returns how many times the substring occurs in a string
vowel_count += prophecy.count('a')
vowel_count += prophecy.count('e')
vowel_count += prophecy.count('i')
vowel_count += prophecy.count('o')
vowel_count += prophecy.count('u')

# Print the final count
print(vowel_count)
