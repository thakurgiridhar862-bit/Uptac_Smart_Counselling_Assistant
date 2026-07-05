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


def inst_wise_analysis(df):

    print("\nINSTITUTE WISE ANALYSIS")
    print("-" * 50)

    inst_count = df["Institute"].value_counts().sort_values(ascending=False)

    print(inst_count.head(10))

    print("\nTotal Institutes :", df["Category"].nunique())

    print("\nHighest Records")
    print(inst_count.max())

    print("\nLowest Records")
    print(inst_count.min())

    # graph 2
    plt.figure(figsize=(12, 8))

    x = inst_count.head(10).values
    y = inst_count.head(10).index

    plt.barh(y, x)

    plt.title("Top 10 Institutes By Cutoff Records")
    plt.xlabel("Number of Records")
    plt.ylabel("Institute")

    for i in range(len(x)):
        plt.text(x[i] + 2, i, str(x[i]), va="center")

    plt.gca().invert_yaxis()

    plt.tight_layout()

    plt.savefig("Uptac_Smart_Counselling_Assistant/graphs/inst_wise_analysis.png")


def branch_wise_analysis(df):

    print("\nBRANCH WISE ANALYSIS")
    print("-" * 50)

    br_count = df["Program"].value_counts().sort_values(ascending=False)

    print(br_count.head(10))

    print("\nTotal Branches :", df["Program"].nunique())

    print("\nHighest Records")
    print(br_count.max())

    print("\nLowest Records")
    print(br_count.min())

    # graph 2
    plt.figure(figsize=(12, 8))

    x = br_count.head(10).values
    y = br_count.head(10).index

    plt.barh(y, x)

    plt.title("Top 10 Branches By Cutoff Records")
    plt.xlabel("Number of Records")
    plt.ylabel("Branch")

    for i in range(len(x)):
        plt.text(x[i] + 2, i, str(x[i]), va="center")

    plt.gca().invert_yaxis()

    plt.tight_layout()

    plt.savefig("Uptac_Smart_Counselling_Assistant/graphs/branch_wise_analysis.png")


def cr_analysis(df):

    print("\nCLOSING RANK ANALYSIS")
    print("-" * 50)

    print(f"Minimum Closing Rank : {df['Closing_Rank'].min()}")
    print(f"Maximum Closing Rank : {df['Closing_Rank'].max()}")
    print(f"Average Closing Rank : {df['Closing_Rank'].mean().round(2)}")
    print(f"Median  Closing Rank : {df['Closing_Rank'].median()}")


def main():
    df = load_data()
    round_wise_analysis(df)
    cat_wise_analysis(df)
    inst_wise_analysis(df)
    branch_wise_analysis(df)
    cr_analysis(df)
    print(df[df["Closing_Rank"] == df["Closing_Rank"].max()])


if __name__ == "__main__":
    main()
