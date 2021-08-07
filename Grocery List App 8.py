# Hello, In the 8th challenge we create Grocery list app
import datetime
# Create the datetime object and store the current date and time
time = datetime.datetime.now()
month = str(time.month)
day = str(time.day)
hour = str(time.hour)
minute = str(time.minute)
# Welcome message
foods = ["Meat", "Cheese"]
print("Welcome To The Grocery List App")
print("Current Date and Time: " + month + "/" + day + "  " +hour+ "." + minute)
print("You Currently have " + foods[0] + " and " + foods[1] + " in your list.")

# Get user input
food = input("\nType of food add to the Grocery List:")
foods.append(food.title())
food = input("\nType of food add to the Grocery List:")
foods.append(food.title())
food = input("\nType of food add to the Grocery List:")
foods.append(food.title())

# print and sort the list
print("\nHere is the your Grocery List:")
print(foods)
foods.sort()
print("Here is your Grocery List Sorted: ")
print(foods)
# Simulate Shopping

print("\nSimulating grocery shopping...")
print("\nCurrent grocery list: " + str(len(foods)) + " items")
print(foods)
buy_food = input("What food did you just buy: ").title()
str(foods.remove(buy_food))
print("Removing " + buy_food + " from the list...")

print("\nSimulating grocery shopping...")
print("\nCurrent grocery list: " + str(len(foods)) + " items")
print(foods)
buy_food = input("What food did you just buy: ").title()
foods.remove(buy_food)
print("Removing " + buy_food + " from the list...")

print("\nSimulating grocery shopping...")
print("\nCurrent grocery list: " + str(len(foods)) + " items")
print(foods)
buy_food = input("What food did you just buy: ").title()
str(foods.remove(buy_food))
print("Removing " + buy_food + " from the list...")

# the store is out of item
print("\nCurrent grocery list: " + str(len(foods)) + " items")
print(foods)
no_item = foods.pop()
print("\nSorry, the store is out of " + no_item + ".")
new_food = input("What food would you like instead: ").title()
foods.insert(0, new_food)

print("\nHere is what remains on your grocery list: ")
print(foods)
