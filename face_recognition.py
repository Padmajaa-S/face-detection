import cv2
import os

# Create a directory to store detected faces
output_dir = 'detected_faces'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Initialize video capture
video_capture = cv2.VideoCapture(0)  # 0 for default camera

# Load OpenCV's Haar cascades for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    # Capture each frame of the video stream
    ret, frame = video_capture.read()
    
    # Check if the frame is not empty
    if not ret:
        break
    
    # Convert the frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces using OpenCV's Haar cascades
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    # Process each detected face
    for (x, y, w, h) in faces:
        # Draw a rectangle around the detected face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
        # Crop the detected face region
        face_image = frame[y:y+h, x:x+w]
        
        # Save the cropped face image
        filename = os.path.join(output_dir, f"face_{len(os.listdir(output_dir))}.jpg")
        cv2.imwrite(filename, face_image)
    
    # Display the frame with detected faces
    cv2.imshow('Video', frame)
    
    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture and close all OpenCV windows
video_capture.release()
cv2.destroyAllWindows()
