import streamlit as st
import pandas as pd
import pymupdf
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GROQ_API_KEY") or st.secrets["GROQ_API_KEY"]
client = Groq(api_key=api_key)

st.title("DataTalk")
st.write("Every Information you need from csv and pdf's at you fingertip")

file = st.file_uploader("Upload CSV/PDF files", type=["csv", "pdf"])

def csv_parser(file):
    df = pd.read_csv(file)
    st.dataframe(df)

    data = df.to_string()
    user_input = st.text_input("Ask Questions Related on Data: ")

    prompts = f"""

    Data:
    {data}

    Question:
    {user_input}

    Answer: 
    """
        
    return prompts, user_input

def pdf_parser(file):
    doc = pymupdf.open(stream=file.read(), filetype="pdf")
    text = []
    
    for page in doc:
        text.append(page.get_text())
    
    user_input = st.text_input("Ask Questions Related on Data: ")

    prompts = f"""

    Data:
    {"\n".join(text)}

    Question:
    {user_input}

    Answer: 
    """

    return prompts, user_input


if file is not None:
    if file.name.endswith(".csv"):
        prompt, user_input = csv_parser(file)
    
    elif file.name.endswith(".pdf"):
        prompt = pdf_parser(file)

    with st.form("ask"):
        submitted = st.form_submit_button("Send")

    if not user_input:
        st.warning("Please enter a question.    ")

    else:
        chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a data analyst. Only answer based provided data concise and precise. If a user asks anything else, say 'I am restricted to data-related questions only.'"
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        model="llama-3.3-70b-versatile",
    )
            
        st.write(chat_completion.choices[0].message.content)


