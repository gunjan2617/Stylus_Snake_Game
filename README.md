# Virtual_Drawing_Pad
We will create a virtual drawing pad (VDP) that will track an object for drawing on the screen. 

## Structure: 
**Step 1:** Find the HSV upper and the lower range of the object to be tracked using trackbars.   
**Step 2:** Applying filters to reduce noice of the frame.  
**Step 3:** Saving the HSV range of the object to be used further in the code.   
**Step 4:** load the HSV value and capture the video.  
**Step 5:** Read video and apply suitable morphological operations.   
**Step 6:** Find the object’s x,y coordinates to draw on the screen.  
**Step 8:** Detect and track the object with contour detection.  

<img src="https://user-images.githubusercontent.com/88222317/136737452-e78d8dbe-fcbf-4203-8728-8dd554ae466b.png" data-canonical-src="https://user-images.githubusercontent.com/88222317/136737452-e78d8dbe-fcbf-4203-8728-8dd554ae466b.png" width="650" height="150" />



## Concepts Required :
**1.** Image Thersholding   
**2.** Smoothing and filtering   
**3.** Morphological Operations such as Dilation and Erosion  
**4.** Contour Detection  


# Snake_Game 
Creating a snake game operated with keys 

## Structure:   
**Step 1:** Initialise the game window by declaring window parameters that is height and width.  
**Step 2:** Define functions such as for the score, for snake, for output message and for the main game loop.  
**Step 3:** Inside game loop initiate all the variables such as snake's initial position, bool for game close and game over,
length of snake, x and y coordinates of food.   
**Step 4:** Using loop to either continue the game or close the game according to input given.  
**Step 5:** Change the direction of the snake according to LEFT,RIGHT,UP,DOWN keys given as input.  
**Step 6:** Closing the game if touches the hurdle or the game window boundary or itself.  
**Step 7:** Increase length of the snake if it eats the food and then generate the new food at some other position.  

<img src="https://user-images.githubusercontent.com/88222317/136739895-f3aaedca-1608-44f1-86f3-f5e8fc3c2340.png" data-canonical-src="https://user-images.githubusercontent.com/88222317/136739895-f3aaedca-1608-44f1-86f3-f5e8fc3c2340.png" width="250" height="250" />


# Stylus_Snake_Game  
The VDP code and snake game code has to be linked

## Structure:  
**Step 1:** Using ROI , take the HSV value of the stylus and average all the values. This is to avoid manually feeding HSV value through trackbars.  
**Step 2:** Define four regions on camera window (LEFT,RIGHT,UP,DOWN).  
**Step 3:** Check if the centroid of the stylus lies inside the region defined. 
**Step 4:** Remove the key part from the snake game code to use stylus.
**Step 5:** Use the cetroid obtained from contours and pass it to the function used for checking the region.  
**Step 6:** Insert hurdles by defining the wall range in x direction and y direction and build up a logic for closing the game if snake touches the hurdle.  
**Step 7:** In this way stylus gets linked to the snake game.

<img src="https://user-images.githubusercontent.com/88222317/136739953-27fbf93c-10e5-4714-b830-85949ca8bee8.png" data-canonical-src="https://user-images.githubusercontent.com/88222317/136739953-27fbf93c-10e5-4714-b830-85949ca8bee8.png" width="200" height="200" />

![Alt Text]((https://user-images.githubusercontent.com/88222317/137592223-ddf9dbf7-e8df-4aa9-a799-8ca12ad58a32.gif)

<img src="https://user-images.githubusercontent.com/88222317/136740038-152f74c1-1149-4f84-98fe-baf86739c25e.png" data-canonical-src="https://user-images.githubusercontent.com/88222317/136740038-152f74c1-1149-4f84-98fe-baf86739c25e.png" width="400" height="200" />

## Concepts Required :
**Step 1:** Use of ROI and image thresholding  
**Step 2:** pygame concepts   


## Link to the video of the project
Click [here](https://drive.google.com/drive/folders/1QKNdxNRJIFjskXf8WHzYAuR21d4I_RGY?usp=sharing) to view the demonstration. 
