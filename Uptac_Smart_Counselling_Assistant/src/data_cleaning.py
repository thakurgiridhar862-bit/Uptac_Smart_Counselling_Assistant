import pandas as pd


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


def save_dataset(df):

    df.to_csv(
        "Uptac_Smart_Counselling_Assistant/data/processed/final_dataset.csv",
        index=False,
    )

    print("\nProcessed dataset saved successfully.")


def load_final_data():
    df = pd.read_csv(
        "Uptac_Smart_Counselling_Assistant/data/processed/final_dataset.csv"
    )
    return df


def data_summary(df):
    print("\nDATASET SUMMARY")
    print("-" * 50)

    print(f"Total Institutes : {df['Institute'].nunique()}")
    print(f"Total Programs   : {df['Program'].nunique()}")
    print(f"Total Streams    : {df['Stream'].nunique()}")
    print(f"Total Quotas     : {df['Quota'].nunique()}")
    print(f"Total Categories : {df['Category'].nunique()}")
    print(f"Total Seat Types : {df['Seat_Gender'].nunique()}")
    print(f"Total Rounds     : {df['Round'].nunique()}")

    print("\nROUND WISE RECORDS")
    print("-" * 50)
    print(df["Round"].value_counts())

    print("\nCATEGORY WISE RECORDS")
    print("-" * 50)
    print(df["Category"].value_counts())

    print("\nQUOTA WISE RECORDS")
    print("-" * 50)
    print(df["Quota"].value_counts())


def filter_rounds(df):

    print("\nFILTERING DATASET FOR ROUND 1 TO ROUND 4")
    print("-" * 50)

    print("Before Filtering")
    print(df["Round"].value_counts().sort_index())

    df = df[df["Round"].isin(["Round 1", "Round 2", "Round 3", "Round 4"])]

    print("\nAfter Filtering")
    print(df["Round"].value_counts().sort_index())

    df = df.reset_index(drop=True)

    return df


def main():
    df = load_data()
    data_overview(df)
    duplicate_analysis(df)
    df = remove_duplicates(df)
    save_dataset(df)
    load_final_data()
    data_summary(df)
    df = filter_rounds(df)
    df.to_csv(
        "Uptac_Smart_Counselling_Assistant/data/processed/final_dataset.csv",
        index=False,
    )


if __name__ == "__main__":
    main()
