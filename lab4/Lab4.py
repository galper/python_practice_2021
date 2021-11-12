import pygame
import math
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 600))

color_background = (220, 220, 220)
color_black = (0, 0, 0)
color_yellow = (255, 255, 0)
color_red = (255, 0, 0)

x0 = 300
y0 = 300

r_face = 200
r_eye = r_face / 6
x_left_eye = x0 - r_face / 2
y_left_eye = y0 - r_face / 5

x_right_eye = x0 + r_face / 2
y_right_eye = y0 - r_face / 5

#k_left_brow = math.tan()
#left_brow = ((100, k_left_brow * 100), (280, k_left_brow * 280), (,300), (80,120))
#right_brow =

mouth = (x_left_eye , y0 + r_face / 2, x_right_eye - x_left_eye, r_face / 6)

rect(screen, color_background, (0, 0, 600, 600))
circle(screen, color_yellow, (x0, y0), r_face)
circle(screen, color_black, (x0, y0), r_face + 2, 2)

circle(screen, color_red, (x_left_eye, y_left_eye), r_eye + 10)
circle(screen, color_black, (x_left_eye, y_left_eye), r_eye / 2)

circle(screen, color_red, (x_right_eye, y_right_eye), r_eye)
circle(screen, color_black, (x_right_eye, y_right_eye), r_eye / 2)

#polygon(screen, color_black, left_brow)
#polygon(screen, color_black, right_brow)

rect(screen, color_black, mouth)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()