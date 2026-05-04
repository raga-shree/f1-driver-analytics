import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data/features.csv")

print(df.head())

# -----------------------------
# TOP DRIVERS BY TOTAL POINTS
# -----------------------------
top_points = df.sort_values(by='total_points', ascending=False).head(10)

plt.figure()
plt.bar(top_points['driver_name'], top_points['total_points'])
plt.title("Top Drivers by Total Points")
plt.xlabel("Driver")
plt.ylabel("Points")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# -----------------------------
# CONSISTENCY ANALYSIS
# -----------------------------
top_consistency = df.sort_values(by='consistency').head(10)

plt.figure()
plt.bar(top_consistency['driver_name'], top_consistency['consistency'])
plt.title("Most Consistent Drivers (Lower is Better)")
plt.xlabel("Driver")
plt.ylabel("Consistency Score")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()