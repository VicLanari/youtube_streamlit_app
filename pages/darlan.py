from openai import OpenAI
import os
from dotenv import load_dotenv
import streamlit as st
import shutil
import glob
from youtube_transcript_api import YouTubeTranscriptApi
load_dotenv()

GPT_KEY = os.getenv('GPT_KEY')
MY_VIDEO_DIR = os.getenv('MY_VIDEO_DIR')
MAIN_VIDEO_FOLDER_PATH = os.getenv('MAIN_VIDEO_FOLDER_PATH')
MAIN_VIDEO_FOLDER = os.getenv('MAIN_VIDEO_FOLDER')

def get_ids(links):
    urls = []
    separated_links = links.split(",")
    clean_links = []
    for i in separated_links:
        clean_links.append(i.lstrip())
    ids = []
    for i in clean_links:
        ids.append(i.split("=")[-1])
    for i in ids:
        id = i
    return id

def get_transcript(link):
    id = get_ids(link)
    outls = []
    tx = YouTubeTranscriptApi.get_transcript(id)
    for i in tx:
        outtxt = (i['text'])
        outls.append(outtxt)
    final = ' '.join(outls)
    return final

def gpt15top(script):
    response = client.chat.completions.create(
        model = "gpt-4o",
        messages = [
        {"role":"system", "content":"Você é meu assistente em uma empresa de produção de conteúdo para o youtube. Seu papel é ler e resumir scripts"},
        {"role":"user", "content":f"Com esse script e título crie um resumo de 15 tópicos: {script}"} # mudar aqui a prompt que gera os 15 tópicos
        ]
    
    )
    output = response.choices[0].message.content
    response = client.chat.completions.create(
        model = "gpt-4o",
        messages = [
        {"role":"system", "content":"Você é meu assistente em uma empresa de produção de conteúdo para o youtube. Seu papel é ler o resumo dado e criar um script novo"},
        {"role":"user", "content":f"Com esse resumo crie um script para um vídeo em espanhol: {output}"} # Mudar aqui a prompt de criação de script
        ]
    )
    out = response.choices[0].message.content
    with open('/Users/vicentelanari/desktop/output.txt', 'w') as final:
        final.write(out)


client = OpenAI(
    api_key=GPT_KEY
)

st.set_page_config(page_title='Automate Youtube App')
st.title("Darlan Transcripts 🗒")
st.subheader("Essa ferramenta transforma um link de vídeo em um script novo")
st.write('Só colar o link do script')

link = st.text_input("Cole seu link aqui")
if link is not None:
    script = get_transcript(link)
    gpt15top(script)