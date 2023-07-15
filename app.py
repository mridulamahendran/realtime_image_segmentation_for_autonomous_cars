import shutil
from Old.main import func
from Old.video_segment import vid_fun
import streamlit as st 
from segment import segment_vid, segment_image
import os
from PIL import Image

def remove(path):
    try:
        shutil.rmtree(path)
    except OSError as e:
        print("Error: %s : %s" % (path, e.strerror))

def remove2():
    try:
        os.remove("./out.mp4")
    except OSError as e:
        print("Error: %s" % ( e.strerror))
    try:
        os.remove("./output.mp4")
    except OSError as e:
        print("Error: %s" % ( e.strerror))


st.header('Semantic Segmentation')
tab1, tab2 = st.tabs(["Image Segmentation", "Video Segmentation"])

with tab1:
    img = st.file_uploader('Upload Image', type=["jpg"])
    img_path = './Images/uploaded.jpg'
    out_path = './runs/detect'
    if img is not None:
        with open(img_path, 'wb') as f:
            f.write(img.read())
            
        if st.button('Segment Image'):
            remove(out_path)
            output = func(img_path)
            segment_image(img_path)
            st.warning('Segmentation Completed')
            image = Image.open('./Images/segmented.jpg')
            image2 = Image.open('./runs/detect/exp/uploaded.jpg')
            image3 = Image.open('./Images/uploaded.jpg')
            st.write("Input Image:")
            st.image(image3)
            st.write("Segmented Image:")
            st.image(image)
            st.write("Predicted Image:")
            st.image(image2)
            st.write("Inference:")
            st.write(output)
        
    
        
        
with tab2:
    vdo = st.file_uploader('Upload video')
    vid_path = './Videos/uploaded.mp4'
    
    if vdo is not None:
        with open(vid_path, 'wb') as f:
            f.write(vdo.read())
            
        if st.button('Segment Video'):
            remove2()
            segment_vid(vid_path)
            os.system("ffmpeg -i ./Videos/segmented.mp4 -vcodec libx264 ./Videos/segmented_out.mp4 -y")
            vid_fun(vid_path)
            os.system("ffmpeg -i ./out.mp4 -vcodec libx264 ./output.mp4 -y")
            st.warning('Segmentation Completed')
            
            video = open('./Videos/segmented_out.mp4', 'rb')
            video2 = open('./Videos/uploaded.mp4','rb')
            video3 = open('./output.mp4', 'rb')
            video_bytes = video.read()
            video_bytes2 = video2.read()
            video_bytes3 = video3.read()
            st.write("Input video:")
            st.video(video_bytes2)
            st.write("Segmented video:")
            st.video(video_bytes)
            st.write("Predicted video:")
            st.video(video_bytes3)            