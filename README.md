# Explainable AI Fraud Detection System

## Overview
This project is a Streamlit-based application that detects fraudulent financial transactions using machine learning and explainable AI techniques.

The system allows users to generate predictions and understand why a transaction is classified as fraudulent.

---

## Features

- Fraud prediction using a trained model  
- Interactive dashboard for data exploration  
- Global feature importance  
- Local explanations using LIME  
- Clean user interface  

---

## System Modules

- **Dashboard** – Explore dataset statistics  
- **Predictions** – Generate fraud risk scores  
- **Model Insights** – Understand model behaviour  
- **Dataset & Ethics** – View limitations and considerations  

---
## How to Run

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the app:
```bash
streamlit run app.py
```

---

## Dataset

The dataset is not included due to file size limitations.  
Use a labelled fraud dataset (e.g., creditcard.csv).

---

## Model

The trained model is included in the `/models` folder.  
Alternatively, it can be recreated using `train_model.py`.

---

## Author

Final-year undergraduate dissertation project (BSc Information Technology).
