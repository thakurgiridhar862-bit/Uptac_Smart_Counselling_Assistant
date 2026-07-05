import pandas as pd


def load_data():
    df = df = pd.read_csv(
        "Uptac_Smart_Counselling_Assistant/data/processed/final_dataset.csv"
    )
    return df


def clg_search(df):

    clg = input("Enter college name : ").strip().lower()
    df["Institute"] = df["Institute"].str.strip().str.lower()

    search = df[df["Institute"].str.contains(clg)]

    if search.empty:
        print("College not found")

    else:
        print(search)


def main():
    df = load_data()
    clg_search(df)


if __name__ == "__main__":
    main()
