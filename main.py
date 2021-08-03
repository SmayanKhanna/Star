#author - Smayan Khanna
#Date Completed - 29th June 2021

import pygame
import random
import math
from pygame.locals import *

pygame.init()

#variables
width = 1280
height = 720
run = True
star_size = 1
keyboard_vel = 1
rectangles = []
star_classification = 'O'

#spectrum variables
rectangles = []
position = [350, 600]
size = [1, 60]
color = [0,0,0]
count = 0

#colours
dark_blue = (0,50,150)
white = (255,255,255)
yellow = (255,255,0)
black = (0,0,0)

#font
font = pygame.font.SysFont('times new roman', 20)
title_font = pygame.font.SysFont('times new roman', 60)
screen = pygame.display.set_mode((width, height))
caption = pygame.display.set_caption('Star Simulation')
star_colour = [white, yellow]

class Spectrum(object):

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.x = 350
        self.y = 600

    def draw(self, screen):
        pygame.draw.rect(screen, black, pygame.Rect(350, 600, self.width, self.height))

class Star(object):

    def __init__(self, radius):
        self.x = 640
        self.y = 400
        self.radius = radius
        self.temperature = 2000
        self.colour = [255,255,0]

    def draw(self, screen):
        pygame.draw.circle(screen, list(self.colour), (self.x,self.y), self.radius)

class button(object):

    def __init__(self, x):
        self.x = x
        self.y = 150
        self.radius = 10

    def draw(self, screen):
        pygame.draw.circle(screen, black, (self.x, self.y), self.radius)

class Rectangle:

    def __init__(self, pos, size, color):
        self.pos = pos
        self.color = color
        self.size = size

    def draw(self):
        pygame.draw.rect(screen, list(self.color), Rect(self.pos, self.size))

#credit to user3679917 on stackoverflow for helping with rendering multiple rectangles
for count in range(1020):
    position[0] += 0.588
    count += 1

    if count <254:
        color[0] += 1

    if count >254 and color[0]>0:
        color[0] -= 1
        color[1] += 1

    if count > 508 and color[1] > 0:
        color[2] += 1
        color[1] -= 1

    if count > 763:
        color[0] += 1.5
        color[2]= 255
        print(color[0])

    rectangles.append(Rectangle(list(position), list(size), list(color)))

def draw():
    #variables
    circle_count = 0

    #drawings
    screen.fill(dark_blue)

    x, y = random.randint(1,1200), random.randint(1,720)
    radius = random.randint(1,5)

    #flashing stars
    while circle_count < 1000:

        pygame.draw.circle(screen,random.choice(star_colour),(x,y),radius)
        circle_count = circle_count + 1

    pygame.draw.line(screen,white,(200,150),(1000,150), 3)
    main_button.draw(screen)
    main_star.draw(screen)
    main_spectrum.draw(screen)

    text = font.render('Size of Star: ' + str(star_size) +' Solar Radii', 1, white)
    classification = font.render('Class: ' + star_classification, 1,white)
    temperature = font.render('Temp: ' + str(main_star.temperature) + 'K', 1, white)
    title = title_font.render('Star Simulator',1,white)
    sun = font.render('Sun for Reference',1,white)
    spectrum = font.render('Star Spectrum', 1, white)

    screen.blit(title, (450, 50))
    screen.blit(classification,(1020,175))
    screen.blit(temperature, (1020, 215))
    screen.blit(text, (1020,135))
    screen.blit(sun, (235, 360))
    screen.blit(spectrum, (350, 560))
    pygame.draw.circle(screen, yellow, (300,400), 13)

    #drawing spectrum

    for rectangle in rectangles:
        rectangle.draw()

    #transparent - credit to StackOverflow user Gustavo Girealdez

    transparent = pygame.Surface((300, 60))
    transparent.set_alpha(200)
    transparent.fill((0, 0, 0))
    screen.blit(transparent, (-0.373*main_button.x + 723.13, 600))

    pygame.display.update()

main_button = button(500)
main_star = Star(40)
main_spectrum = Spectrum(600, 60)

while run:

    #calculations/colour scales

    star_size = round((0.0177* main_button.x) -2.8,1)
    main_star.radius = star_size * 13
    main_star.temperature = round(38.324*main_button.x -4328,0)
    main_star.colour[2] = (main_button.x - 196)/3.65
    main_star.colour[1] = (1000 - main_button.x )/5
    main_star.colour[0] = (1000 - main_button.x )/3.65
    main_button.draw(screen)
    draw()

    # classifications

    if star_size <= 0.07:
        star_classification = "M"
    elif star_size <= 0.96:
        star_classification = "K"
    elif star_size <= 1.15:
        star_classification = "G"
    elif star_size <= 1.4:
        star_classification = "F"
    elif star_size <= 1.8:
        star_classification = "A"
    elif star_size <= 6.6:
        star_classification = "B"
    else:
        star_classification = "O"

    #user interaction

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEMOTION and pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            dist = math.sqrt((main_button.x - mouse_x) ** 2 + (main_button.y - mouse_y) ** 2)
            if dist < main_button.radius + 30:
                if main_button.x > 196 and main_button.x < 1000:
                    main_button.x = mouse_x
                    if main_button.x <= 196:
                        main_button.x += 20
                    if main_button.x >= 1000:
                        main_button.x -= 20

pygame.quit()
