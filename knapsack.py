
# Fractional Knapsack using Greedy Algorithm

weights = [2, 3, 5, 4]
profits = [12, 15, 20, 12]
capacity = 8

n = len(weights)

# Calculate profit-to-weight ratio
ratio = []
for i in range(n):
    ratio.append(profits[i] / weights[i])

# Sort objects by ratio in descending order
items = list(zip(weights, profits, ratio))
items.sort(key=lambda x: x[2], reverse=True)

total_profit = 0

print("Selected objects:")

for weight, profit, r in items:
    if capacity == 0:
        break

    if weight <= capacity:
        # Take the complete object
        capacity -= weight
        total_profit += profit
        print(f"Full object: Weight={weight}, Profit={profit}")

    else:
        # Take only the fraction that fits
        fraction = capacity / weight
        earned = profit * fraction
        total_profit += earned

        print(f"Fraction taken: {fraction:.2f}")
        print(f"Weight taken: {capacity} kg")
        print(f"Profit earned: {earned:.2f}")

        capacity = 0

print("Maximum profit:", total_profit)



#  constructing max heapp by taking arrays as input 

