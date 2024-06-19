import streamlit as st
import os 
import base64
import io
from PIL import Image
import pdf2image as pd2
import google.generativeai as genx
from dotenv import load_dotenv
load_dotenv()

# Configure Google Generative AI
genx.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get AI response
def get_ai(input, pdf_content, prompt):
    model = genx.GenerativeModel('gemini-pro-vision')
    res = model.generate_content(input, pdf_content, prompt)
    return res.text

# Function to process the uploaded PDF
def input_pdf(uploaded_file):
    if uploaded_file is not None:
        try:
            # Convert PDF to images
            pages = pd2.convert_from_bytes(uploaded_file.read())
            f1 = pages[0]
            imag = io.BytesIO()
            f1.save(imag, format="JPEG")
            imag_byte = imag.getvalue()
            pdf_parts = [
                {
                    "mime_type": "image/jpeg",
                    "data": base64.b64encode(imag_byte).decode()
                }
            ]
            return pdf_parts
        except pd2.exceptions.PDFInfoNotInstalledError as e:
            st.error("Poppler is not installed or not in PATH. Please install it to proceed.")
            return None
    else:
        st.error("No file found")
        return None

# Streamlit app configuration
st.set_page_config(page_title="RESUME CHECKER")
st.header("ATS RESUME TRACKING")

# User inputs
input = st.text_input("Job Description", key="input")
upload = st.file_uploader("Upload Your resume", type=["pdf"])

if upload is not None:
    st.write("Resume Uploaded Successfully")

# Button actions
prompt1 = st.button("Tell me about resume")
prompt2 = st.button("How can I improve")
prompt3 = st.button("Percentage match")

prompt = "You are an experienced technical human resource manager your task is to review the resume on the basis of job description. Please share your professional evaluation on whether the candidate profile aligns with the job description"

# Define the button actions
if prompt1:
    if upload is not None:
        pdf_content = input_pdf(upload)
        if pdf_content:
            response = get_ai(prompt, pdf_content, input)
            st.subheader("GENERATED")
            st.write(response)
        else:
            st.write("Please upload a valid resume")
elif prompt2:
    if upload is not None:
        pdf_content = input_pdf(upload)
        if pdf_content:
            response = get_ai(prompt, pdf_content, input)
            st.subheader("GENERATED")
            st.write(response)
        else:
            st.write("Please upload a valid resume")
elif prompt3:
    if upload is not None:
        pdf_content = input_pdf(upload)
        if pdf_content:
            response = get_ai(prompt, pdf_content, input)
            st.subheader("GENERATED")
            st.write(response)
        else:
            st.write("Please upload a valid resume")
