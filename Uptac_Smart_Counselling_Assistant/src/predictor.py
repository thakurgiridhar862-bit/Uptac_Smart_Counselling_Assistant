import pandas as pd


def load_data():
    df = pd.read_csv(
        "Uptac_Smart_Counselling_Assistant/data/processed/final_dataset.csv"
    )
    return df


def pred(df):

    rank = int(input("Enter your Rank : "))
    program = input("Enter Preferred Program : ").strip().lower()
    cat = input("Enter Your Category : ").strip().lower()
    ro = input("Enter Round (Round 1 - Round 4) : ").strip().lower()
    qu = input("Enter Quota (All india / Home state) : ").strip().lower()

    program_df = df[df["Program"].str.strip().str.lower().str.contains(program)]
    cat_df = program_df[
        program_df["Category"].str.lower().str.strip().str.contains(cat)
    ]
    ro_df = cat_df[cat_df["Round"].str.strip().str.lower().str.contains(ro)]
    qu_df = ro_df[ro_df["Quota"].str.strip().str.lower().str.contains(qu)]

    el_df = qu_df[rank <= qu_df["Closing_Rank"]]

    result = el_df[
        [
            "Institute",
            "Program",
            "Round",
            "Category",
            "Quota",
            "Opening_Rank",
            "Closing_Rank",
        ]
    ].copy()

    result["Rank_Gap"] = result["Closing_Rank"] - rank

    result = result.sort_values(by="Closing_Rank", ascending=True).reset_index(
        drop=True
    )

    print("RANK PREDICTION RESULTS")
    print("-" * 50)
    print(f"Your Rank        : {rank}")
    print(f"Your Program     : {program}")
    print(f"Your Category    : {cat}")
    print(f"Your Quota       : {qu}")
    print(f"Your Round       : {ro}")
    print("Eligible Colleges : ", len(result))

    if result.empty:
        print("No eligible colleges found for the given rank and filters.")
    else:
        print(result.head(20))


def main():
    df = load_data()
    pred(df)


if __name__ == "__main__":
    main()
