import streamlit as st
import google.generativeai as genai
from docx import Document
genai.configure(api_key="AQ.Ab8RN6LjEu7CX51xyX7O_yDA3QY6IhImrDKigtsV8gMl9aBtaQ")
model=genai.GenerativeModel("gemini-2.5-flash")
st.header("AI Story Teller:")
prompt=st.text_input("Enter your topic:")
a="You are a pro in story teller so accooringly give me story introduction subtopic and conclusion win a entered topic by input as user "
if st.button("submit"):
    response=model.generate_content(a+prompt)
    st.write(response.text)
    document = Document()
    document.add_paragraph(response.text)
    document.save("Story.docx")
    st.download_button(label="Download Story",  file_name="Story.docx", data =open("Story.docx", "rb"), mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document")