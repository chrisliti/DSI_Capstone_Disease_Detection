import streamlit as st
import os
import PIL
import cv2
from pathlib import Path
import subprocess
import sys
import moviepy.editor as moviepy

## introduction

html_temp = """
<div style="background-color:dodgerblue;padding:10px">
<h2 style="color:white;text-align:center;">Plant Disease Detection App </h2>
</div>
    """
st.markdown(html_temp,unsafe_allow_html=True)

st.markdown("")
image = Image.open('drone_field1.jpeg')
st.image(image,use_column_width=True)

st.markdown("""
This web page leverages computer vision (deep learning) to detect plant diseases from videos. This application uses YoloV5 algorithm.


## Upload video
st.subheader('Upload Video')
st.write('Upload a video of your crops below for detection.')
video_file = st.file_uploader('myvideo.mp4', type = ['mp4'])
#st.video(video_file)

st.subheader('Disease Detection')
st.write('Hit the Detect Disease button below to run the algorithm on your video.')
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
      #st_video = open(str(Path(f'{get_detection_folder()}') / vid),'rb')
      #video_bytes = st_video.read()
      #st.video(video_bytes)
      #st.write(str(Path(f'{get_detection_folder()}') / vid))
      #video_name = str(Path(f'{get_detection_folder()}') / vid)
      #st.write(video_name)
      #st.video(str(Path(f'{get_detection_folder()}') / vid))
      
      video_name = str(Path(f'{get_detection_folder()}') / vid)
      #st.write(video_name)
      #clip = moviepy.VideoFileClip(video_name)
      #clip.write_videofile(video_name)
      #st_video = open(video_name,'rb')
      #video_bytes = st_video.read()
      #st.video(video_bytes)
      st.subheader('Download Processed Video')
      st.write('Hit the Download Video button to download your processed video below')
      with open(video_name, "rb") as file:
        btn = st.download_button(
          label="Download Video",
          data=file,
          file_name="Detection Disease Video.mp4",
          mime="video/mp4"
          )
      
      

            
      

      

