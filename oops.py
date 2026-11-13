# oop = object oriented prgrming in python 
# provide a clear structure , less repetation dry dont repeat yourself 
# reusable block of code with a specific purpose

# car is a class while brands are its object beacuse a car is worldwide have 4 wheels and a engine and a body 
# and brnads may have different prop but at last they are cars only 

# creatin class sues class keywprd
#  python is an obj oriented prgrmg lang  almost evrythng in py is an obj , with 
# its prop and methods A Class is like an object constructor, or a "blueprint" for creating objects.

# class Vaas:
#     c = 5

# A = Vaas()
# print(A.c)

# del A # deleting object 

# print(A.c)

# pass 

# class Person:
#     pass

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# p1 = Person("Roi",90)

# print(p1.name)
# print(p1.age)

# withoput __init__() we ahve to manualy set a obj prop after its creation 
# like p1.name = "sam" p1.age = 43

# but with init this method calls it self automaticallly everytime the class is being used to create a new obj 
 
# multiple parameters can be passed to the init method and we can set them as obj prop4
# class Person:
#   def __init__(self, name, age, city, country):


# self paaram is a reference to the current instance of the class
# self  is used to acces class prop

# class Dog:
# 	def __init__(self,name,age):
# 		self.name = name
# 		self.age = age
# 	def bark(self): # self is llike this pointer into c++ it point to the correct instance and help a function recieve a param
# 		# In Python, we use self in def bark(self) because self refers to the current object that is calling the method.
# 		# without slef well not know which objects prop u want to access 
# 		#  self doesnt have to be named self . but it is the first param of any method in class
# 		print(self.name)
# # Create an object
# d = Dog("SER",3)
# d.bark()

#  calling method with self 

# class person:
	
#     def __init__(self,name):
#         self.name = name

#     def greet(self):
#         return "Hello , " + self.name

#     def welcome(self):
#         message = self.greet()
#         print(message + "welcome to the soul")

# P = person("Roi")
# P.welcome()

# Class  properties are varb that belongs to a class and store data for each object
# created from the class 
# like name , age , brand , year  manipulating value 
#  accessing obj.prop 
# modify prop - obj.prop = " " -> change the value of the property
# delete propo - del obj.prop -> delete the property from the object

# we can add prop later by leaving space for them 
# from distro import name


# class Person:
#     lastname = " "

#     def __init__(self, name):
#         self.name = name

# p1 = Person("Linus")
# p2 = Person("Emil")

# Person.lastname = "Refsnes" #This will set the lastname for all instances of Person
# p1.age = "34" # added new prop to a existing obj p1 only not p2
# print(p1.age)
# print(p1.lastname)
# print(p2.lastname)


# class Student:
# 	def __init__(self,name,grade):
# 		self.name = name
# 		self.grade = grade

# s1 = Student("Anna","A")
# s1.grade = "B"
# print(s1.grade)


# methodas are funxctions that belongs to a class , they define the behaviour of objects created from the class
# alll must have self as the first parameter 

# Mwthods with parameters can accept parameters just like regular functions .



# class Calculator:
#   def add(self,a,b):
#     return a + b
#   def cal(self,a,b):
#     return a*b # method with parameter 



# class person:
	
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def greet(self):
#         return "Hello , " + self.name

#     def welcome(self):
#         message = self.greet()
#         print(message + "welcome to the soul")

#     # method that can acess obj property

#     def get_info(self):
#         return f"{self.name} is {self.age} years old"

#     def celebrate_birthday(self):
#         self.age += 1
#         print(f"Happy birthday! You are now {self.age}") #methods that can modify prop

# # with __str__() we can  print obj

#     def __str__(self):
#         return f"{self.name} ({self.age})"

# P = person("Roi", 30)
# P.welcome()
# print(P.get_info())
# print(P)

#  a class can have multiple methods that works together 
#  we can use del to delete a mthods 
# del P.get_info()

# Magic Methods 

# magic methods are specail methods with double underscore , theyare also callled as dunder methods 
#  we do not call it directly , py calls them for us  some ex -  __eq__ (controls the eql means for the class  obj2 == obj2 )
# __add__() 


# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def __add__(self, other):
#     return self.age + other.age

# p1 = Person("Emil", 22)
# p2 = Person("Tobias", 19)

# print(p1 + p2)

# without def __add__() writting p1+p2 would rasie a Typeerror
# len = returns the num of employee or len of object 
# it = used to compare two objects or to sort smthn
#  contains() controls what in operatore checks for your own objects 

#  Python inheritance
# inheritance  allows a another class to inherit all the methods and prop of another class
# parent class class where prop are being inherited from  also called base class
# child class is class the inherits from another class derived classc
# any class can be a parent class so the syntax will be same 

# creating a child class is done my passing the parent class aas a parmeter
# class Person:
#     def __init__(self,fname,lname):
#         self.fname = fname
#         self.lname = lname
#     def callname(self):
#         print(f"your name is {self.fname} {self.lname}")

# class Student(Person):
#     def __init__(self,fname,lname,year):
#         super().__init__(fname, lname) #addin super func to it
#     # adding a prop year to the cild obj 
#         self.gradyear = year
#     #  addding methods
#     def welcome(self):
#         print(f"welcome {self.fname} {self.lname} to the class of {self.gradyear}")

# when we add __init__ method to child class , then it wil not call the init func of the pARENT CHILD 
# the child 's __inti__ func will overide the parent one inint func .
#     pass

# x = Student("Sam",21,2021)
# x.callname()

# python also has a super() func that will make the child classs to inherit all the prop and methods of the parnt calsss 

# Polymorphism the word polymorphism mean "many forms" i programming it refers that a sam e function or method or operator can be impllemented in various objects and clases .
# ex of len() on string , tuple , dict 

# class Polymorphism
# polymorphism is mainl;y used in  class method , where different class can have 
# same method name 
# we can call same method by looping  
# for x in (obj1.obj2,obj3):
#     x.move()

# works with iheritance to polymorphism

# Encapsulation
#  it main hiding or protecting data properties and mr=ethods in a class and controoling how and who can access , so it prevents changes made by others and protct how a class work and its data .

# making prop priv by using __age like
# def __init__(self,name,age):
#     self.name = name
#     self.__age = age

# print(p1.__age)  this statement ill cAUSE AN ERROR 
# for accesssing any private prop we use getter method 

# print(p1.get_age())
# p1.get_age()

# for setting private prop we use setter method
# def set_age():
#     if age > 0:
#         self.__age = set_age
#     else:
#         print

# p1.set_age(23)

# using single underscor it is for others dev loper to see it doesnt make our data protecteed 

# private methods 

# same usinf doubleundersocre as prefix __ infront of any method
#  def __callp(self):
#     pass
#  NAME MANGLING 
# name mangling deals with private prop and methods , llike whenver we add 
# __ to the start of prop or meth it aotumatically rename it internally by adding the class's namee in front 
# like  self.__age becomes _person__age
# we can access private prop by name mangling 
# print(p1._person__age)


# File handling 
# open is the main function here while manipulating file 
# it takes two params filename , and mode
# modes are = r,w,a(append),x(create new file),t(text mode),b(binary mode)
# f = open("sam.text","r") opening and reading the file
# make sure the file exists otherwise it will cause an error 
# open() func return a file object , which has a built in method to read() for reading the content 
# f = open("sam.txt")
# print(f.read())
# by using with we dont hAVE TO WRRY ABOIUT CLOSING THE FILE 

# with open("sam.txt") as f:
#     print(f.read())
# loooping it to read the whole content 
#     for x in f:
#         print(x)

# for writting in a file we use two params 
#  a appending (it adds content  to the end of the file ) 
#  w write it will overwrite the existing content of the file 
# with open("sam.txt","a") as f:
#     f.write("i am sam and this is it")


# try:
#     a = int(input("a ?"))
#     b = int(input("b ?"))
#     sum = a+b

# except ValueError:
#     print("num are not valid")
# finally:
#     print("operation ended")

#     package is a coollection of module in python similar module that has similar methods  container 
# a module is a aimple .py file containig data such as functions variables or classes that can be reuse in other py file 

# suppose i make a module name which is py fil e
# mymath.py

# def add(a,b):
#     return a+b

# then we can use in our main.ppy 
# by importing it 

# import mymath
# print(mymath.add(3,4))

# a package is a directory used to organize related pyhton module 
# __init__.py is our package initializer i sused to mark a directory as a paclage and helps to get module import in specific 

