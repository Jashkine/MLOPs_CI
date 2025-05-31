import streamlit as st

st.title("🔢 Square Finder Calculator")

# Input
number = st.number_input("Enter a number:", value=0.0)

# Compute square
square = number ** 2

# Output
st.write(f"The square of {number} is **{square}**.")
