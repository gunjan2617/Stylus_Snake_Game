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


## Concepts Required :
**1.** Image Thersholding   
**2.** Smoothing and filtering   
**3.** Morphological Operations such as Dilation and Erosion  
**4.** Contour Detection  

# Snake Game 
Creating a snake game operated with keys 

## Structure: 
**Step 1:** Initialise the game window by declaring window parameters that is height and width.
**Step 2:** Define functions such as for the score, for snake, for output message and for the main game loop.
**Step 3:** Inside game loop initiate all the variables such as snake's initial position, bool for game close and game over,
length of snake, x and y coordinates of food, 
**Step 4:** Using loop to either continue the game or close the game according to input given.
**Step 5:** Change the direction of the snake according to LEFT,RIGHT,UP,DOWN keys given as input.
**Step 6:** Closing the game if touches the hurdle or the game window boundary or itself.
**Step 7:** Increase length of the snake if it eats the food and then generate the new food at some other position.


## Link to the video of the project
Click [here](https://drive.google.com/file/d/1fjGlOwH9nCM6ie6hgwiNMgZJCC_4Cz9e/view?usp=sharing) to view the demonstration. 
