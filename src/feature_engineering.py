import pandas as pd

def load_data():
   return pd.read_csv("data/cleaned_f1.csv")


def create_features(df):
   grouped = df.groupby('driver_name')

   features = pd.DataFrame()
   features['avg_position'] = grouped['position'].mean()
   features['total_points'] = grouped['points'].sum()
   features['consistency'] = grouped['position'].std()

   features = features.fillna(0)

   return features


def save_features(features):
   features.to_csv("data/features.csv")


def main():
   df = load_data()
   features = create_features(df)
   save_features(features)
   print("Features created successfully")


if __name__ == "__main__":
   main()
