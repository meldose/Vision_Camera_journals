import cv2 # import OpenCV module
import numpy as np # import NumPy module

# Function to initialize the camera
def initialize_camera(camera_index=0): # defined an function to initialize the camera and set camera index to 0
    cap = cv2.VideoCapture(camera_index) # create a video capture object
    if not cap.isOpened(): # if camera not found
        print("Error: Camera not detected.") # print error message
        return None
    return cap

# Function to process the frame
def process_frame(frame): # defined a function to process the frame
    
    
    # Convert to grayscale (example of processing)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # set the frame to grayscale
    
    
    # Thresholding (simple binary segmentation example)
    _, thresh = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY) # set the frame to binary
    
    
    # Contour detection to find objects
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # find contours
    
    
    # Draw bounding boxes around detected objects
    for cnt in contours: # check if contours exist
        x, y, w, h = cv2.boundingRect(cnt) # get bounding box coordinates
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2) # draw bounding box
    
    # Here you can integrate a machine learning model to classify objects
    # For example: class_label = classify_item(frame[x:x+w, y:y+h])

    return frame, contours # return the processed frame and contours

# Function to sort items based on detection
def sort_item(contours): # defined a function to sort items based on detection
    # Based on object detection and classification, control the sorting mechanism
    for cnt in contours: # check if contours exist
        x, y, w, h = cv2.boundingRect(cnt) # get bounding box coordinates
        # Example logic to sort based on the position of the object
        if x < 100: # check if object is in the left side
            print("Move object to left side")
        elif x > 200: # check if object is in the right side
            print("Move object to right side")
        else:
            print("Keep object in the middle") # if object is in the middle, keep it in the middle

# Main loop
def main(): # defined a main loop
    cap = initialize_camera() # set the camera

    if cap is None: # if camera not found
        return

    while True: # set infinite loop
        ret, frame = cap.read() # read the frame
        if not ret: # if frame not read
            print("Failed to grab frame") # print error message
            break

        # Process the frame to detect objects
        processed_frame, contours = process_frame(frame)

        # Perform sorting logic
        sort_item(contours)

        # Show the frame with object detection
        cv2.imshow("Conveyor Belt", processed_frame) # show the frame

        # Exit on pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'): # wait for 1 millisecond and check if 'q' key is pressed
            break

    cap.release() # release the camera
    cv2.destroyAllWindows() # close all OpenCV windows

if __name__ == "__main__": # check if the script is being run directly
    main() # call the main function
