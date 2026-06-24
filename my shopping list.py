# Shopping List Manager using File Handling

# Step 1: Write the initial shopping list
file = open("shopping_list.txt", "w")

n = int(input("Enter the number of initial shopping items: "))

for i in range(n):
    item = input(f"Enter item {i + 1}: ")
    file.write(item + "\n")

file.close()

# Step 2: Append new items
file = open("shopping_list.txt", "a")

m = int(input("\nEnter the number of new items to add: "))

for i in range(m):
    item = input(f"Enter new item {i + 1}: ")
    file.write(item + "\n")

file.close()

# Step 3: Read and display the updated shopping list
file = open("shopping_list.txt", "r")

print("\n----- Updated Shopping List -----")

for line in file:
    print(line.strip())

file.close()