#Use either type of quote to define strings. 
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
