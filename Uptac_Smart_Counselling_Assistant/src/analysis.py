import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def load_data():
    df = df = pd.read_csv(
        "Uptac_Smart_Counselling_Assistant/data/processed/final_dataset.csv"
    )
    return df


def round_wise_analysis(df):

    print("\nROUND WISE ANALYSIS")
    print("-" * 50)

    round_count = df["Round"].value_counts().sort_index()

    print(round_count)

    print("\nTotal Rounds :", df["Round"].nunique())

    print("\nHighest Records")
    print(round_count.max())

    print("\nLowest Records")
    print(round_count.min())


def main():
    df = load_data()
    round_wise_analysis(df)


if __name__ == "__main__":
    main()
