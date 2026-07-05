import pandas as pd


def load_data():
    df = pd.read_csv(
        "Uptac_Smart_Counselling_Assistant/data/processed/final_dataset.csv"
    )
    return df


def choice_filling(df):

    rank = int(input("Enter your Rank : "))
    program = input("Enter Preferred Program : ").strip().lower()
    cat = input("Enter Your Category : ").strip().lower()
    ro = input("Enter Round (Round 1 - Round 4) : ").strip().lower()
    qu = input("Enter Quota (All india / Home state) : ").strip().lower()

    program_df = df[df["Program"].str.strip().str.lower().str.contains(program)]
    cat_df = program_df[
        program_df["Category"].str.strip().str.lower().str.contains(cat)
    ]
    ro_df = cat_df[cat_df["Round"].str.strip().str.lower().str.contains(ro)]
    qu_df = ro_df[ro_df["Quota"].str.strip().str.lower().str.contains(qu)]

    eligible_df = qu_df[rank <= qu_df["Closing_Rank"]]

    choice_df = eligible_df[
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

    choice_df["Rank_Gap"] = choice_df["Closing_Rank"] - rank

    choice_df = choice_df.sort_values(
        by=["Closing_Rank", "Rank_Gap"], ascending=True
    ).reset_index(drop=True)

    choice_df.insert(0, "Choice_No", range(1, len(choice_df) + 1))

    print("CHOICE FILLING LIST")
    print("-" * 50)
    print("Total Choices : ", len(choice_df))

    if choice_df.empty:
        print("No choices found for the given rank and filters.")
    else:
        print(choice_df.head(50))
        choice_df.to_csv(
            "Uptac_Smart_Counselling_Assistant/outputs/choice_filling_list.csv",
            index=False,
        )

        print("Choice filling list saved successfully.")


def main():
    df = load_data()
    choice_filling(df)


if __name__ == "__main__":
    main()
