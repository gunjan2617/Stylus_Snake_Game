import cv2 as cv           # Importing Libraries
import numpy as np

cap = cv.VideoCapture(0)    # Initializing the webcam.
cap.set(3, 9900)
cap.set(4, 9900)
cv.namedWindow("Trackbars")      # Create a new window for trackbars.
def pass_(x):              # Callback function for trackbars
    pass

# Creating  trackbars that will control the lower of HSV and we are keeping the upper range fixed
cv.createTrackbar("L-H", "Trackbars", 0, 179, pass_)    # For Hue the range is 0-179
cv.createTrackbar("L-S", "Trackbars", 0, 255, pass_)    # For Saturation the range is 0-255
cv.createTrackbar("L-V", "Trackbars", 0, 255, pass_)    # For Value the range is 0-255

while 1 :
    temp, frame = cap.read()
    frame = cv.flip(frame, 1)

    lh = cv.getTrackbarPos("L-H", "Trackbars")     # To get the new value of trackbars
    ls = cv.getTrackbarPos("L-S", "Trackbars")
    lv = cv.getTrackbarPos("L-V", "Trackbars")

    upper = np.array([179, 255, 255], dtype=np.uint8)       # Creating an array of lower and upper hsv values
    lower = np.array([lh, ls, lv], dtype=np.uint8)

    filtered_frame = cv.GaussianBlur(frame, (9, 9), 0)       # Removing noise of the frame
    hsv = cv.cvtColor(filtered_frame, cv.COLOR_BGR2HSV)      # Convert the BGR image to HSV image.
    apply_mask = cv.inRange(hsv, lower, upper)               # Mask operation
    bitwise = cv.bitwise_and(filtered_frame, filtered_frame, mask = apply_mask)
    mask_color = cv.cvtColor(apply_mask, cv.COLOR_GRAY2BGR)          # Converting the binary mask to BGR
    Combine_windows = np.hstack((bitwise,mask_color, filtered_frame))     # For combining all the windows in one window itself

    cv.imshow('Trackbars', cv.resize(Combine_windows, None, fx=0.35, fy=0.35))   # To show the combined frame.
    key = cv.waitKey(1)      # Press ESC to exit
    if key == 27:
        break
    elif key == ord('s'):    # Press s to print and save the hsv array
        array = [[lh, ls, lv], [179, 255, 255]]
        print(array)
        np.save('HSV_array', array)
        break

cap.release()     # Camera release
cv.destroyAllWindows()
# *********************************************************************************
HSV_array = np.load('HSV_array.npy')       # Accessing the saved HSV array
cap = cv.VideoCapture(0)                   # Initializing the webcam.
cap.set(3, 9900)
cap.set(4, 9900)
kernel = np.ones((5, 5), np.uint8)
x1, y1 = 0, 0        # Initilize x1,y1 as initial points
windows = None       # Initializing the drawing window

while True :
    ret, frame = cap.read()
    frame = cv.flip(frame, 1)
    if windows is None:        # Initialize the black drawing window of the size of frame
        windows = np.zeros_like(frame)

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV) # Convert BGR to HSV

    if True :                      # If we take the range from trackbars
        lower = HSV_array[0]
        upper = HSV_array[1]
    else:                           # Otherwise defining own custom values for upper and lower range.
        lower = np.array([26, 80, 147])
        upper = np.array([81, 255, 255])

    mask = cv.inRange(hsv, lower, upper)     # Mask operation
    mask = cv.erode(mask, kernel, iterations=1)    # Morphological operations to remove noise
    mask = cv.dilate(mask, kernel, iterations=2)

    contours, hierarchy = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)   # Finding Contours

    # checking if contour is present and also its size is bigger than the noise threshold
    if contours and cv.contourArea(max(contours,key=cv.contourArea)) > 900:  # 800 is threshold for noice
        c = max(contours, key=cv.contourArea)
        x2, y2, width, height = cv.boundingRect(c)
        # If there were no initial points then x2,y2 becomes the new initial points that is x1, y1,
        # that is when stylus appears for the first time
        if x1 == 0 and y1 == 0:
            x1, y1 = x2, y2
        else:
            windows = cv.line(windows, (x1, y1), (x2, y2), [255, 0, 0], 6) # Draw line on the windows

        x1, y1 = x2, y2       # After drawing new line the new points become the previous points.
    else:
        x1, y1 = 0, 0     # If no contours detected then x1,y1 = 0

    # frame = cv.add(frame, windows) # For writing on camera window also
    stacked = np.hstack((windows, frame))   # for writing on drawing window only
    cv.imshow('VDP', cv.resize(stacked, None, fx=0.6, fy=0.6))

    k = cv.waitKey(1) & 0xFF
    if k == 27:  # Press ESC to exit
        break
    elif k == ord('c'):      # Press c to clear the drawing window
        windows = None

cv.destroyAllWindows()
cap.release()