import streamlit as st
import os

#os.chdir('/content/drive/MyDrive/Capstone-Project/Object-Detection/yolov5')

def _all_subdirs_of(b='.'):
    '''
        Returns all sub-directories in a specific Path
    '''
    result = []
    for d in os.listdir(b):
        bd = os.path.join(b, d)
        if os.path.isdir(bd): result.append(bd)
    return result

def _get_latest_folder():
    '''
        Returns the latest folder in a runs\detect
    '''
    return max(all_subdirs_of('runs/detect'), key=os.path.getmtime)

def _save_uploadedfile(uploadedfile):
    '''
        Saves uploaded videos to disk.
    '''
    with open(os.path.join("data/videos",uploadedfile.name),"wb") as f:
        f.write(uploadedfile.getbuffer())

## Upload video
video_file = st.file_uploader('myvideo.mp4', type = ['mp4'])


#st.video(video_file)

