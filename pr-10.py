
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load Iris dataset
df = sns.load_dataset("iris")

# Display first five rows
print(df.head())


# scatter plot


sns.scatterplot(
    data=df,
    x="sepal_length",
    y="sepal_width",
    hue="species"
)

plt.title("Iris Scatter Plot")
plt.show()



# kde density plot


sns.kdeplot(
    data=df,
    x="petal_length",
    hue="species",
    fill=True,
    alpha=0.3
)

plt.title("Density Plot of Petal Length")
plt.show()


# violin plot 



sns.violinplot(
    data=df,
    x="species",
    y="petal_length"
)

plt.title("Violin Plot of Petal Length")
plt.show()



# heatmap 


# Calculate correlation
corr = df.select_dtypes(include="number").corr()

# Create heatmap
sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Iris Dataset Correlation Heatmap")
plt.show()


# joint plot



sns.jointplot(
    data=df,
    x="petal_length",
    y="petal_width",
    hue="species",
    kind="scatter"
)

plt.show()


# pair plot 


sns.pairplot(
    df,
    hue="species",
    diag_kind="kde"
)

plt.show()



# The Iris dataset was successfully visualized using six Seaborn plotting techniques
