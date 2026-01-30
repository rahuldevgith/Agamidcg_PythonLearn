#exercise 1

milk = 15
bread = 5
eggs = 10
total_cost = milk + bread + eggs
print(f"Your total is: ${total_cost}")

# exercise 2

# Exercise 2: String Manipulation
# Instructions:
# Create a Python script that asks the user for the name of their favourite grocery store, then prints a silly greeting welcoming them to the store. 

# Requirements:
# Use input() to get the store name from the user.
# Use string concatenation to print a greeting
# like "Welcome to [store name]!".
# Add a comment explaining each line of code. 

# Program to print grocery store welcome them
# below is the store name variable to which accepts the input from use for favourite grocery store name
store_name = input("Please provie your favourite grocery store name : ")
# Below line of code is the F string for concat the string with the store name to welcome the usesr
print(f"Welcome to {store_name}") 


# Exercise 3: Common Errors
# Instructions:
# Here’s a small buggy code block. The task is to fix it!


# The program has an error, find it and fix it
milk = float("3")
bread = 2.5
total = milk + bread
print(f"The total cost is: ${total}")