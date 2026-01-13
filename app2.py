import streamlit as st

st.title("some basic commands in streamlit like slider button")

age = st.slider("Enter your age", 1,100)

city = st.selectbox("choose your city :",["delhi", "pune", "mumbai", "banglore", "nagar","kolhapur"])

if st.button("submit"):
    st.write(f"you are {age} year old and live in {city} city.")



