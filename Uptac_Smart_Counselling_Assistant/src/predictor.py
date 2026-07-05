import pandas as pd


def load_data():
    df = df = pd.read_csv(
        "Uptac_Smart_Counselling_Assistant/data/processed/final_dataset.csv"
    )
    return df


def pred(df):

    rank = int(input("Enter your Rank : "))
    cat = input("Enter Your Category : ").strip().lower()
    ro = input("Enter Round (Round 1 - Round 4) : ").strip().lower()
    qu = input("Enter  Quota (All india / Home state) : ").strip().lower()


def main():
    df = load_data()


if __name__ == "__main__":
    main()
