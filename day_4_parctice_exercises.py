'''BASIC IF-ELSE:  Write a program that checks if a number is even or odd.
Get Input: Ask the user to input a number. Use int(input()) to ensure it’s treated as an integer.
'''
number = int(input("Please provide the input number : "))
if number % 2 == 0 :
    print(f"given number {number} is evern")
else :
    print(f"given number {number} is odd")

'''
- IF-ELIF-ELSE CHAIN: Write a program that categorizes temperature as “Cold,” “Warm,” or “Hot.”
- Get Input: Ask the user to input the temperature in Celsius or Farenheit 
- Set Up the Conditions:
    Use if to check if the temperature is less than 15. If true, it’s “Cold.”
    Use elif to check if the temperature is between 15 and 25. If true, it’s “Warm.”
    Use else to categorize temperatures above 25 as “Hot.”
'''
temperature = int(input("Please provide temperature in Celsius : "))
if temperature < 15 :
    print("now the temperature is cold")
elif temperature >=15 and temperature <= 25 :
    print("now the temperature is warm")
else :
    print("now the temperature is Hot")

'''
1. NESTED CONDITIONALS: Write a program that checks if a person is eligible to vote in an election. They must be 18 years or older and a citizen of the country.
	1. Get Input:
		§ Ask the user to input their age
		                        age = int(input("Enter your age: "))
		§ Ask if they are a citizen 
		                        citizenship = input("Are you a citizen? (yes/no): ").lower()
	2. First Conditional (Age Check):  Use if to check if the age is 18 or older. If this is true, move to the next condition.
	3. Nested Conditional (Citizenship Check):
		§  Inside the first if that checks for age,  use another if to check if they answered “yes” to being a citizen. If true, print “Eligible to vote.”
		§ Add the else inside this nested conditional to print “Not eligible: Must be a citizen.”
Outer Else Statement: Add the matching else to the first condition (age check) to print “Not eligible: Must be 18 or older.
'''

age = int(input("Enter your age: "))

if age >= 18 :
    citizenship = input("Are you a citizen? (yes/no): ").lower()
    if citizenship == "yes" :
        print("You are Eligible to vote")
    else :
        print("Your are Not eligible: Must be a citizen")
else :
    print("Not eligible: Must be 18 or older")

'''
Basic for Loop: Create a for loop that prints each item in a list of groceries.
While Loop with User Input: Write a program that lets the user add items to a grocery list until they type "done."
'''
groceries = ["milk", "bread", "eggs", "cheese"]
for i in groceries:
    print(i)

groceries_list = []
user_input = input("Please add items to your grocery list (type 'done' to finish): ").lower()
while user_input != "done" :
	groceries_list.append(user_input)
	user_input = input("Please add items to your grocery list (type 'done' to finish): ").lower()
print("Your grocery list:", groceries_list)

'''
Loop through a Dictionary: Using a grocery list with item details, loop through and print each item’s name and total cost.
'''
grocery_dict = {
	"milk": {"quantity": 2, "price_per_unit": 1.50}, 
	"bread": {"quantity": 1, "price_per_unit": 2.00},
	"eggs": {"quantity": 12, "price_per_unit": 0.10},
	"cheese": {"quantity": 1, "price_per_unit": 3.00}
}

for item_name, item_details in grocery_dict.items() :
	total_cost = item_details["quantity"] * item_details["price_per_unit"]
	print(f"item name {item_name.capitalize()} , total quntity is : {item_details["quantity"]} and total cost {total_cost:.2f}")

'''
Using Break: Write a loop that stops when a specific item is found in a list.
Using Continue: Create a loop that skips specific items (e.g., non-fruit items) in a grocery list.
Using Pass: Write a loop that uses pass for an item to act as a placeholder for future code.
'''

count = 0

items_list = ["Gold","Silver","Iron"]
for i in items_list:
    count += 1
    if i == "Silver" :
        break
print(f"item Silver found at position : {count}")


non_fruit = ["glass","car", "bed"]
item_to_buy = ["mango", "banana", "glass", "pinapple", "car","apple"]
for fruit in item_to_buy :
    if fruit in non_fruit :
        continue
    print(f"fruit name : {fruit}")
    

animal_list = ["cat", "dog", "bird", "monkey"]
for animal in animal_list :
    if animal == "dog" :
        pass
    print(f"Animal name : {animal}")


'''
 If input is a number
Enter a number: 42 

You entered the number: 42.0
# If input is NOT a number:
Enter a number: abc
Error: Please enter a valid number.
'''

try :
	request_input = int(input("Please provide the number :"))
	print(f"You entered the number: {request_input:.2f}")
except (ValueError, TypeError) as e :
	print("Error: Please enter a valid number")


a = 10
b = 5

# Step 1: Attempt to double the value of 'b' by assigning it to 'double_b'
double_b = b * int("2")

# Step 2: Try to add 'a' and 'double_b' and store the result in 'total'
total = a + double_b

print("The total is:", total)



'''
EXERCISE 1 : 
You are building a grocery app that needs to categorize items into food and non-food categories. Write a script that takes a grocery item as input and uses if, elif, and else statements to print whether the item is food item or household item.
Ask the user to input a grocery item
Use conditional statements (if, elif, else) to categorize the item as either food or non-food
Example food items: 
food_items = ["apple", "bread", "milk"]
Example non-food items: 
non_food_items = ["soap", "detergent", "paper towels"]
Use food and non food items unique to you
If the item doesn’t match any category, print “Unknown item”

'''


food_items = ["rice", "chicken", "eggs", "cheese", "vegetables"]
non_food_items = ["toothpaste", "shampoo", "trash bags", "dish soap", "tissues"]

user_input = input("please provide the grocery item name : ")
if user_input in food_items:
    print(f"{user_input} is a food item")
elif user_input in non_food_items :
    print(f"{user_input} is a household item")
else :
    print(f"{user_input} is Unknown item")

'''
EXERCISE 2

You want to make burgers and fries for you and your friends, but you only have $27.50. Let’s see if we can make burgers and fries with our budget.
From the given list of dictionaries:
	1. Create a variable called shopping_list that stores an empty list:
	2. Create a variable called budget that stores our budget
	3. Create a variable called total_cost with the value of zero
	4. Create a variable called index that will store the current index starting from 0
	5. Create a while loop that runs while the total cost is less than or equal to the budget
	6. Under the while loop create a variable called item that gets the item at the current index from the items_list
	7. Add the item name to the shopping list
	8. Add the item cost to the total cost by calculating the cost multiplied by the amount
	9. Add one to the index
Outside of the while loop, print the shopping list
'''
shopping_list = []
our_budget = 27.50
total_cost = 0.00
index = 0

items_list = [
    {"name": "fries", "cost":6.25, "amount": 1},
    {"name": "burger patties", "cost":13.50, "amount": 1},
    {"name": "burger buns", "cost":3.50, "amount": 2},
    {"name": "tomato", "cost":1.50, "amount": 2},
    {"name": "lettuce", "cost":5, "amount": 1},
    {"name": "Ketchup", "cost":3.47, "amount": 1},
    {"name": "pickles", "cost":4.25, "amount": 1}
]

while int(total_cost) <= our_budget and index < len(items_list) :
    #print(f"present total cost : {total_cost}, present budget {our_budget}")
    item = items_list[index]
    shopping_list.append(item["name"])
    total_cost = total_cost + (item["cost"] * item["amount"])
    index += 1
print("out shoping list : ", shopping_list)



'''
EXERCISE 3: Extending Logic with Nesting
We want to know more information about how this script is working. Using your burger making script:
	1. After we add to the index, create a for loop that prints each item in the shopping list:
After and outside of the for loop print ten dashes "----------"
'''

shopping_list = []
our_budget = 27.50
total_cost = 0.00
index = 0

items_list = [
    {"name": "fries", "cost":6.25, "amount": 1},
    {"name": "burger patties", "cost":13.50, "amount": 1},
    {"name": "burger buns", "cost":3.50, "amount": 2},
    {"name": "tomato", "cost":1.50, "amount": 2},
    {"name": "lettuce", "cost":5, "amount": 1},
    {"name": "Ketchup", "cost":3.47, "amount": 1},
    {"name": "pickles", "cost":4.25, "amount": 1}
]

while total_cost <= our_budget : #and index < len(items_list) :
    #print(f"present total cost : {total_cost}, present budget {our_budget}")
    item = items_list[index]
    shopping_list.append(item["name"])
    total_cost = total_cost + (item["cost"] * item["amount"])
    index += 1
    for e in shopping_list :
        print(f"{e}")
    print("----------")
if "fries" in shopping_list and "burger patties" in shopping_list and "burger buns"  in shopping_list :
            print(f"We can make burgers and fries for {our_budget}")
print("out shoping list : ", shopping_list)

'''
EXERCISE 5: Error Handling with Try-Except

What happens when we change the index to a string? This should give you an error:
	1. Inside the while loop, add a try-except block to catch the error and print a useful message to the user so that the error doesn’t occur. 
	2. Add a break after printing the message
This is because if we have an error we don’t  want to go through the rest of the code
'''

try:
	shopping_list = []
	our_budget = 27.50
	total_cost = 0.00
	index = str(0)

	items_list = [
		{"name": "fries", "cost":6.25, "amount": 1},
		{"name": "burger patties", "cost":13.50, "amount": 1},
		{"name": "burger buns", "cost":3.50, "amount": 2},
		{"name": "tomato", "cost":1.50, "amount": 2},
		{"name": "lettuce", "cost":5, "amount": 1},
		{"name": "Ketchup", "cost":3.47, "amount": 1},
		{"name": "pickles", "cost":4.25, "amount": 1}
	]


	while total_cost <= our_budget : #and index < len(items_list) :
		#print(f"present total cost : {total_cost}, present budget {our_budget}")
		item = items_list[index]
		total_cost = total_cost + (item["cost"] * item["amount"])
		index += 1
		if total_cost <= our_budget :
			shopping_list.append(item["name"])
			for e in shopping_list :
					print(f"{e}")
			print("----------")
	if "fries" in shopping_list and "burger patties" in shopping_list and "burger buns"  in shopping_list :
				print(f"We can make burgers and fries for {our_budget}")
	print("out shoping list : ", shopping_list)
except (TypeError) as e :
	print("ERROR: The index must be an integer\n", shopping_list)


'''
EXERCISE 6: Customize Your Script
'''

#Pasta Dinner

try:
	shopping_list = []
	our_budget = 27.50
	total_cost = 0.00
	index = 0

	items_list = [
		{"name": "spaghetti pasta", "cost": 6.25, "amount": 1},
    	{"name": "tomato sauce", "cost": 13.50, "amount": 1},
    	{"name": "parmesan cheese", "cost": 3.50, "amount": 2},
    	{"name": "chicken breast", "cost": 1.50, "amount": 2},
    	{"name": "garlic", "cost": 5.00, "amount": 1},
    	{"name": "olive oil", "cost": 3.47, "amount": 1},
    	{"name": "basil", "cost": 4.25, "amount": 1},
	]


	while total_cost <= our_budget : #and index < len(items_list) :
		#print(f"present total cost : {total_cost}, present budget {our_budget}")
		item = items_list[index]
		total_cost = total_cost + (item["cost"] * item["amount"])
		index += 1
		if total_cost <= our_budget :
			shopping_list.append(item["name"])
			for e in shopping_list :
					print(f"{e}")
			print("----------")
	if "spaghetti pasta" in shopping_list and "tomato sauce" in shopping_list and "parmesan cheese"  in shopping_list :
				print(f"We can make Pasta Dinner for {our_budget}")
	print("out shoping list : ", shopping_list)
except (TypeError) as e :
	print("ERROR: The index must be an integer\n", shopping_list)

