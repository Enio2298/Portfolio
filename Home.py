import streamlit as st
from Email import send_email

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/foto.png", width=300)
with col2:
    st.text("Enio Rodríguez")
    content = """I'm Enio, and I enjoy learning new things, especially programming. 
    I want to challenge myself in these areas, and so far, it has been a fun hobby to pursue. 
    I’d like to deepen my knowledge of Python and explore other programming languages and applications, 
    such as Power BI, to apply these skills in real-world scenarios.
    I'm particularly interested in data-driven projects."""
    st.info(content)

content2="""You can send me an email below to get in touch with me!"""

st.text(content2)

st.header("Contact Me")

with st.form(key="email_form"):
    user_email = st.text_input("Your email address")
    raw_message = st.text_area("Your Message")
    message = f"""\
From: {user_email}


{raw_message}
"""
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Your email was sent succesfully!")
