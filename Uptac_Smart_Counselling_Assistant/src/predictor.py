import pandas as pd


def load_data():
    df = df = pd.read_csv(
        "Uptac_Smart_Counselling_Assistant/data/processed/final_dataset.csv"
    )
    return df


def main():
    df = load_data()


if __name__ == "__main__":
    main()
