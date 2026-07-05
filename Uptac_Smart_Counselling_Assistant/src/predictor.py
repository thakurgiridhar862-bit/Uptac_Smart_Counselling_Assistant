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

    search_imp = el_df[
        [
            "Institute",
            "Program",
            "Round",
            "Category",
            "Quota",
            "Opening_Rank",
            "Closing_Rank",
        ]
    ]
    search_imp = search_imp.sort_values(by="Closing_Rank", ascending=True).reset_index(
        drop=True
    )

    print("COLLEGE SEARCH RESULTS")
    print("-" * 50)
    print("Total Matching Records : ", len(search_imp))
    if el_df.empty:
        print("No eligible colleges found for the given rank and filters.")

    else:
        print(search_imp)


def main():
    df = load_data()
    pred(df)


if __name__ == "__main__":
    main()
