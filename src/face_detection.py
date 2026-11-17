import cv2
import os
from datetime import datetime

folder_path = 'imgs'
os.makedirs(folder_path, exist_ok=True)

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

file_count = 0
while rval: 
    cv2.imshow("preview", frame)
    rval, frame = vc.read()
    key = cv2.waitKey(20)

    if key == 27: # exit on ESC
        break
    if key == ord('q'):
        # Get the current time to use as a file name
        current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
        # Construct the file path
        file_name = os.path.join(folder_path, f'IMG_{current_time}.jpg')
        # Check if the file already exists
        while os.path.exists(file_name):
            # If the file exists, increment the file count
            file_count += 1
            # Construct a new file name
            file_name = os.path.join(folder_path, f'IMG_{current_time}_{file_count}.jpg')
        # Save the frame as an image
        cv2.imwrite(file_name, frame)
        print("Photo Success!")

vc.release()
cv2.destroyWindow("preview")
