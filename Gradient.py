# a very simple program on how I created the spectrum/gradient
import pygame
from pygame.locals import *
from sys import exit
from random import *

pygame.init()

screen = pygame.display.set_mode((640, 480), 0,32)

class Rectangle:
    def __init__(self, pos, size, color):
        self.pos = pos
        self.color = color
        self.size = size

    def draw(self):
        pygame.draw.rect(screen, list(self.color), Rect(self.pos, self.size))

rectangles = []

position = [50, 80]
size = [1, 30]
color = [0,0,0]
count = 0

for count in range(1020):
    position[0] += 0.5
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

    rectangles.append(Rectangle(list(position), list(size),list(color)))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    screen.lock()
    for rectangle in rectangles:
        rectangle.draw()
    screen.unlock()
    pygame.display.update()
