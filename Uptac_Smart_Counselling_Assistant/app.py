import streamlit as st
import pandas as pd


def load_data():
    df = pd.read_csv("data/processed/final_dataset.csv")
    return df


df = load_data()

st.title("🎓 UPTAC Smart Counselling Assistant")

menu = st.sidebar.selectbox(
    "Choose Feature",
    ["🏠 Home", "🔍 College Search", "🎯 Rank Predictor", "📝 Choice Filling"],
)

inst = sorted(df["Institute"].dropna().unique())
prog = sorted(df["Program"].dropna().unique())
cat = sorted(df["Category"].dropna().unique())
ro = sorted(df["Round"].dropna().unique())
qu = sorted(df["Quota"].dropna().unique())


if menu == "🏠 Home":
    st.header("🏠 Home")
    st.write("This project helps students during UPTAC counselling.")
    st.write("1. 🔍 College Search")
    st.write("2. 🎯 Rank Predictor")
    st.write("3. 📝 Choice Filling")


elif menu == "🔍 College Search":
    st.header("🔍 College Search")

    college = st.selectbox("Select College", inst)
    program = st.selectbox("Select Program", prog)
    category = st.selectbox("Select Category", cat)
    round = st.selectbox("Select Round", ro)
    quota = st.selectbox("Select Quota", qu)

    if st.button("🔍 Search"):
        result = df[df["Institute"] == college]
        result = result[result["Program"] == program]
        result = result[result["Category"] == category]
        result = result[result["Round"] == round]
        result = result[result["Quota"] == quota]

        result = result[
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

        result = result.sort_values(by="Closing_Rank").reset_index(drop=True)

        st.write("📊 Total Records :", len(result))

        if result.empty:
            st.write("❌ No matching records found.")
        else:
            st.dataframe(result)


elif menu == "🎯 Rank Predictor":
    st.header("🎯 Rank Predictor")

    rank = st.number_input("Enter Your Rank", min_value=1, step=1)
    program = st.selectbox("Select Program", prog)
    category = st.selectbox("Select Category", cat)
    round = st.selectbox("Select Round", ro)
    quota = st.selectbox("Select Quota", qu)

    if st.button("🎯 Predict"):
        result = df[df["Program"] == program]
        result = result[result["Category"] == category]
        result = result[result["Round"] == round]
        result = result[result["Quota"] == quota]
        result = result[rank <= result["Closing_Rank"]]

        result = result[
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

        result = result.sort_values(by="Closing_Rank").reset_index(drop=True)

        dream = result[result["Rank_Gap"] <= 5000]
        moderate = result[(result["Rank_Gap"] > 5000) & (result["Rank_Gap"] <= 20000)]
        safe = result[result["Rank_Gap"] > 20000]

        st.write("📊 Total Eligible Colleges :", len(result))

        if result.empty:
            st.write("❌ No eligible colleges found.")
        else:
            st.write("🌟 Dream Colleges")
            st.dataframe(dream.head(10))

            st.write("⚖️ Moderate Colleges")
            st.dataframe(moderate.head(10))

            st.write("✅ Safe Colleges")
            st.dataframe(safe.head(10))


elif menu == "📝 Choice Filling":
    st.header("📝 Choice Filling")

    rank = st.number_input("Enter Your Rank", min_value=1, step=1)
    se_prog = st.multiselect("Select Programs", prog)
    category = st.selectbox("Select Category", cat)
    round = st.selectbox("Select Round", ro)
    quota = st.selectbox("Select Quota", qu)

    if st.button("📝 Generate Choice List"):
        if len(se_prog) == 0:
            st.write("❌ Please select at least one program.")
        else:
            choice_df = df[df["Program"].isin(se_prog)]
            choice_df = choice_df[choice_df["Category"] == category]
            choice_df = choice_df[choice_df["Round"] == round]
            choice_df = choice_df[choice_df["Quota"] == quota]
            choice_df = choice_df[rank <= choice_df["Closing_Rank"]]

            choice_df = choice_df[
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
                by=["Closing_Rank", "Rank_Gap"]
            ).reset_index(drop=True)

            choice_no = []

            for i in range(len(choice_df)):
                choice_no.append(i + 1)

            choice_df["Choice_No"] = choice_no

            choice_df = choice_df[
                [
                    "Choice_No",
                    "Institute",
                    "Program",
                    "Round",
                    "Category",
                    "Quota",
                    "Opening_Rank",
                    "Closing_Rank",
                    "Rank_Gap",
                ]
            ]

            st.write("📊 Total Choices :", len(choice_df))

            if choice_df.empty:
                st.write("❌ No choices found.")
            else:
                st.dataframe(choice_df.head(50))
