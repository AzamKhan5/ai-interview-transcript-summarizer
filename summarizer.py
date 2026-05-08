import os
from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai

load_dotenv()

API_KEY = os.getenv("Google_API_KEY")

if not API_KEY:
    st.error("Gemini API Key not found in .env file")
    st.stop()
    
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

st.title("Interview Transcript Summarizer")

st.write("Upload an interview transcript file and get a structured summary.")

uploaded_file = st.file_uploader(
    "Upload Transcript",
    type=["txt"]
)

if uploaded_file is not None:

    transcript = uploaded_file.read().decode("utf-8")

    st.subheader("Transcript Preview")
    st.text_area("Transcript", transcript[:3000], height=250)

    if st.button("Generate Summary"):

        with st.spinner("Generating summary..."):

            prompt = f"""
            You are an interview transcript analyzer.

            Read the transcript and create a structured summary with these 3 sections:

            1. Topics Covered
            - Mention the main themes discussed in the interview.
            - Use bullet points.

            2. Profile
            - Identify what role/profile this candidate fits.
            - Mention seniority level if possible.
            - Give a short justification based on the interview.

            3. Candidate Summary
            - Write a short paragraph (3 to 6 sentences).
            - Include:
              - candidate background
              - strengths
              - concerns or weaknesses
              - overall impression

            Keep the output simple and clean.

            Transcript:
            {transcript}
            """

            response = model.generate_content(prompt)

            st.subheader("Generated Summary")

            st.write(response.text)