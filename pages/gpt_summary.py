from openai import OpenAI
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

# You need to insert your chat gpt API key in order for this program to work
GPT_KEY = os.getenv('GPT_KEY')

client = OpenAI(
    api_key=GPT_KEY
)

# You can change the prompt if you have previously used prompts that have worked for you
def gptsummary(transcipt_path):
    with open(transcipt_path, 'r') as file:
        file_content = file.read()
    response = client.chat.completions.create(
        model = "gpt-4o",
        messages = [
        {"role":"system", "content":"You are an assistant to my Youtube production company. Our job is to analyze video transcripts in order to summarize or create our own"},
        {"role":"user", "content":f"Please summarize this video transcript {file_content}"}
        ]
    
    )
    output = response.choices[0].message.content
    with open('transcript_summary', 'w') as summary:
        summary.write(output)

st.set_page_config(page_title='Automate Youtube App')
st.title("Summarize Transcripts 🗒")
st.subheader("Here you can summarize the transcripts you previously downloaded")
st.write('just paste your file path below as such /yourhd/channelfolder/videofolder/transcript.txt')

path = st.text_input('Paste your path here')
if path is not None:
    gptsummary(path)