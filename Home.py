import streamlit as st
import pandas

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/foto.png", width=300)
with col2:
    st.text("Enio Rodríguez")
    content = """I'm Enio i like to learn new things such as programming, i want to prove myself
    in this scenarios, and also till' this day it had been a funny hobbie to take, i would like to learn
    more about Python, and other languages, to apply this things in the real world"""
    st.info(content)

content2="""Below you can find some of the apps i have built in Python. Feel free to contact me!"""

st.text(content2)

df = pandas.read_csv("data.csv", sep=";")

col3, empty_col, col4 = st.columns([1.5, .5, 1.5])
#"""Los 1.5 y el .5 son las relaciones que tienen los anchos de las
#tres columnas"""
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.image("images/" + row["image"])
        st.write(row["description"])
        st.write(f"[Source code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.image("images/" + row["image"])
        st.write(row["description"])
        st.write(f"[Source code]({row['url']})")


