import pygame, sys
from pygame.locals import *
from config import *
 
pygame.init()
 
FramePerSec = pygame.time.Clock()

infoObject = pygame.display.Info()
DISPLAYSURF = pygame.display.set_mode(
    (infoObject.current_w, infoObject.current_h), 
    pygame.RESIZABLE)
DISPLAYSURF.fill(BLACK)
pygame.display.set_caption("SSVEP Stimulation")

class Box:
    def __init__(self, color, x_fraction, y_fraction, side_fraction, frequency, current_time):
        self.color = color
        self.x_fraction = x_fraction
        self.y_fraction = y_fraction
        self.side_fraction = side_fraction
        self.delay = ((1/frequency)*1000) / 2
        self.change_time = current_time + self.delay
        self.show = True

    def update(self, current_time):
        if current_time >= self.change_time:
             self.change_time = current_time + self.delay
             self.show = not self.show

    def draw(self, surface):
        if not self.show:
            return

        surface_width, surface_height = surface.get_size()

        side_size = min(surface_width, surface_height) * self.side_fraction

        x = (surface_width * self.x_fraction) - (side_size / 2)
        y = (surface_height * self.y_fraction) - (side_size / 2)
        w = side_size
        z = side_size

        pygame.draw.rect(surface, self.color, pygame.Rect(x, y, w, z))

def main():
    current_time = pygame.time.get_ticks()
    boxes = []
    for box_data in BOXES:
        box = Box(box_data[0], box_data[1], 
                    box_data[2], box_data[3], 
                    box_data[4], current_time)
        boxes.append(box)

    while True:     
        for event in pygame.event.get(): 
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        current_time = pygame.time.get_ticks()

        # Update objects
        for box in boxes:
            box.update(current_time)
        
        # Make objects update screen
        DISPLAYSURF.fill(BLACK)
        for box in boxes:
            box.draw(DISPLAYSURF)
                
        pygame.display.update()
        FramePerSec.tick(FPS)

main()