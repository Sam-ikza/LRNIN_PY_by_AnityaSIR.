# import matplotlib.pyplot as plt

# x = [1, 2, 3, 4, 5]
# y = [10, 20, 15, 30, 25]

# plt.plot(x, y, marker='o')
# plt.title("My First Graph")
# plt.xlabel("X Values")
# plt.ylabel("Y Values")

# plt.show()



import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = pd.DataFrame({
    "Hours": [1, 2, 3, 4, 5],
    "Marks": [30, 40, 50, 70, 80],
    "Sleep": [8, 7, 8, 6, 7]
})

sns.heatmap(data.corr(numeric_only=True), annot=True, cmap="coolwarm")

plt.title("Correlation Heatmap")
plt.show()
