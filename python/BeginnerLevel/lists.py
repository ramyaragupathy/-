python_versions = [1.0, 1.5, 1.6, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6]
print(python_versions[-1])

def how_many_days(month_number):
    """Returns the number of days in a month.
    WARNING: This function doesn't account for leap years!
    """
    days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
    return days_in_month[month_number-1]
   
    
# This test case should print 31, the number of days in the eighth month, August
print(how_many_days(8))

# SLICING

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
q3 = months[6:9]
print(q3)

first_half = months[:6]
second_half = months[6:]
print(first_half)
print(second_half)

# Lists, Strings, and Mutability
sample_string = "And Now For Something Completely Different"
sample_list = ['Graham', 'John', 'Terry', 'Eric', 'Terry', 'Michael']
print(sample_string[4]) # 'N'
print(sample_list[4]) # 'Terry'
print(sample_string[12:21]) # 'Something'
print(sample_list[2:4]) # ['Terry', 'Eric']
print(len(sample_string)) # 42
print(len(sample_list)) # 6
print('thing' in sample_string) # True
print('Rowan' in sample_list) # False
sample_list[3] = "Ramya"
sample_list[0:2] = ["Krish","Sakthi"] #slicing plus assignmnet happening simultaneously
# sample_string[3] = "R" error
print(sample_list)

name = "Old Woman"
person = name
name = "Dennis"
print(name) # Dennis
print(person) # Old Woman
dish = ["Spam", "Spam", "Spam", "Spam", "Spam", "Spam", "baked beans", "Spam", "Spam", "Spam", "Spam"]
mr_buns_order = dish
print(dish)
print(mr_buns_order)
dish[6] = "Spam" #baked beans are off
print(mr_buns_order) # ['Spam', 'Spam', 'Spam', 'Spam', 'Spam', 'Spam', 'Spam', 'Spam', 'Spam', 'Spam', 'Spam']
print(dish) # ['Spam', 'Spam', 'Spam', 'Spam', 'Spam', 'Spam', 'Spam', 'Spam', 'Spam', 'Spam', 'Spam']

# Working with lists

# Length
print(len(sample_list))

# Maximum values
batch_sizes = [15, 6, 89, 34, 65, 35]
print(max(batch_sizes))
python_varieties = ['Burmese Python', 'African Rock Python', 'Ball Python', 'Reticulated Python', 'Angolan Python']
print(max(python_varieties)) #Alphabetical sorting

# Minimum values
print(min(batch_sizes))
print(min(python_varieties))

# Sorting
print(sorted(batch_sizes))
print(batch_sizes[0]) #sorting does not alter the list index,  15 is still the first element
print(sorted(python_varieties,reverse=True)) # sorting in descending order
python_varieties.sort() # affects index
print(python_varieties[0])


# Appending elements to the list
python_varieties.append('Blood Python')
print(python_varieties)


# String method: Join, works only on string lists
nautical_directions = "\n".join(["fore", "aft", "starboard", "port"])
print(nautical_directions)

def median(numbers):
    numbers.sort() #The sort method sorts a list directly, rather than returning a new sorted list
    if len(numbers)%2 == 0:
        return((numbers[len(numbers)//2] + numbers[(len(numbers)//2) -1])/2)
    else:
    
        middle_index = len(numbers)//2
        return numbers[middle_index]

test1 = median([1,2,3])
print("expected result: 2, actual result: {}".format(test1))

test2 = median([1,2,3,4])
print("expected result: 2.5, actual result: {}".format(test2))

test3 = median([53, 12, 65, 7, 420, 317, 88])
print("expected result: 65, actual result: {}".format(test3))


