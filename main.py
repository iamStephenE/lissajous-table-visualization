# importing all needed modules
import pygame
from lissajous import Lissajous

# initializing pygame
pygame.init()

# Permanent variables: Scale, each block size, width, height, dimensions
WIDTH = 1000
HEIGHT = 1000
DIMENSIONS = (WIDTH, HEIGHT)

BLACK = (0, 0, 0)

# Setting up pygame
screen = pygame.display.set_mode(DIMENSIONS)
pygame.display.set_caption('Lissajous Table Visualization')

FRAMES = int(1000/100)

# -----------------------------------------------------------------------

num_of_curves = 10
base_angle = 0.01
curves = Lissajous(WIDTH, num_of_curves, base_angle, 1)

# Game loop
while True:
    pygame.time.delay(FRAMES)
    screen.fill(BLACK)

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()

    curves.update()
    curves.render(pygame, screen)

    pygame.display.update()




