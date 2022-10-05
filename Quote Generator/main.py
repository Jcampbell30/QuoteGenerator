import random
import pygame
import os
import re



# Define the background colour
# using RGB color coding.
pygame.init()
green = (0, 255, 0)
blue = (0, 0, 128)
white = (255, 255, 255)
crimson = (220,20,60)
yellow = (255,185,15)
purple = (153,50,204)



myStrings = ['Maddie','Jared','Karen', 'Arwen', 'Markia']
colors = [blue,crimson,green,yellow,purple]

background_colour = (white)

# opening the file in read mode
txtFile = open('quotes.txt',encoding="utf8")
data = txtFile.read()
txtFile.close()
myarray = data.split("\n\n")
list1 = []
i = 0
while i < len(myarray):
    if len(myarray[i]) < 100:
        list1.append(myarray[i].replace('\n',""))
    i+=1


X = 1200
Y = 800
# Define the dimensions of
# screen object(width,height)
screen = pygame.display.set_mode((X, Y))
print(len(myarray))
print("the number of my quotes are:",len(list1))

# Set the caption of the screen
pygame.display.set_caption('Click_A_Quote!')

# Fill the background colour to the screen
screen.fill(background_colour)
font = pygame.font.SysFont('arial.ttf', 32)

print(myarray)


text = font.render(random.choice(list1), True, random.choice(colors))

# create a rectangular object for the
# text surface object
textRect = text.get_rect()

# set the center of the rectangular object.
textRect.center = (X // 2, Y // 2)

# Update the display using flip
pygame.display.flip()

# Variable to keep our game loop running
running = True
rectangle_dragging = False
# game loop
while running:
    screen.blit(text, textRect)
    for color in colors:
        if color == background_colour:
            colors.remove(color)
    # for loop through the event queue
    for event in pygame.event.get():


        # Check for QUIT event
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if textRect.collidepoint(event.pos):
                    rectangle_dragging = True
                    mouse_x, mouse_y = event.pos
                    offset_x = textRect.x - mouse_x
                    offset_y = textRect.y - mouse_y
                    text = font.render(random.choice(list1), True, random.choice(colors))
                    screen.fill(background_colour)


        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                rectangle_dragging = False



        elif event.type == pygame.MOUSEMOTION:
            if rectangle_dragging:
                mouse_x, mouse_y = event.pos
                textRect.x = mouse_x + offset_x
                textRect.y = mouse_y + offset_y
                screen.fill(background_colour)





    pygame.display.update()