import pandas as pd
import matplotlib.pyplot as plt

# Create the dataset
data = {
    "Year": [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
    "Patents Filed": [1200, 1500, 1800, 2200, 2700, 3500, 4200, 5000, 5800]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Create a figure
plt.figure(figsize=(10, 5))

# Plot Bar Chart
plt.bar(df["Year"], df["Patents Filed"], color='blue', alpha=0.6, label="Patents Filed (Bar)")

# Plot Line Chart (on top of the bar chart)
plt.plot(df["Year"], df["Patents Filed"], marker='o', linestyle='-', color='red', label="Patents Filed (Line)")

# Labels and Title
plt.xlabel("Year")
plt.ylabel("Number of Patents")
plt.title("Number of AI-related Patents Filed (2015-2023)")
plt.legend()
plt.grid(True)

# Show combined chart
plt.show()
