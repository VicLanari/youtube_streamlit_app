from openai import OpenAI
import os
from dotenv import load_dotenv
import streamlit as st
import shutil
import glob

load_dotenv()

# You need to insert your chat gpt API key in order for this program to work
GPT_KEY = os.getenv('GPT_KEY')
MY_VIDEO_DIR = os.getenv('MY_VIDEO_DIR')
MAIN_VIDEO_FOLDER_PATH = os.getenv('MAIN_VIDEO_FOLDER_PATH')
MAIN_VIDEO_FOLDER = os.getenv('MAIN_VIDEO_FOLDER')

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
    with open('transcript_summary.txt', 'w') as summary:
        summary.write(output)

# This function moves your transcript summaries into your desired video folder
def move_to_video_file(video_folder):
    cur_dir = os.getcwd()
    video_dir = MY_VIDEO_DIR
    dest = os.path.join(video_dir, video_folder) 
    ls = glob.glob('transcript_summary*.txt')
    print(ls)
    for i in ls:
        try:
            shutil.move(os.path.join(cur_dir, i), dest)
            print("File moved.")
        except FileExistsError:
            print(f"Directory folder already exists.")
        except PermissionError:
            print(f"Permission denied: Unable to create folder.")
        except Exception as e:
            print(f"An error occurred: {e}")

st.set_page_config(page_title='Automate Youtube App')
st.title("Summarize Transcripts 🗒")
st.subheader("Here you can summarize the transcripts you previously downloaded")
st.write('just paste your file path below as such /yourhd/channelfolder/videofolder/transcript.txt')

path = st.text_input('Paste your path here', value=None)
if path is not None:
   gptsummary(path)

path_ls = glob.glob(MAIN_VIDEO_FOLDER_PATH) # include a * after the path ex: /Users/example/channelvideos/* to get all video folders
video_ls = []
videos = []
for path in path_ls:
    video_ls.append(path.split(MAIN_VIDEO_FOLDER)) # only the video folder from the previous path ex: channelvideos/
for i in video_ls:
    for x in i:
        if '/' not in x:
            videos.append(x)

select = st.selectbox("where would you like your transcripts to go?", videos, index=None)
if select is not None:
    move_to_video_file(select)