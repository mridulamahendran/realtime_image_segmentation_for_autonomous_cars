import cv2
import torch
import argparse

def vid_fun(image_path):

    try: 
        vid = cv2.VideoCapture(int(image_path))
    except:
        print("Video File Found")
        vid = cv2.VideoCapture(image_path)
    num_frames = int(vid.get(cv2.CAP_PROP_FRAME_COUNT))

    # Print the number of frames
    print(f'Total number of frames: {num_frames}')

    try:
        model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
    except:
        print("OOPS! Looks like you are not connected to internet.")

    # Define the output video codec and frame rate
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    fps = vid.get(cv2.CAP_PROP_FPS)
    width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
    output = './out.mp4'
    # Create the output video writer object
    out = cv2.VideoWriter(output, fourcc, fps, (width, height))
    x = 0
    while True:  
        ret, frame = vid.read()
    
        if not ret:
            break
        x=x+1
        # Perform object detection on the current frame
        results = model(frame)
        # Draw the detected objects bounding boxes on the frame
        output_frame = results.render()[0]
        # Write the processed frame to the output video
        out.write(output_frame)
    out.release()
    return