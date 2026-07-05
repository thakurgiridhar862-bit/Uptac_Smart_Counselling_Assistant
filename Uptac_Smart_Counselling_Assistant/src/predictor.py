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

    cat_df = df[df["Category"].str.lower().str.strip().str.contains(cat)]
    ro_df = cat_df[cat_df["Round"].str.strip().str.lower().str.contains(ro)]
    qu_df = ro_df[ro_df["Quota"].str.strip().str.lower().str.contains(qu)]
    el_df = qu_df[(qu_df["Opening_Rank"] <= rank) & (rank <= qu_df["Closing_Rank"])]


def main():
    df = load_data()


if __name__ == "__main__":
    main()
