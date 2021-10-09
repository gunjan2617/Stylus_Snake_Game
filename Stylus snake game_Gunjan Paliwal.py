import cv2 as cv
import numpy as np
import pygame
import sys
import time
import os
import random
# **************************************************************************************

# Colors (R, G, B)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Initialise camera window to take HSV range of stylus
cam = cv.VideoCapture(0)
cv.namedWindow("Take HSV")

img_counter = 0

a = [0,0,0]
b = [0,0,0]
c = 0

while True :
    ret, frame = cam.read()
    frame = cv.flip(frame,1)
    print(frame.shape)
    frame = cv.putText(frame, 'Place the rect inside the stylus area',(1,110),cv.FONT_HERSHEY_DUPLEX,0.94,white,2,cv.LINE_AA)
    frame = cv.putText(frame,'Press C to continue', (120,400),cv.FONT_HERSHEY_DUPLEX,1,white,2,cv.LINE_AA)
    cv.rectangle(frame,(305,250),(320,235),(255, 0, 0),2)
    # cv.circle(frame, (305,250), 10, blue, 2)
    cv.imshow("Object Detection",frame)

    k = cv.waitKey(1)
    if k == ord('c') or k == ord('C'):
        print("Saving HSV value")
        break

# Slicing the video frame
img = frame[230:240,310:320]
img = cv.cvtColor(img,cv.COLOR_BGR2HSV)

# Averaging the HSV value
for i in range(0,10):
    for j in range(1,10):
        if img[i,j][0] != 0:
            a = a + img[i,j]
            c = c + 1
            print(img[i,j])
b = a//c
cam.release()
cv.destroyAllWindows()
# **************************************************************************************


cap = cv.VideoCapture(0)
cx1 = 0
cy1 = 0

# For finding area of the triangle
def area(x1, y1, x2, y2, x3, y3):
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)

# To check if the centroid of the stylus lies inside specific region (LEFT,RIGHT,UP,DOWN)
def check_region(x1, y1, x2, y2, x3, y3, cx, cy):
    A = area(x1, y1, x2, y2, x3, y3)
    A1 = area(cx, cy, x2, y2, x3, y3)
    A2 = area(x1, y1, cx, cy, x3, y3)
    A3 = area(x1, y1, x2, y2, cx, cy)
    if A == (A1 + A2 + A3):
        return True
    else:
        return False
# **************************************************************************************

# Initialising snake game
pygame.init()

# Declating size of snake game window
dis_width = 800
dis_height = 600

# Fixing the position of camera window and snake game window at particular position initially
os.environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % (490,30)
# os.environ['SDL_VIDEO_CENTERED'] = '500'
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

# Declaring size and speed of snake
snake_block = 10
snake_speed = 12

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Function for updating the score
def Your_score(score):
    score_value = score_font.render("Your Score: " + str(score), True, (100,200,200))
    dis.blit(score_value, [0, 0])

def snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, (50, 153, 220), [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    msg = font_style.render(msg, True, color)
    dis.blit(msg, [dis_width / 6, dis_height / 3])
# **************************************************************************************

# Main snake game loop
def gameLoop():
    # Declaring initial direction
    direction = 'RIGHT'
    change_to = direction

    cx1 = 0
    cy1 = 0

    # Closing both camera and snake game window
    game_over = False
    # Snake game ends but window is still there
    game_close = False

    # Initialising initial snake position
    x1_initial = dis_width / 2
    y1_initial = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    # Initialising random food position
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
# **********************************************************************************
    # Creating hurdles
    def hurdle_1():
        print('1')
        pygame.draw.rect(dis, [255, 255, 255], [100, 150, 450, 20])
        pygame.draw.rect(dis, [255, 255, 255], [450, 100, 20, 400])

    def hurdle_2():
        print('2')
        pygame.draw.rect(dis, [255, 255, 255], [200, 150, 400, 30])
        pygame.draw.rect(dis, [255, 255, 255], [200, 450, 400, 30])

    def hurdle_3():
        print('3')
        pygame.draw.rect(dis, [255, 255, 255], [100, 100, 200, 30])
        pygame.draw.rect(dis, [255, 255, 255], [500, 100, 200, 30])
        pygame.draw.rect(dis, [255, 255, 255], [370, 230, 30, 200])

    def hurdle_4():
        print('4')
        pygame.draw.rect(dis, [255, 255, 255], [100, 100, 200, 30])
        pygame.draw.rect(dis, [255, 255, 255], [670, 100, 30, 200])
        pygame.draw.rect(dis, [255, 255, 255], [100, 300, 30, 200])
        pygame.draw.rect(dis, [255, 255, 255], [500, 470, 200, 30])

    def hurdle_5():
        print('5')
        pygame.draw.rect(dis, [255, 255, 255], [275, 175, 50, 50])
        pygame.draw.rect(dis, [255, 255, 255], [325, 225, 50, 50])
        pygame.draw.rect(dis, [255, 255, 255], [425, 325, 50, 50])
        pygame.draw.rect(dis, [255, 255, 255], [475, 375, 50, 50])

    # Saving hurdles in a list
    hurdle = [hurdle_1, hurdle_2, hurdle_3, hurdle_4, hurdle_5]
    obs = random.choice([0, 1, 2, 3, 4])

    if obs == 0 :
        direction = 'LEFT'
    if obs == 1 :
        direction = 'RIGHT'
    if obs == 2 :
        direction = 'RIGHT'
    if obs == 3 :
        direction = 'RIGHT'
    if obs == 4 :
        direction = 'RIGHT'

#********************************************************************************
    while not game_over:

        # Initialising camera window
        ret, frame = cap.read()
        frame = cv.flip(frame, 1)
        frame = cv.resize(frame,(480,480))
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

        # Declaring lower and upper HSV value
        lower = np.array([b[0] - 50, b[1] - 50, b[2] - 50])
        upper = np.array([b[0] + 50, b[1] + 50, b[2] + 50])

        # Applying mask on the region of interest
        mask = cv.inRange(hsv, lower, upper)

        kernel = np.ones((5, 5), np.uint8)

        # Applying morphological operations
        closing = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel)
        opening = cv.morphologyEx(closing, cv.MORPH_OPEN, kernel)
        blur = cv.GaussianBlur(opening, (5, 5), 0)

        # Applying thresholding
        ret1, thresh = cv.threshold(blur, 127, 255, 0)
        contours, hierarchy = cv.findContours(thresh, 1, 2)

        # For darwing diagonal lines on camera screen to differentiate the regions (LEFT,RIGHT,UP,DOWN)
        frame = cv.line(frame, (0, 0), (480, 480), (0, 0, 0), 5)
        frame = cv.line(frame, (0, 480), (480, 0), (0, 0, 0), 5)

        # Labelling the regions (LEFT,RIGHT,UP,DOWN)
        frame = cv.putText(frame, 'LEFT', (120, 240), cv.FONT_HERSHEY_DUPLEX, 1, (255, 255, 255), 2, cv.LINE_AA)
        frame = cv.putText(frame, 'RIGHT', (300, 240), cv.FONT_HERSHEY_DUPLEX, 1, (255, 255, 255), 2, cv.LINE_AA)
        frame = cv.putText(frame, 'UP', (220, 180), cv.FONT_HERSHEY_DUPLEX, 1, (255, 255, 255), 2, cv.LINE_AA)
        frame = cv.putText(frame, 'DOWN', (190, 320), cv.FONT_HERSHEY_DUPLEX, 1, (255, 255, 255), 2, cv.LINE_AA)

        cv.imshow('Camera frame', frame)
        cv.moveWindow('Camera frame', 0, 0)
        k = cv.waitKey(20) & 0xFF
        if k == 27:
            break

        # Finding centroid of the stylus using contours
        if len(contours) > 0:
            cnt = contours[0]
            M = cv.moments(cnt)
            cx1 = int(M['m10'] / M['m00'])
            cy1 = int(M['m01'] / M['m00'])
            print(cx1, cy1)

        # Defining different regions (LEFT,RIGHT,UP,DOWN)
        left = check_region(0, 0, 240, 240, 0, 480, cx1, cy1)
        right = check_region(480, 0, 480, 480, 240, 240, cx1, cy1)
        up = check_region(0, 0, 480, 0, 240, 240, cx1, cy1)
        down = check_region(0, 480, 240, 240, 480, 480, cx1, cy1)
        print(up, down, left, right)

        while game_close == True:
            dis.fill((0, 0, 0))
            message("You Lost! Press C-Play Again or Q-Quit", (213, 50, 80))
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            # For game close and game over
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
#************************************************************************

        # For changing direction of snake using stylus depending on the region it is present
        if up:
            print('UP')
            change_to = 'UP'
        if down:
            print('DOWN')
            change_to = 'DOWN'
        if left:
            print('LEFT')
            change_to = 'LEFT'
        if right:
            print('RIGHT')
            change_to = 'RIGHT'

        # Making sure the snake cannot move in the opposite direction to its current direction
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        # Moving the snake
        if direction == 'UP':
            y1_change = -snake_block
            x1_change = 0
        if direction == 'DOWN':
            y1_change = snake_block
            x1_change = 0
        if direction == 'LEFT':
            x1_change = -snake_block
            y1_change = 0
        if direction == 'RIGHT':
            x1_change = snake_block
            y1_change = 0
#************************************************************************

        # Closing the game if snake touches the boundary of the snake game window
        if x1_initial >= dis_width or x1_initial < 0 or y1_initial >= dis_height or y1_initial < 0:
            game_close = True
        # Changing initial co-ordinates of snake
        x1_initial = x1_initial + x1_change
        y1_initial = y1_initial + y1_change
        dis.fill((0, 0, 0))
        pygame.draw.rect(dis, (0, 255, 0), [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1_initial)
        snake_Head.append(y1_initial)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        # calling hurdles
        hurdle[obs]()

        # Closing game if snake head touches the hurdle
        if (obs == 0):
            if (80 < x1_initial < 560 and 130 < y1_initial < 180) or (
                    430 < x1_initial < 480 and 80 < y1_initial < 510):
                game_close = True
        elif (obs == 1):
            if (180 < x1_initial <610 and 130 < y1_initial < 190) or (
                    180 < x1_initial <610  and 430 < y1_initial < 490):
                game_close = True
        elif (obs == 2):
            if (80 < x1_initial < 310 and 80 < y1_initial < 140) or (
                    480 < x1_initial < 710 and 80 < y1_initial < 140) or (
                    350 < x1_initial < 410 and 210 < y1_initial < 440):
                game_close = True
        elif (obs == 3):
            if (80 < x1_initial < 310 and 80 < y1_initial < 140) or (
                    650 < x1_initial < 710 and 80 < y1_initial < 310) or (
                    80 < x1_initial < 140 and 280 < y1_initial < 510) or (
                    480 < x1_initial < 710 and 450 < y1_initial < 510):
                game_close = True
        elif (obs == 4):
            if (260 < x1_initial < 330 and 160 < y1_initial < 230) or (
                    310 < x1_initial < 380 and 210 < y1_initial < 280) or (
                    410 < x1_initial < 480 and 310 < y1_initial < 380) or (
                    460 < x1_initial < 530 and 360 < y1_initial < 430):
                game_close = True

        snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        # Increasing the length of snake if it eats food
        if x1_initial == foodx and y1_initial == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Calling gameloop
gameLoop()

