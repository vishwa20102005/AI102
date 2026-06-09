import streamlit as st
import google.generativeai as genai
genai.configure(api_key="AQ.Ab8RN6IjzDm8ESTSQPjdBBfRFuB8ADDEA9-cfMtTxehMtoeC2A")
model=genai.GenerativeModel("gemini-2.5-flash")
qns=st.text_input("Enter the question:")
if st.button("submit"):
    res=model.generate_content(qns)
    st.write(res.text)