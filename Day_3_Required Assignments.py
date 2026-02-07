'''
Docstring for Day_3_Required Assignments

Define three tuples to represent grocery items, each containing:
name (string), price (float), and quantity (integer).
Example: apples_tuple = ("apples", 0.50, 5)
'''
apple_item = ("apple",0.50,5)
orange_item = ("orange",0.70,7)
banana_item = ("banana ",0.60,6)

grocery_list = []
grocery_list.extend([apple_item,orange_item,banana_item])
print(f"out put of 1st item : {grocery_list[0]}")
print(f"out put of 2nd item : {grocery_list[1]}")
print(f"out put of 3rd item : {grocery_list[2]}")

apple_totalprice = grocery_list[0][1] * grocery_list[0][2]
orange_totalprice = round(grocery_list[1][1] * grocery_list[1][2],1)
banana_item = round(grocery_list[2][1] * grocery_list[2][2],1)
total_apples = f"Total cost of apples: {apple_totalprice}"
total_oranges = f"Total cost of apples: {orange_totalprice}"
total_bananas = f"Total cost of apples: {banana_item}"
print(total_apples)
print(total_oranges)
print(total_oranges)

'''
Create three dictionaries for grocery items containing the following keys:
"name" (string), "price" (float), "quantity" (integer)
Example: apple_dict = {"name":"apple", "price":0.50, "quantity": 5}

'''
apple_dict = {"name":"apple", "price":0.50, "quantity": 5}
orange_dict = {"name":"orange", "price":0.70, "quantity": 7}
banana_dict = {"name":"banana", "price":0.60, "quantity": 6}

print(apple_dict)
print(orange_dict)
print(banana_dict)

'''
For each of the dictionaries, calculate and store the total cost by multiplying price and quantity, and assign it to a new key, "total_cost".
Expected output:
'''
total_dict_apples = round((apple_dict["price"] * apple_dict["quantity"]),2)
total_dict_oranges = round((orange_dict["price"] * orange_dict["quantity"]),2)
total_dict_bananas = round((banana_dict["price"] * banana_dict["quantity"]),2)

print(total_dict_apples)
print(total_dict_oranges)
print(total_dict_bananas)
apple_dict.update({"total_cost":total_dict_apples})
orange_dict.update({"total_cost":total_dict_oranges})
banana_dict.update({"total_cost":total_dict_bananas})

print(apple_dict)
print(orange_dict)
print(banana_dict)

print(f"Total cost of apples: ${apple_dict["total_cost"] :.2f}")
print(f"Total cost of apples: ${orange_dict["total_cost"] :.2f}")
print(f"Total cost of apples: ${banana_dict["total_cost"] :.2f}")

'''
Using the list num_list = [16, 47, 1, 3, 5, 9, 15, 2], complete the following:
Slice and print: Everything from the second index onward.
Slice and print: Everything up to (but not including) the fourth index.
Use a negative index to get and print the third-to-last item in the list.
'''

num_list = [16, 47, 1, 3, 5, 9, 15, 2]
print(f"Slice and print: Everything from the second index onward {num_list[2:]}")
print(f"Slice and print: Everything up to (but not including) the fourth index {num_list[:4]}")
print(f"Use a negative index to get and print the third-to-last item in the list : {num_list[-3]}")

# Sort the list in descending order and print the sorted list
print(num_list)
sort_list = sorted(num_list)

print(f"sorted list : {sort_list}")
4
# or use below code
num_list.sort()
print(num_list)

#Find and print the length of 
print(f"lenght of the list : {len(num_list)}")

'''
Create two sets that contain the following:
    Dairy Products: milk, butter, cream, yogurt, and cheese 
    Desserts: jello, chocolate, candy, cookies, muffins 
'''
Dairy_Products = {"milk","butter", "cream", "yogurt", "cheese"}
Desserts = {"jello", "chocolate", "candy", "cookies", "muffins"}

#Add the shared item, ‘ice_cream’ to both sets that qualifies as both a dessert and a dairy product
Dairy_Products.add("ice_cream")
Desserts.add("ice_cream")
print(Dairy_Products)
print(Desserts)

#Remove an item from each set that is not the shared item
Dairy_Products.discard("butter")
Desserts.discard("candy")
print(Dairy_Products)
print(Desserts)

# Find and print the intersection (common items) between the two sets
intersect_result = Dairy_Products.intersection(Desserts)
print(f"intersection (common items) between the two sets : {intersect_result}")