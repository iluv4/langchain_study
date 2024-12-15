from dotenv import load_dotenv
load_dotenv()

#put in api 

from langchain.chat_models import ChatOpenAI
chat_model = ChatOpenAI()
content = "hi"

result = chat_model.predict(content + "~can you write about it?")
print(result)

import streamlit as st
st.title("I'm your mother")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

import pdfplumber

if uploaded_file is not None:
    with pdfplumber.open(uploaded_file) as pdf:
        first_page = pdf.pages[0]
        text = first_page.extract_text()
        st.write(text)

import base64

def show_pdf(file):
    base64_pdf = base64.b64encode(file.read()).decode('utf-8')
    pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf">'
    st.markdown(pdf_display, unsafe_allow_html=True)

if uploaded_file is not None:
    show_pdf(uploaded_file)
