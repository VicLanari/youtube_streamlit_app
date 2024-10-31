# youtube_streamlit
## Created by: Vicente Lanari

This app was made to facilitate creators jobs in organizing, downloading transcripts, and more
New aditions will come to the github page

## Credits

This package was created with Cookiecutter and the [andymcdgeo/cookiecutter_streamlit_app](https://github.com/andymcdgeo/cookiecutter-streamlit) project template.

YoutubeTranscriptApi by Jonas Depoix

## Set up your dotenv
Create a .env file to set your own parameters

MY_VIDEO_DIR = Path to your main video folder ex: "YourHardDrive/Users/You/YourChannel/Videos" #must be str#

MY_VIDEO_FOLDERS = Folder you would like to create inside every new video folder you make ex: "assets, video, audio, text" #Must be str#

MAIN_VIDEO_FOLDER_PATH = Same as MY_VIDEO_DIR but used to retrieve your video folder names, so include a * ex:"YourHardDrive/Users/You/YourChannel/Videos/*" #must be str#

MAIN_VIDEO_FOLDER = Only the folder name ex: "Videos/"

## To run your webapp
Use streamlit to run the home.py file in your localhost
streamlit run home.py