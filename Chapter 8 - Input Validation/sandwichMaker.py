#!python3
import pyinputplus as pyip, re

print("Please input your sandwich preferences")
prices = {'White': 1.00, 'Brown': 1.25, 'Sourdough': 1.50, 'Whole Wheat': 2.00, 'Chicken': 1.50, 'Turkey': 2.00, 'Ham': 0.50, 'Tofu': 2.00,
          'Cheddar': 0.50, 'Swiss': 0.75, 'Mozzarella': 1.00, 'Mayo': 0.10, 'Mustard': 0.1, 
          'lettuce': 0.15, 'Tomato': 0.10}

while True:
    try:
        totalCost = 0.00
        sandwich = {}
        sandwich['Bread'] = pyip.inputMenu(['White', 'Brown', 'Sourdough', 'Whole Wheat'], numbered=True)
        sandwich['Protein'] = pyip.inputMenu(['Chicken', 'Turkey', 'Ham', 'Tofu'], numbered=True)
        promptCheese = pyip.inputYesNo("Would you like Cheese, yes or no?")
        
        if promptCheese:
            sandwich['Cheese'] = pyip.inputMenu(['Cheddar', 'Swiss', 'Mozzarella'], numbered=True)
        
        promptDressing = pyip.inputYesNo('Would you like mayo, lettuce or tomato?')
        if promptDressing:
            sandwich['Side'] = pyip.inputMenu(["Mayo", "Mustard", "Lettuce", "Tomato"], numbered=True)
        
        orderNumber = pyip.inputInt('How many of these sandwiches would you like?', max=99, min=1)
        
        for choice in sandwich:
            if sandwich[choice] in prices.keys():
                totalCost += prices[sandwich[choice]]
        totalCost *= orderNumber
        print("Ok, that'll be $" + "{:.2f}".format(totalCost) + " please!")
        break
    except:
        break