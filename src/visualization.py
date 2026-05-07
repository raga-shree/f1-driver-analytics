import pandas as pd
import matplotlib.pyplot as plt


def load_data():
    return pd.read_csv("data/features.csv")


def plot_top_drivers(features):
    top = features.sort_values(by='total_points', ascending=False).head(10)

    plt.figure(figsize=(10, 5))
    top['total_points'].plot(kind='bar')

    plt.title("Top 10 Drivers")
    plt.xlabel("Drivers")
    plt.ylabel("Total Points")

    plt.tight_layout()
    plt.savefig("top_drivers.png")


def plot_relationship(features):
    plt.figure(figsize=(8, 5))

    plt.scatter(features['avg_position'], features['total_points'])

    plt.xlabel("Average Position")
    plt.ylabel("Total Points")
    plt.title("Performance Relationship")

    plt.tight_layout()
    plt.savefig("performance_plot.png")


def main():
    features = load_data()

    plot_top_drivers(features)
    plot_relationship(features)

    print("Visualizations created successfully!")


if __name__ == "__main__":
    main()