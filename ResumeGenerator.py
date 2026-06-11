import streamlit as st
import google.generativeai as genai
from docx import Document
genai.configure(api_key="AQ.Ab8RN6LjEu7CX51xyX7O_yDA3QY6IhImrDKigtsV8gMl9aBtaQ")
model=genai.GenerativeModel("gemini-2.5-flash")
st.header("AI Resume & Cover Letter Generator")
prompt=st.text_input("Enter your paragraph:")
a="You are a Resume & Cover Letter Generator ,Generate a resume and cover letter based on the content given by the user., The features of the resume and cover letter should include the key points and the main idea of the text, and also include the important details and the supporting evidence in a concise manner."
if st.button("submit"):
    response=model.generate_content(a+prompt)
    st.write(response.text)
    document = Document()
    document.add_paragraph(response.text)
    document.save("Resume_CoverLetter.docx")
    st.download_button(label="Download Resume & Cover Letter",  file_name="Resume_CoverLetter.docx", data =open("Resume_CoverLetter.docx", "rb"), mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document")