# app.py
import streamlit as st

def calculate_square(x):
    return x ** 2

st.title("🔢 Square Finder Calculator")

number = st.number_input("Enter a number:", value=0.0)
square = calculate_square(number)
st.write(f"The square of {number} is **{square}**.")
