# Finger-Counter-without-using-HandTrackingModule
This project is a real-time hand and finger counter implemented using OpenCV in Python. The program captures video from a webcam or a video file, processes each frame to detect hand contours, and counts the number of fingers raised. The results are displayed on the video feed in real-time.
Hand and Finger Counter using OpenCV
Project Description
This project is a real-time hand and finger counter implemented using OpenCV in Python. The program captures video from a webcam or a video file, processes each frame to detect hand contours, and counts the number of fingers raised. The results are displayed on the video feed in real-time.

# Features
1. Real-time video processing: Captures and processes video frames in real-time from a webcam or video file.
2. Hand detection: Detects hand contours using adaptive thresholding and contour detection techniques.
3. Finger counting: Counts the number of fingers raised based on convexity defects in the detected hand contour.
4. Visual feedback: Displays the detected contours and the finger count on the video feed.

# Installation
Clone the repository:

bash
Copy code
git clone https://github.com/Theanonymousghost/Finger-Counter-without-using-HandTrackingModule.git
cd hand-and-finger-counter

# Install dependencies:
Make sure you have Python installed. Then, install the required packages using pip:

pip install opencv-python numpy
Usage
Run the script with the default webcam as the video source:

python hand_and_finger_counter.py
Or specify a video file as the source:

python hand_and_finger_counter.py --video_path path/to/your/video.mp4
# Code Overview
# count_fingers(contour): This function calculates the number of fingers raised based on the convexity defects of the detected hand contour.
# hand_and_finger_counter(video_path=0): This function captures video frames, processes them to detect hand contours, counts the fingers, and displays the results in real-time.

How it Works
# Capture Video: The video is captured frame by frame from the specified source (webcam or video file).
# Preprocess Frame: Each frame is converted to grayscale and blurred to reduce noise.
# Thresholding: Adaptive thresholding is applied to create a binary image where the hand is white, and the background is black.
# Contour Detection: Contours are detected in the binary image, and only those with a significant area are considered.
# Finger Counting: For each valid contour, the convex hull and convexity defects are calculated to determine the number of fingers raised.
# Display Results: The original frame is displayed with contours and finger counts annotated.

Contributing
Contributions are welcome! If you have any suggestions or improvements, please open an issue or submit a pull request.
