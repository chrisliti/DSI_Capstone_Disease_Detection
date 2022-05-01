import streamlit as st
import os
import PIL
import cv2
from pathlib import Path
import subprocess
import sys
import moviepy.editor as moviepy

## Upload video
video_file = st.file_uploader('myvideo.mp4', type = ['mp4'])
st.video(video_file)

submit = st.button('Detect Disease')

with st.spinner('Detecting...'):
  #On predict button click
  if submit:
    #if st.button('Detect Disease'):
    with open(video_file.name, "wb") as f:
      f.write(video_file.getbuffer())



    ## Run inference
    #os.chdir('/content/drive/MyDrive/Capstone-Project/Object-Detection/yolov5')

    img_fdr= video_file.name
    weights_fdr="best.pt"

    subprocess.run([f"{sys.executable} detect.py --weights {weights_fdr} --source {img_fdr}"],shell=True)
    #subprocess.Popen([f"{sys.executable} -m scoop run.py {RUN_ID}"],stdout=PIPE,stderr=STDOUT,shell=True)
    #subprocess.run([f"{sys.executable}", "script.py"])
    #print(f"python3 detect.py --weights {weights_fdr} --source {img_fdr}")

    def get_subdirs(b='.'):
        '''
            Returns all sub-directories in a specific Path
        '''
        result = []
        for d in os.listdir(b):
            bd = os.path.join(b, d)
            if os.path.isdir(bd):
                result.append(bd)
        return result

    def get_detection_folder():
        '''
            Returns the latest folder in a runs\detect
        '''
        return max(get_subdirs(os.path.join('runs', 'detect')), key=os.path.getmtime)

    for vid in os.listdir(get_detection_folder()):
      st_video = open(str(Path(f'{get_detection_folder()}') / vid),'rb')
      video_bytes = st_video.read()
      st.video(video_bytes)
      #st.write(str(Path(f'{get_detection_folder()}') / vid))
      #video_name = str(Path(f'{get_detection_folder()}') / vid)
      #st.write(video_name)
      #st.video(str(Path(f'{get_detection_folder()}') / vid))
      
      #video_name = str(Path(f'{get_detection_folder()}') / vid)
      #st.write(video_name)
      #clip = moviepy.VideoFileClip(video_name)
      #clip.write_videofile(video_name)
      #st_video = open(video_name,'rb')
      #video_bytes = st_video.read()
      #st.video(video_bytes)
      

            
      

      

