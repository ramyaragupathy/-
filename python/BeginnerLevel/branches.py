#First Example - uncomment lines or change values to test the code
phone_balance = 7.62
bank_balance = 104.39
#phone_balance = 12.34
#bank_balance = 25
if phone_balance < 10:
    phone_balance += 10
    bank_balance -= 10
print(phone_balance)
print(bank_balance)

#Second Example

#change the number to experiment!
number = 145346334
#number = 5 #3 sir
if number % 2 == 0:
    print("The number " + str(number) + " is even.")
else:
    print("The number " + str(number) + " is odd.")

#Third Example 

#change the age to experiment with the pricing
age = 35

#set the age limits for bus fares
free_up_to_age = 4
child_up_to_age = 18
senior_from_age = 65

#set bus fares
concession_ticket = 1.25
adult_ticket = 2.50

#ticket price logic
if age <= free_up_to_age:
    ticket_price = 0
elif age <= child_up_to_age:
    ticket_price = concession_ticket
elif age >= senior_from_age:
    ticket_price = concession_ticket
else:
    ticket_price = adult_ticket
message = "Somebody who is {} years old will pay ${} to ride the bus.".format(age,ticket_price)
print(message)

def which_prize(points):
    """Prize logic based on points earned

	points: int, points earned by a member in the game

	"""
    if (points <= 50):
        return ("Congratulations! You have won a wooden rabbit!")
    elif (points <=150):
        return ("Oh dear, no prize this time.")
    elif (points <=180):
        return ("Congratulations! You have won a wafer-thin mint!")
    else:
        return ("Congratulations! You have won a penguin!")
        


print(which_prize(75))


def which_prize2(points):
    """
    Returns the number of prize-winning message, given a number of points
    """
    prize = None
    if points <= 50:
        prize = "a wooden rabbit"
    elif 151 <= points <= 180:
        prize = "a wafer-thin mint"
    elif points >= 181:
        prize = "a penguin"

    # Using truth value of prize object in boolean expression
    if prize:
        return "Congratulations! You have won " + prize + "!"
    else:
        return "Oh dear, no prize this time."


print(which_prize2(200))
