import streamlit as st
import pandas

st.header("Python Developer Projects")

df = pandas.read_csv("data.csv", sep=";")

col3, empty_col, col4 = st.columns([1.5, .5, 1.5])
#"""Los 1.5 y el .5 son las relaciones que tienen los anchos de las
#tres columnas"""
with col3:
    for index, row in df[:5].iterrows():
        st.header(row["title"])
        st.image("images/" + row["image"])
        st.write(row["description"])
        st.write(f"[Source code]({row['url']})")

with col4:
    for index, row in df[5:].iterrows():
        st.header(row["title"])
        st.image("images/" + row["image"])
        st.write(row["description"])
        st.write(f"[Source code]({row['url']})")