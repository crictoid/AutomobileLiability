# Mark Bulmer - CIS 115 - 6-23-2021
# Automobile liability insurance estimate program.

# Define intro for introduction page.
def intro():
    print('Hello and thanks for choosing Bulmer insurance!')
    print('We just have a few questions.')


def main():
    print('Hello and thanks for choosing Bulmer insurance!')
    print('We just have a few questions.')
intro()
# Ask for customer name.
name = input('Please enter your name: ')
# Ask customer age.
age = int(input('Please enter your age: '))
# Ask for number of traffic violations.
vio = int(input('Number of traffic violations: '))


# Set limits for valid and invalid age responses.
def invalid():
    if age < 16 or age > 105:
        True
        print('Invalid Entry: Age Out of Range')
    elif age >= 16 or age <= 105:
        False
        print('We appreciate your interest.')

        
# Define risk level and risk type.
if vio >= 4:
    risk = 1
    risktype = 'high'
elif vio == 3:
    risk = 2
    risktype = 'moderate'
elif vio == 2:
     risk = 2
     risktype = 'moderate'
elif vio == 1:
     risk = 3
     risktype = 'low'
elif vio == 0:
     risk = 4
     risktype = 'no'

     
# Determine pricing policy based on age and violations.
if vio >= 4 and age < 25:
    price = 480
elif vio >= 4 and age >= 25:
    price = 410
elif vio == 3 and age < 25:
    price = 450
elif vio == 3 and age >= 25:
    price = 390
elif vio == 2 and age < 25:
    price = 405
elif vio == 2 and age >= 25:
    price = 365
elif vio == 1 and age < 25:
    price = 380
elif vio == 1 and age >= 25:
    price = 315
elif vio == 0 and age < 25:
    price = 325
elif vio == 0 and age >= 25:
    price = 275


# Display the quote to the customer.
print(name,', as a', risktype,'risk driver, your insurance will cost: $', price)        
