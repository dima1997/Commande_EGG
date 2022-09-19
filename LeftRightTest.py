import pygame
from Tools.FontRender import RenderFont
import colors as C


class LeftRightTest(object):
    def __init__(self, screen):
        self.screen = screen
        self.on_race_menu = True
        self.screen_width, self.screen_height = pygame.display.get_surface().get_size()
        self.button_list = []
        self.templeft = RenderFont("L", 300, C.WHITE)
        self.tempright = RenderFont("R", 300, C.WHITE)

    def DrawButtons(self):

        for num in range(2):
            self.button_list.append(pygame.Rect(((self.screen_width + 250)/2) * num + 200, (self.screen_height - 200)/2, 400, 100))

        self.button_list.append(
            pygame.Rect(((self.screen_width + 250) / 3) - 180, (self.screen_height / 2)-100, 800, 100))

        self.button_list.append(
            pygame.Rect(((self.screen_width) /2) -15 , (self.screen_height / 2)-110, 5, 120))

    def DisplayWindow(self):
        self.DrawButtons()

        while self.on_race_menu:
            alpha_detected = False
            beta_detected = True
            mx, my = pygame.mouse.get_pos()
            self.screen.fill(C.LGREY)
            pygame.draw.rect(self.screen, C.RED, self.button_list[2])
            pygame.draw.circle(self.screen, C.GREY, self.button_list[0].center, 200)
            pygame.draw.circle(self.screen, C.GREY, self.button_list[1].center, 200)
            click = False
            self.screen.blit(self.templeft, [self.button_list[0].center[0]-75,self.button_list[0].center[1]-150])
            self.screen.blit(self.tempright, [self.button_list[1].center[0]-80,self.button_list[2].center[1]-150])

            pygame.draw.rect(self.screen, C.GREEN, self.button_list[3], 15)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.on_race_menu = False
                    if event.key == pygame.K_RIGHT:
                        print("Right")
                        self.button_list[3].move_ip(20,0)
                    if event.key == pygame.K_LEFT:
                        print("Left")
                        self.button_list[3].move_ip(-20, 0)

            pygame.display.update()





