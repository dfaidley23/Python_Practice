import streamlit as st
import sys
import os
    
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
    
from send_email import send_mail

st.header("Contact Us")

with st.form(key="email_form"):
    user_email = st.text_input("Your Email Address")
    raw_message = st.text_area("Your message here")
    message = f"""\
        Subject: new email from {user_email}

        From: {user_email}
        {raw_message}
        """
    button = st.form_submit_button("Submit")
    if button:
        send_mail(message)
        st.info("Your email was sent successfully.")