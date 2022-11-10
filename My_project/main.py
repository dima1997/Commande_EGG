import pygame, sys
from pygame.locals import *
import random
 
pygame.init()
 
FPS = 60
FramePerSec = pygame.time.Clock()
 
# Predefined some colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
# Screen information
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

infoObject = pygame.display.Info()
DISPLAYSURF = pygame.display.set_mode(
    (infoObject.current_w, infoObject.current_h), 
    pygame.RESIZABLE)
DISPLAYSURF.fill(BLACK)
pygame.display.set_caption("SSVEP Stimulation")

BOX_SCREEN_FRACTION = 0.1
BOX_CENTER_Y_SCREEN_FRACTION = 0.5
RED_BOX_CENTER_X_SCREEN_FRACTION = 0.25
BLUE_BOX_CENTER_X_SCREEN_FRACTION = 0.75

RED_FREQUENCY = 15
BLUE_FREQUENCY = 25

class Box:
    def __init__(self, color, center_x_surface_fraction, frequency, current_time):
        self.color = color
        self.center_x_surface_fraction = center_x_surface_fraction
        self.delay = ((1/frequency)*1000) / 2
        self.time = current_time + self.delay
        self.show = True

    def update(self, current_time):
        if current_time >= self.time:
             self.time = current_time + self.delay
             self.show = not self.show

    def draw(self, surface):
        if not self.show:
            return

        surface_width, surface_height = surface.get_size()

        side_size = min(surface_width, surface_height) * BOX_SCREEN_FRACTION 

        x = (surface_width * self.center_x_surface_fraction) - (side_size / 2)
        y = (surface_height * BOX_CENTER_Y_SCREEN_FRACTION) - (side_size / 2)
        w = side_size
        z = side_size

        pygame.draw.rect(surface, self.color, pygame.Rect(x, y, w, z))

def main():
    current_time = pygame.time.get_ticks()
    red_box = Box(RED, RED_BOX_CENTER_X_SCREEN_FRACTION, RED_FREQUENCY, current_time)
    blue_box = Box(BLUE, BLUE_BOX_CENTER_X_SCREEN_FRACTION, BLUE_FREQUENCY, current_time)

    while True:     
        for event in pygame.event.get(): 
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        current_time = pygame.time.get_ticks()

        # Update objects
        red_box.update(current_time)
        blue_box.update(current_time)
        
        # Make objects update screen
        DISPLAYSURF.fill(BLACK)
        red_box.draw(DISPLAYSURF)
        blue_box.draw(DISPLAYSURF)
                
        pygame.display.update()
        FramePerSec.tick(FPS)

main()