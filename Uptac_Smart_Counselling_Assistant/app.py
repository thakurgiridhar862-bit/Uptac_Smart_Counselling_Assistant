import streamlit as st
import pandas as pd


def load_data():
    df = pd.read_csv(
        "Uptac_Smart_Counselling_Assistant/data/processed/final_dataset.csv"
    )
    return df


df = load_data()

st.title("UPTAC Smart Counselling Assistant")

menu = st.sidebar.selectbox(
    "Choose Option", ["Home", "College Search", "Rank Predictor", "Choice Filling"]
)

if menu == "Home":
    st.header("Welcome")
    st.write("This app helps students in UPTAC counselling.")
    st.write(
        "You can search colleges, predict colleges by rank, and generate choice filling list."
    )

elif menu == "College Search":
    st.header("College Search")
    st.write("College search feature will be added here.")

elif menu == "Rank Predictor":
    st.header("Rank Predictor")
    st.write("Rank predictor feature will be added here.")

elif menu == "Choice Filling":
    st.header("Choice Filling")
    st.write("Choice filling feature will be added here.")
