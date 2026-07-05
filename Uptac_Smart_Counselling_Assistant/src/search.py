import pandas as pd


def load_data():
    df = pd.read_csv(
        "Uptac_Smart_Counselling_Assistant/data/processed/final_dataset.csv"
    )
    return df


def clg_search(df):

    clg = input("Enter college name : ").strip().lower()
    br = input("Enter Branch You want : ").strip().lower()
    cat = input("Enter Your Category : ").strip().lower()
    ro = input("Enter Round (Round 1 - Round 4) : ").strip().lower()
    qu = input("Enter Quota (All india / Home state) : ").strip().lower()

    search = df[df["Institute"].str.strip().str.lower().str.contains(clg)]
    br_search = search[search["Program"].str.strip().str.lower().str.contains(br)]
    cat_search = br_search[
        br_search["Category"].str.strip().str.lower().str.contains(cat)
    ]
    ro_search = cat_search[cat_search["Round"].str.strip().str.lower().str.contains(ro)]
    qu_search = ro_search[ro_search["Quota"].str.strip().str.lower().str.contains(qu)]

    result = qu_search[
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

    result = result.sort_values(by="Closing_Rank", ascending=True).reset_index(
        drop=True
    )

    print("COLLEGE SEARCH RESULTS")
    print("-" * 50)
    print("Total Matching Records : ", len(result))

    if result.empty:
        print("No matching records found.")
    else:
        print(result)


def main():
    df = load_data()
    clg_search(df)


if __name__ == "__main__":
    main()
