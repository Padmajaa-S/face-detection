# Face Detection with OpenCV

This project demonstrates how to perform face detection using OpenCV's Haar cascades. The application captures video from the default camera, detects faces in real-time, draws rectangles around detected faces, and saves the detected face images to a directory.

## Features

- Real-time face detection using OpenCV's Haar cascades.
- Captures video stream from the default camera.
- Draws rectangles around detected faces.
- Saves the detected face images in a specified directory.

## Project Structure

- `face_detection.py`: The main Python script that runs the face detection application.
- `detected_faces/`: Directory to store the detected face images.


Install the required packages:
    ```sh
    pip install opencv-python
    ```

## Usage

1. Run the face detection script:
    ```sh
    python face_detection.py
    ```

2. The application will start capturing video from the default camera.

3. Faces detected in the video stream will be highlighted with rectangles, and the cropped face images will be saved in the `detected_faces` directory.

4. Press 'q' to stop the video capture and close the application.

## Code Overview

The main steps of the face detection script are:

1. **Initialize Video Capture**: Captures video from the default camera (camera index 0).
    ```python
    video_capture = cv2.VideoCapture(0)
    ```

2. **Load Haar Cascades**: Loads OpenCV's pre-trained Haar cascades for face detection.
    ```python
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    ```

3. **Process Video Frames**: Reads frames from the video stream, converts them to grayscale, and detects faces.
    ```python
    ret, frame = video_capture.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    ```

4. **Draw Rectangles and Save Faces**: Draws rectangles around detected faces and saves the cropped face images.
    ```python
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        face_image = frame[y:y+h, x:x+w]
        filename = os.path.join(output_dir, f"face_{len(os.listdir(output_dir))}.jpg")
        cv2.imwrite(filename, face_image)
    ```

5. **Display the Video Stream**: Displays the video stream with detected faces.
    ```python
    cv2.imshow('Video', frame)
    ```

6. **Cleanup**: Releases the video capture and closes all OpenCV windows when 'q' is pressed.
    ```python
    video_capture.release()
    cv2.destroyAllWindows()
    ```

## Contact

For any questions or inquiries, please contact [padmajaatms@gmail.com](padmajaatms@gmail.com).

