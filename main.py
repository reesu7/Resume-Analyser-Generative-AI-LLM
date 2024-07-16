import streamlit as st
from Response.utils import get_response
from ResumeParser.parser import pdf_text
from Prompts.prompt import input_prompt
import os
from dotenv import load_dotenv
load_dotenv()
import google.generativeai as genai
st.set_page_config(page_title="RESUME CHECKER")
st.header("ATS RESUME TRACKING")

job_description = st.text_input("Job Description", key="job_description")
uploaded_file = st.file_uploader("Upload Your resume", type=["pdf"])

if uploaded_file is not None:
    st.write("Resume Uploaded Successfully")


prompt1 = st.button("Evaluate")
#prompt2 = st.button("Improvements")
#prompt3 = st.button("Percentage match")

if prompt1:
    if uploaded_file is not None:
        text_content = pdf_text(uploaded_file)
        if text_content:
            get_input = input_prompt(text_content,job_description)
            response = get_response(get_input)
            st.subheader("GENERATED")
            st.write(response)
        else:
            st.write("Please upload a valid resume")
    else:
        st.error("No file found")
