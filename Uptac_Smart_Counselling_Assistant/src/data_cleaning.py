import pandas as pd

df = pd.read_csv("Uptac_Smart_Counselling_Assistant/data/raw/uptac_cutoff_2025.csv")


def load_data():
    df = pd.read_csv("Uptac_Smart_Counselling_Assistant/data/raw/uptac_cutoff_2025.csv")
    return df


def data_overview(df):
    print("-" * 60)
    print("DATASET OVERVIEW")
    print("-" * 50)

    print("\nFIRST FIVE ROWS")
    print(df.head(5))

    print(f"\nTotal row              : {df.shape[0]}")
    print(f"Total Columns          : {df.shape[1]}")
    print(f"Total Null Values      : {df.isnull().sum().sum()}")
    print(f"Total Duplicate Values : {df.duplicated().sum()}")

    print("\nMISSING VALUES ")
    print("-" * 50)
    print(df.isnull().sum())

    print(" \n DATA TYPES")
    print("-" * 50)
    print(df.dtypes)

    print("\nNUMERICAL SUMMARY")
    print("-" * 50)
    print(df.describe())


def duplicate_analysis(df):
    print("\nDUPLICATE ANALYSIS")
    print("-" * 50)

    duplicates = df[df.duplicated()]

    print(f"Total Duplicate Records : {duplicates.shape[0]}")

    print("\nFIRST FIVE DUPLICATE ROWS")
    print(duplicates.head())


def remove_duplicates(df):

    print("\nREMOVING DUPLICATES")
    print("-" * 50)

    before = df.shape[0]

    df = df.drop_duplicates()

    after = df.shape[0]

    print(f"Rows Before : {before}")
    print(f"Rows After  : {after}")
    print(f"Removed     : {before - after}")

    return df


def main():
    df = load_data()
    data_overview(df)
    duplicate_analysis(df)
    df = remove_duplicates(df)


if __name__ == "__main__":
    main()
