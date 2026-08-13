import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Penguins dataset
data = pd.read_csv(r"C:\Users\user pc\Desktop\FIP\Week 3 Deliverable\penguins.csv")

print("Dataset loaded successfully!")
print(data.head())

# Line Plot
plt.plot(data.index[:20], data["body_mass_g"][:20])

plt.title("Penguin Body Mass")
plt.xlabel("Penguin")
plt.ylabel("Body Mass (g)")

plt.show()

# Scatter Plot
plt.scatter(data["flipper_length_mm"], data["body_mass_g"])

plt.title("Flipper Length vs Body Mass")
plt.xlabel("Flipper Length (mm)")
plt.ylabel("Body Mass (g)")

plt.show()

# Histogram
sns.histplot(data["body_mass_g"].dropna(), bins=10)

plt.title("Distribution of Penguin Body Mass")
plt.xlabel("Body Mass (g)")
plt.ylabel("Number of Penguins")

plt.show()

# Box Plot
sns.boxplot(x="species", y="body_mass_g", data=data)

plt.title("Penguin Body Mass by Species")
plt.xlabel("Penguin Species")
plt.ylabel("Body Mass (g)")

plt.show()