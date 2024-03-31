import math
import pygame
import random

speed = int(input("Enter speed of square: "))
height = int(input("Enter height of window: "))
width = int (input("Enter width of window:"))
if height > 1080:
    height = 1080
if width > 1920:
    width = 1920

#initialise the main variables
recwidth = 50
recheight = 50
posx = random.randint(0, width - recwidth)
posy = random.randint(0, height - recheight)
i=0

velocity_x = speed
velocity_y = speed

# Define wall dimensions
wall_thickness = 10
WHITE = (255, 255, 255)

# pygame setup
pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True
pygame.display.set_caption("Bouncing Square")

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    i +=1
    red=math.floor(math.sqrt(pow(math.sin(i/100),2))*255)
    green=math.floor(math.sqrt(pow(math.sin((i/100)+3.1415/3),2))*255)
    blue=math.floor(math.sqrt(pow(math.sin((i/100)+3.1415*2/3),2))*255)
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # Draw the object with the current color
    square = pygame.draw.rect(screen, (red,green,blue), (posx, posy, recwidth, recheight))

    posx += velocity_x
    posy += velocity_y

    if posx <= 0 or posx >= width - recwidth:
        velocity_x = -velocity_x
    if posy <= 0 or posy >= height - recheight:
        velocity_y = -velocity_y

    #wow it work OwO
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(180)  # limits FPS to 180

pygame.quit()