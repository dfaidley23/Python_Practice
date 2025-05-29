import streamlit as st

st.title("Weather Forecast for the Next Day")
location = st.text_input("Location: ")
days = st.slider("Forecasted Days", min_value=1, max_value=5, help="Select the number of forcasted days")
option = st.selectbox("Select the data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {location}")