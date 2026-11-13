# dataset = [

# {"Name":"Serena Williams" , "Sport" : "Tennis" , "Achievements": 23},
#     {"Name": "Lionel Messi", "Sport": "Soccer", "Achievements": 7},
#     {"Name": "Michael Phelps", "Sport": "Swimming", "Achievements": 23},
#     {"Name": "Usain Bolt", "Sport": "Athletics", "Achievements": 8},
#     {"Name": "Roger Federer", "Sport": "Tennis", "Achievements": 20},
#     {"Name": "Cristiano Ronaldo", "Sport": "Soccer", "Achievements": 5},

# ]

# # Q1 — Check if Lionel Messi has more than 10 achievements. Since he has 7 Ballon d'Ors, the output is: "Lionel Messi does not have more than 10 achievements"

# for player in dataset:
#     if player ["Name"] == "Lionel Messi" :
#         if player["Achievements"] > 10:
#             print(player["Name"], "has more than 10 achievements.")
#             # print(f"Name: {player['Name']}, Sport: {player['Sport']}, Achievements: {player['Achievements']}")
#         else :
#             print("does not have more than 10 achievements")

# print("\n")

# # Check if a player plays Tennis or has exactly 20 achievements. Print "Success!" for matches (Roger Federer qualifies on both counts).

# for player in dataset:
#     if player["Sport"] == "Tennis" or player["Achievements"] == 20:
#         print(player["Name"], "Success player found ")
# print("\n")

# # Q3 — Find players with less than 10 achievements who don't play Soccer. Results: Usain Bolt (8 Gold Medals) and Cristiano Ronaldo (5 Ballon d'Ors).

# for player in dataset:
#     if player["Achievements"] < 10 and player["Sport"] != "Soccer":
#         print(f"Player Details: Name: {player['Name']} | Sport: {player['Sport']} | Achievements: {player['Achievements']}\n")

# # Q4 — Branching program for a number (1-9999) that checks:

# # If it's even or odd
# # If it's a palindrome
# # If it's divisible by the sum of its digits


# num_user = input("Enter an int (1 to 9999) : ")
# num = int(num_user)

# # even or odd

# if num % 2 == 0 :
#     print(f"{num} is even.\n")
# else:
#     print(f"{num} is Odd.\n")

# # palindrome

# if num_user == num_user[::-1]:
#     print(f"{num} is a Palindrome.\n")
# else:
#     print(f"{num} is NOT a Palindrome.\n")

# # 3. Divisibility by Sum of Digits

# digit_sum = sum(int(digit) for digits in num_user for digit in digits)

# if digit_sum != 0 and num % digit_sum == 0: 
#     print(f"{num} is divisible by the sum of its digits ({digit_sum}).")
# else:
#     print(f"{num} is NOT divisible by the sum of its digits ({digit_sum}).")

# # For loop printing numbers from -5 to 5 using range(-5, 6)

# for i in range(-5,6):
#     print(i)

# # Q6 — For loop printing all colors from the list: red, yellow, green, purple, blue

# col = ['red','yellow','green', 'purple', 'blue']

# for colors in col:
#     print(colors)

# # Q7 — While loop copying colors to a new list, stopping when 'orange' is encountered (though 'orange' isn't in the original list, so all colors copy over)

# new_list = []
# i = 0
# while i < len(col):
#     if col[i] == 'orange':
#         break
#     new_list.append(col[i])
#     i += 1

# print("New list:", new_list)

# Q8 — While loop finding animals with exactly 7 letters. Results: giraffe, gorilla, parrots

# Animals = ["lion", "giraffe", "gorilla", "parrots", "crocodile", "deer", "swan"]
# seven_letter_animals = []
# index = 0

# while index < len(Animals):
#     if len(Animals[index]) == 7:
#         seven_letter_animals.append(Animals[index])
#     index += 1

# print("Animals with 7 letters:", seven_letter_animals)


age = int(input())

if (age >= 18):
    print("u re elgibile to whtvr")
else:
    print("go to ur mum")