
import pandas as pd
import numpy as np
from IPython.display import display

# Problem 1
data1 = {
    "Student": ["David", "Samuel", "Terry", "Evan"],
    "Age": [27, 24, 22, 32],
    "Country": ["UK", "Canada", "China", "USA"],
    "Course": ["Python", "Data Structures", "Machine Learning", "Web Development"],
    "Marks": [85, 72, 89, 76]
}

df1 = pd.DataFrame(data1)
print("Problem 1")
display(df1)


# Problem 2
b = df1["Marks"]
print("Problem 2")
display(b)


# Problem 3
c = df1[["Country", "Course"]]
print("Problem 3")
display(c)


# Problem 4
data = {
    "Customer_ID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "Name": ["Amit", "Riya", "John", "Sara", "Karan", "Neha", "Rahul", "Pooja", "Vikas", "Anita"],
    "Age": [25, 32, 45, 28, np.nan, 35, 41, 29, 52, 31],
    "Gender": ["Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female"],
    "Purchase_Amount": [1200, 2500, 3200, 1800, 2200, np.nan, 4100, 1500, 3600, 2800]
}

df = pd.DataFrame(data)

print("\nProblem 4")
print("First 5 rows")
display(df.head())

print("Summary statistics")
display(df.describe())

print("Missing values before")
display(df.isnull().sum())

df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Purchase_Amount"] = df["Purchase_Amount"].fillna(df["Purchase_Amount"].mean())

print("Missing values after")
display(df.isnull().sum())


# Problem 5
print("\nProblem 5")

print("Age > 30")
display(df[df["Age"] > 30])

print("Total purchase by gender")
display(df.groupby("Gender")["Purchase_Amount"].sum())

print("Selected columns")
display(df[["Customer_ID", "Name", "Purchase_Amount"]])


# Problem 6
print("\nProblem 6")

df["Discounted_Price"] = df["Purchase_Amount"] * 0.90

print("With Discounted_Price")
display(df)

print("Average purchase by gender")
display(df.groupby("Gender")["Purchase_Amount"].mean())

print("Sorted by Purchase_Amount (descending)")
display(df.sort_values(by="Purchase_Amount", ascending=False))
