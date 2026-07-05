# 🎓 UPTAC Smart Counselling Assistant

A beginner-friendly Streamlit application developed to help students during UPTAC counselling. This project allows users to search college cutoff details, predict eligible colleges based on rank, and generate a personalized choice filling list using historical UPTAC cutoff data.

---

## 🚀 Features

### 🔍 College Search
- Search college cutoff details.
- Filter by:
  - Institute
  - Program
  - Category
  - Round
  - Quota
- View Opening Rank and Closing Rank.

### 🎯 Rank Predictor
- Predict eligible colleges using:
  - Rank
  - Program
  - Category
  - Round
  - Quota
- Shows:
  - Dream Colleges
  - Moderate Colleges
  - Safe Colleges
- Calculates Rank Gap.

### 📝 Choice Filling
- Select multiple preferred programs.
- Generates a priority-based choice filling list.
- Displays top recommended choices.

---

## 📂 Project Structure

```text
Uptac_Smart_Counselling_Assistant
│
├── data
│   ├── raw
│   └── processed
│       └── final_dataset.csv
│
├── graphs
│
├── src
│   ├── data_cleaning.py
│   ├── analysis.py
│   ├── search.py
│   ├── predictor.py
│   └── choice_filling.py
│
├── app.py
├── requirements.txt
└── README.md
```

---

## 🛠️ Technologies Used

- Python
- Pandas
- Streamlit

---

## ▶️ How to Run

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
streamlit run app.py
```

---

## 📊 Dataset

The project uses historical UPTAC counselling cutoff data after preprocessing and cleaning.

---

## 🎯 Future Improvements

- PDF Download Support
- Better UI Design
- Advanced Recommendation Logic
- Latest Year Cutoff Support

---

## 📸 Project Screenshots

### 🏠 Home
-- Uptac_dash.png

### 🔍 College Search
-- Uptac_dash_search.png

### 🎯 Rank Predictor
-- Uptac_dash_pred.png

### 📝 Choice Filling
-- Uptac_dash_choice.png

---

## 👨‍💻 Author

**Giridhar Jadon**

Machine Learning & AI Enthusiast