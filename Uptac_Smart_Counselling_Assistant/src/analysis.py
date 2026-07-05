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

    # graph 1
    plt.figure(figsize=(12, 5))
    plt.title("Round Wise Cutoff Records")
    plt.xlabel("Round")
    plt.ylabel("Number of records")
    plt.grid(axis="y", alpha=0.4)
    x = round_count.index
    y = round_count.values
    ax = sns.barplot(x=x, y=y, palette="magma")
    for i in ax.containers:
        ax.bar_label(i, padding=5)

    plt.savefig(
        "Uptac_Smart_Counselling_Assistant/graphs/round_wise_analysis.png",
        dpi=300,
        bbox_inches="tight",
    )


def cat_wise_analysis(df):

    print("\nCATEGORY WISE ANALYSIS")
    print("-" * 50)

    cat_count = df["Category"].value_counts().sort_values(ascending=False)

    print(cat_count)

    print("\nTotal Categories :", df["Category"].nunique())

    print("\nHighest Records")
    print(cat_count.max())

    print("\nLowest Records")
    print(cat_count.min())

    # graph 2
    plt.figure(figsize=(12, 5))
    plt.title("Category Wise Cutoff Records")
    plt.xlabel("Category")
    plt.ylabel("Number of records")
    plt.grid(axis="y", alpha=0.4)
    x = cat_count.head(10).index
    y = cat_count.head(10).values
    ax = sns.barplot(x=x, y=y, palette="viridis")
    for i in ax.containers:
        ax.bar_label(i, padding=5)

    plt.savefig(
        "Uptac_Smart_Counselling_Assistant/graphs/cat_wise_analysis.png",
        dpi=300,
        bbox_inches="tight",
    )


def main():
    df = load_data()
    round_wise_analysis(df)
    cat_wise_analysis(df)


if __name__ == "__main__":
    main()
