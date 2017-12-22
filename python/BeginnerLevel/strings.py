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
