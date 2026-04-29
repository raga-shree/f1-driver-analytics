import pandas as pd

def load_data():
    drivers = pd.read_csv("data/drivers.csv")
    results = pd.read_csv("data/results.csv")
    races = pd.read_csv("data/races.csv")
    return drivers, results, races


def clean_results(results):
    # keep required columns
    results = results[['raceId', 'driverId', 'position', 'points', 'constructorId']]
    
    # remove rows with missing values
    results = results.dropna()
    
    # remove non-numeric positions (like 'DNF')
    results = results[results['position'].astype(str).str.isnumeric()]
    
    # convert to int
    results['position'] = results['position'].astype(int)
    
    return results


def merge_data(drivers, results, races):
    df = results.merge(drivers, on='driverId', how='left')
    df = df.merge(races, on='raceId', how='left')
    return df


def final_clean(df):
    # keep only important columns for next stages
    df = df[['driverId', 'forename', 'surname', 'raceId', 'year', 'position', 'points']]
    
    # create full driver name
    df['driver_name'] = df['forename'] + " " + df['surname']
    
    return df


def save_data(df):
    df.to_csv("data/cleaned_f1.csv", index=False)


def main():
    print("Loading data...")
    drivers, results, races = load_data()
    
    print("Cleaning results...")
    results = clean_results(results)
    
    print("Merging data...")
    df = merge_data(drivers, results, races)
    
    print("Final cleaning...")
    df = final_clean(df)
    
    print("Saving file...")
    save_data(df)
    
    print("DONE: cleaned_f1.csv created successfully")


if __name__ == "__main__":
    main()