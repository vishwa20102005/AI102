import streamlit as st
import google.generativeai as genai
genai.configure(api_key="AIzaSyA85tJDn52NCgeEn7S88vYUD7xmxsDTxMU")
model=genai.GenerativeModel("gemini-2.5-flash")
qns=st.text_input("Enter the question:")
if st.button("submit"):
    res=model.generate_content(qns+"you are the smart email writer.writes or replies to email with tone adjustment and quick replies.")
    st.write(res.text)