
# indentation to enclose blocks of code

def print_greeting():
    print('Hello World!')
def cylinder_volume(height, radius):
    pi = 3.14159
    return height * pi * radius ** 2

print_greeting()
print(cylinder_volume(10, 3))

# todo: define a function named `population_density` that takes two arguments, 
# `population` and `land_area` (in square kilometres), and returns a population 
# density calculated from those values.


def population_density(population, area):
    density = population/area
    return density

# Here are test cases to verify that your function works as expected:
test1 = population_density(10, 1)
expected_result1 = 10
print("expected result: {}, actual result: {}".format(expected_result1, test1))

test2 = population_density(864816, 121.4)
expected_result2 = 7123.6902801
print("expected result: {}..., actual result: {}".format(expected_result2, test2))


def population_density(population, land_area):
    """Calculate the population density of an area.

    population: int. The population of the area
    land_area: int or float. This function is unit-agnostic, if you pass
               in values in terms of square km or square miles the
               function will return a density in those units.
    """
    return population / land_area

print(population_density(100,10))


def readable_timedelta(days):
    """Calculate the weekly split for a given number of days.
    
    days: int. Number of days for which the weekly split
          has to be calculated.
    """
    split_week = int(days/7)
    split_days = days % 7
    print_string = '{} week(s) and {} day(s)'.format(split_week, split_days)
    return print_string

print(readable_timedelta(10))
