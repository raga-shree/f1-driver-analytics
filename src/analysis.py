import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score


def load_data():
   return pd.read_csv("data/features.csv")


def rank_drivers(features):
   features['score'] = (
       features['total_points'] * 0.5
       - features['avg_position'] * 0.3
       - features['consistency'] * 0.2
   )
   return features.sort_values(by='score', ascending=False)


def train_model(features):
   X = features[['avg_position', 'consistency']]
   y = features['total_points']

   X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

   model = LinearRegression()
   model.fit(X_train, y_train)

   predictions = model.predict(X_test)

   mae = mean_absolute_error(y_test, predictions)
   r2 = r2_score(y_test, predictions)

   print("MAE:", mae)
   print("R2 Score:", r2)


def main():
   features = load_data()
   ranking = rank_drivers(features)
   print(ranking.head(10))

   train_model(features)


if __name__ == "__main__":
   main()
