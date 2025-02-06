import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("David Faidley")
    content = """I am David"""
    st.info(content)

content2 = """Bewlow you will see a list of my apps built in Python. Feel free to contact me."""
st.write(content2)

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")

with col3:
   for index, row in df[:10].interrows():
       st.header(row["title"])

with col4:
    for index, row in df[10:].interrow():
        st.header(row["title"])
