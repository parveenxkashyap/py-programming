import streamlit as st
import pickle

# Load the trained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("Placement Predictor")

# Input fields for user
iq = st.number_input("Enter IQ of the student", min_value=0.0, max_value=100.0, step=0.01, format="%.2f")
cgpa = st.number_input("Enter CGPA of the student", min_value=0.0, max_value=10.0, step=0.01, format="%.2f")

if st.button("Predict"):
    # Predict placement using loaded model
    result = model.predict([[iq, cgpa]])[0]
    if result == 1:
        st.write("### You will get placed 🙌")
    else:
        st.write("### Placement might be difficult 😅")
