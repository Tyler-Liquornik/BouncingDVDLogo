import pygame
import os
import random
import sys

pygame.init()

# Variables you can change
window_x = 900
window_y = 500
x_dimension = 200
y_dimension = 120
x_speed = y_speed = 2

window = pygame.display.set_mode((window_x, window_y))
pygame.display.set_caption("DVD Screensaver")
location = pygame.Rect(0, 0, x_dimension, y_dimension)
clock = pygame.time.Clock()


blue = pygame.transform.scale((pygame.image.load(os.path.join("Assets", "BLUE.png"))), (x_dimension, y_dimension))
green = pygame.transform.scale((pygame.image.load(os.path.join("Assets", "GREEN.png"))), (x_dimension, y_dimension))
orange = pygame.transform.scale((pygame.image.load(os.path.join("Assets", "ORANGE.png"))), (x_dimension, y_dimension))
red = pygame.transform.scale((pygame.image.load(os.path.join("Assets", "RED.png"))), (x_dimension, y_dimension))
pink = pygame.transform.scale((pygame.image.load(os.path.join("Assets", "PINK.png"))), (x_dimension, y_dimension))
yellow = pygame.transform.scale((pygame.image.load(os.path.join("Assets", "YELLOW.png"))), (x_dimension, y_dimension))


def colours_list():
    return [blue, green, orange, red, pink, yellow]


colour_input = random.choice(colours_list())


def draw(colour):
    window.fill((0, 0, 0))
    window.blit(colour, (location.x, location.y))
    pygame.display.update()


def move(colour):
    location.x += x_speed
    location.y += y_speed
    draw(colour)


def random_colour_self_exempt():
    colours_list_new = colours_list()
    colours_list_new.remove(colour_input)
    selected_colour = random.choice(colours_list_new)
    return selected_colour


running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    move(colour_input)

    if location.y == window_y - y_dimension:
        y_speed *= -1
        colour_input = random_colour_self_exempt()

    if location.y == 0:
        y_speed *= -1
        colour_input = random_colour_self_exempt()

    if location.x == window_x - x_dimension:
        x_speed *= -1
        colour_input = random_colour_self_exempt()

    if location.x == 0:
        x_speed *= -1
        colour_input = random_colour_self_exempt()
