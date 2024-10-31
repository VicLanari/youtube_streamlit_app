import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
import os
import shutil
import glob
from dotenv import load_dotenv, dotenv_values

load_dotenv()
MY_VIDEO_DIR = os.getenv('MY_VIDEO_DIR')
MAIN_VIDEO_FOLDER_PATH = os.getenv('MAIN_VIDEO_FOLDER_PATH')
MAIN_VIDEO_FOLDER = os.getenv('MAIN_VIDEO_FOLDER')

# This function separates the video ID from the link on the youtube URL
def get_ids(links):
    urls = []
    separated_links = links.split(",")
    clean_links = []
    for i in separated_links:
        clean_links.append(i.lstrip())
    ids = []
    for i in clean_links:
        ids.append(i.split("=")[-1])

    return ids

# This function downloads the selected video transcripts into the current dirrectory
def get_transcripts(links):
    ids = get_ids(links)
    rng = [range(1,len(ids))]
    tx = YouTubeTranscriptApi.get_transcripts(ids)
    info, non = tx
    final_lis = []
    for i in ids:
        lis = []
        for dic in info[i]:
            outtxt = dic['text']
            lis.append(outtxt)
        final_lis.append(lis)
        for i in final_lis:
            with open(f'transcript {final_lis.index(i) + 1}.txt', 'a') as opf:
                opf.write(" ".join(i) + '\n')
    print('Transcripts downloaded')

# This function moves your transcripts into your desired video folder
def move_to_video_file(video_folder):
    cur_dir = os.getcwd()
    video_dir = MY_VIDEO_DIR
    dest = os.path.join(video_dir, video_folder) # You can change this path in order to move your transcript to another folder in
#                                                  the video folder ex: users/example/MY_VIDEO_DIR/transcripts 
    ls = glob.glob('transcript*.txt')
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
st.title("Retrieve Transcripts 🗒")
st.subheader("Here you can download the transcripts from any YouTube video and store them in your prefered video file")


links = st.chat_input('Paste your youtube video links separated by commas')
if links is not None:
    get_transcripts(links)

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