# class Circle:
#     def __init__(self, radius, color):
#         self.radius = radius
#         self.color = color


# # Creating a Circle object
# c1 = Circle(5, "Red")

# # Displaying the attributes
# print("Radius:", c1.radius)
# print("Color:", c1.color)


# class Car:
#     def __init__(self,brand,price):
#         self.brand = brand
#         self.price = price


# car1 = Car("Hyundai", 20000)

# print("Brand:", car1.brand)
# print("Brand:", car1.brand)
# print("Brand:", car1.brand)
# print("Brand:", car1.brand)
# print("Price:", car1.price)

# Problem 1: Buggy Code

class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def Display(self):
        print("Name:", self.name)
        print("ID:", self.id)


class Emp(Person):
    def __init__(self, name, id):
        super().__init__(name, id)

    def Print(self):
        print("Emp class called")


Emp_details = Emp("Mayank", 103)
Emp_details.Display()
Emp_details.Print()



# Problem 2: Anagram Check

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

str1 = str1.replace(" ", "").lower()
str2 = str2.replace(" ", "").lower()

if sorted(str1) == sorted(str2):
    print("The strings are anagrams")
else:
    print("The strings are not anagrams")



# Problem 3: Armstrong Number

num = int(input("Enter a number: "))

original = num
digits = len(str(num))
sum = 0

while num > 0:
    digit = num % 10
    sum = sum + digit ** digits
    num = num // 10

if sum == original:
    print("Armstrong number")
else:
    print("Not an Armstrong number")




# Problem 4: Vehicle Class

class Vehicle:

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        self.color = "white"
        self.seating_capacity = 0

    def assign_seating_capacity(self, capacity):
        self.seating_capacity = capacity

    def display_properties(self):
        print("Maximum Speed:", self.max_speed, "kmph")
        print("Mileage:", self.mileage, "kmpl")
        print("Color:", self.color)
        print("Seating Capacity:", self.seating_capacity)
        print("--------------------------")


car1 = Vehicle(200, 20)
car1.assign_seating_capacity(5)

car2 = Vehicle(180, 25)
car2.assign_seating_capacity(4)

print("First Vehicle Details:")
car1.display_properties()

print("Second Vehicle Details:")
car2.display_properties()