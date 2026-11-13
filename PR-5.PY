# ERROR HANDLING 

# 1 HANDLNG ZERO DIVISION ERROR 

# def cmplxcal():
#     num = float(input("Enter your num : "))


# 1  Handling ZeroDivisionError

def safe_div():
    try:
        numerator = float(input("numr :"))
        denominator = float(input("denom : "))
        result = numerator/denominator
        return result
    except ZeroDivisionError:
        print("Error : dividing by zero isnt defined !")
        return None


print(safe_div())


# 2 handling Valueerror
import math
def safe_sqrt(num):
    try:
        return math.sqrt(num)
    except ValueError:
        print("Error : Invalid input, please enter a valid number which is +ve.")
        return None

print(safe_sqrt(-6))
print(safe_sqrt(6))

print(safe_sqrt(16))
# A ValueError is raised when a function receives an argument of the correct type but an incorrect value.
# Think of it like ordering coffee — the cup is the right type, but you asked for something impossible inside it.

# 3 Handling Generic Exceptions 

def cpmlx_cal():
    try:
        return None

def safe_int():
    try:
        return int(input("Enter an integer: "))
    except ValueError:
        print("Error: please enter a valid integer.")
        return None


print(safe_int())
# A ValueError is raised when a function receives an argument of the correct type but an incorrect value.
# Think of it like ordering coffee — the cup is the right type, but you asked for something impossible inside it.

# 3 Handling Generic Exceptions 

def cpmlx_cal():
    try:
        num = float(input("Enter a number: "))
        res = num/(num-5)
        return num
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


print(cpmlx_cal())
print(cpmlx_cal())