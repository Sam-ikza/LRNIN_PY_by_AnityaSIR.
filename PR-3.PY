# 1 . CREATING AN EMPTY DICT

INVENTORY = {}

# 2 . STORING PRODUCT 1 FIRST VAL IN DICT

PROD_NAME_1 = "MOBILE PHONE"
Product_Quantity_1 = 5
Product_Price_1 = 20000
ProductNo1_releaseYear = 2020

# 3 ADDING DETAILS OF THE FIRST PRODUCT UNDER A UNIQUE KEY 'PRODUCT-1' IN INVENTORY

INVENTORY['Product1'] = {
    'NAME': PROD_NAME_1 ,
    'QUANTITY' : Product_Quantity_1,
    'PRICE' : Product_Price_1,
    'release_year' : ProductNo1_releaseYear ,
}

# 4 . STORING THE SECOND Product details in variable

Product_Name_2 = "Laptop"
Product_Quantity_2 = 2
Product_Price_2 = 45000
ProductNo2_releaseYear = 2021

  # 5. Add the item details in inventory
INVENTORY['Product2'] = {
    'name': Product_Name_2,
    'quantity': Product_Quantity_2,
    'price': Product_Price_2,
    'release_year': ProductNo2_releaseYear
}


# 6. Display the products present in inventory
print("--- Current Inventory ---/n")
print(INVENTORY,"\n")

# 7. Check if ProductNo1_releaseYear and ProductNo2_releaseYear are in inventory.

print(f"Does'release_year' exist in Product '1' ? {'release_year' in INVENTORY['Product1']}")
print(f"Does'release_year' exist in Product '2' ? {'release_year' in INVENTORY['Product2']}")
# 8. Delete release year of both the products from the inventory

print("\n",INVENTORY['Product1']['release_year'])

del INVENTORY['Product1']['release_year']
del INVENTORY['Product2']['release_year']

print("\n")
print("--- Inventory after deleting release years ---")
print(INVENTORY)


# OPERATIONS IN TUPLES

# 1 Creating a tuple of product prices

prices = (250, 300, 150, 400, 100, 350, 200)

# 2 Findin n printin the max n min price

print(f"HIGHEST PRICED : {max(prices)}")
print(f"LOWEST PRICED : {min(prices)}")

# 3 CALCULATING AND PRINTIN SUM 

print(f"TOTAL OF ALL PRICES : {sum(prices)}")

# 4 CNVRTING TUPLE IN SORTED LIST IN ASCENDIN ORDER

print(f"SORTED PRICES : {sorted(prices)}")

# 5 TRYIN TO MODIFY ANY ELMN IN TUPLE

# prices[2] = 3434

# tuple are immutable so it'll throw an err

# we should catcch it by 

try:
  prices[0] = 4322
except TypeError as r:
  print(f"Error while modifying : {r}")
