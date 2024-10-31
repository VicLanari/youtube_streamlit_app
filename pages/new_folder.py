import streamlit as st
import os
import shutil
from dotenv import load_dotenv, dotenv_values

load_dotenv()

MY_VIDEO_DIR = os.getenv('MY_VIDEO_DIR')



def new_folder(folder_name):
    Folders = ["Videos", "Images", "Text","Audio", "Assets"]
    cur_dir = os.getcwd()
    video_dir = MY_VIDEO_DIR
    dest = os.path.join(video_dir, folder_name)
    print("New folder located at:" + dest)
    try:
        os.mkdir(folder_name)
        shutil.move(os.path.join(cur_dir, folder_name), video_dir)
        print(f"'{folder_name}' video folder created successfully.")
    except FileExistsError:
        print(f"Directory '{folder_name}' already exists.")
    except PermissionError:
        print(f"Permission denied: Unable to create '{folder_name}'.")
    except Exception as e:
        print(f"An error occurred: {e}")
    for name in Folders:
        try:
            os.mkdir(name)
            to_move = os.path.join(cur_dir, name)
            shutil.move(to_move, dest)
            print(f"'{name}' file created successfully.")
        except FileExistsError:
            print(f"Directory '{name}' already exists.")
        except PermissionError:
            print(f"Permission denied: Unable to create '{name}'.")
        except Exception as e:
            print(f"An error occurred: {e}")
            
st.set_page_config(page_title='Automate Youtube App')
st.title("Create a new folder 📁")
st.subheader("Here you can create a new video file with all the correct folders you need and store them directly in your video storage folder")

option = st.chat_input("Name of your new video folder")
if option is not None:
    new_folder(option)
    "Your new folder " + option + " was created!"