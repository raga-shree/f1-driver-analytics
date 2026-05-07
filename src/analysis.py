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
# AVG POSITION ANALYSIS
# -----------------------------
top_avg = df.sort_values(by='avg_position').head(10)

plt.figure()
plt.bar(top_avg['driver_name'], top_avg['avg_position'])
plt.title("Top Drivers by Average Position (Lower is Better)")
plt.xlabel("Driver")
plt.ylabel("Average Position")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# -----------------------------
# TOP 5 PIE CHART
# -----------------------------
top5 = df.sort_values(by='total_points', ascending=False).head(5)

plt.figure()
plt.pie(top5['total_points'], labels=top5['driver_name'], autopct='%1.1f%%')
plt.title("Top 5 Drivers Contribution by Points")
plt.show()