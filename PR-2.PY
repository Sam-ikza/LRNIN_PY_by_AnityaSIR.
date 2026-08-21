#1 creating an empty list
Splist = []
print (f"EMPTY SHOPING LIST: {Splist}")




#2 STORING ITEMS IN THE LIST
Splist = ['Watch', 'laptop', 'shoes', 'pen', 'clothes']
print (f"SHOPING LIST WITH INITIAL ITEMS: {Splist}")




#3 adding new item by append
Splist.append('Football')
print (f"ADDEDD NEW ITEM TO THE LIST: {Splist}")



#4 printing last item from the list
Splist = ['Watch', 'laptop', 'shoes', 'pen', 'clothes']
print(Splist[-1]) # simple execution
# when there is no 1 ist go with this
# if Splist:
#
print(Splist[-1])
# else:
#
print("The list 'Splist' is empty, so there's no last item to print.")



# 5 printing entire SHOPPING LIST


print(f"ENTIRE SHOPPING LIST: {Splist}")


# emptylis = []
# if emptylis:
# print("PASS")
# else:
# print("list is empty")

# TU = True
# if TU:
# print("failed")
# else:
# print("pass")

# # #uint = "" # trial
# # IS USER'S AGE: uint}") # Print the age after a valid input is received
# uint = ""
# while not uint:
# uint = input("Enter your age: ")
# if not uint:
# print("Age must by typed")
# print (f"USER'S AGE: {uint}")

# user_name = "" # Initialize with an empty string to enter the loop
# while not user_name: # Loop continues as long as user_name is empty (falsy)
# user_name = input("Please enter your name: ")
# if not user_name:
# print("Name cannot be empty. Please try again.")
# print (f"Hello, {user_name}!")






#6 PRINTING ONLY LAPTOP N SHOES.




Splist = ['Watch', 'laptop', 'shoes', 'pen', 'clothes']
#itfnd = ['laptop', 'shoes']
itfnd = []
iitfnd = input("Enter items (space separated): ")
itfnd = iitfnd.split()
foundit = []

#print(iitfnd)

for item in itfnd:
    if item in Splist:
        foundit.append(item)
print(foundit)