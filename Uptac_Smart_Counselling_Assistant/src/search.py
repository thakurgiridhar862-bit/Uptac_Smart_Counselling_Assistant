import pandas as pd


def load_data():
    df = df = pd.read_csv(
        "Uptac_Smart_Counselling_Assistant/data/processed/final_dataset.csv"
    )
    return df


def clg_search(df):

    clg = input("Enter college name : ").strip().lower()
    br = input("Enter Branch You want : ").strip().lower()
    search = df[df["Institute"].str.strip().str.lower().str.contains(clg)]
    br_search = search[search["Program"].str.strip().str.lower().str.contains(br)]
    search_imp = br_search[
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
    print("COLLEGE SEARCH RESULTS")
    print("-" * 50)
    print("Total Matching Records : ", len(search_imp))
    if br_search.empty:
        print("College not found")

    else:
        print(search_imp)


def main():
    df = load_data()
    clg_search(df)


if __name__ == "__main__":
    main()
