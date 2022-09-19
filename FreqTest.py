import pygame
from Tools.FontRender import RenderFont
import colors as C

class FreqTest(object):
    def __init__(self, screen):
        self.screen = screen
        self.on_race_menu = True
        self.screen_width, self.screen_height = pygame.display.get_surface().get_size()
        self.button_list = []
        self.templeft = RenderFont("β", 300, C.WHITE)
        self.tempright = RenderFont("α", 300, C.WHITE)

    def DrawButtons(self):

        for num in range(2):
            self.button_list.append(pygame.Rect(((self.screen_width + 250)/2) * num+215, (self.screen_height - 100)/2, 400, 100))

        self.button_list.append(
            pygame.Rect(((self.screen_width + 250) / 3) , (self.screen_height / 2)-100, 800, 100))

        self.button_list.append(
            pygame.Rect(((self.screen_width) /2) , (self.screen_height / 2)-110, 5, 120))

    def DisplayWindow(self):
        self.DrawButtons()
        click = False
        current_time = pygame.time.get_ticks()
        # 100
        # how long to show or hide
        delay_alpha = 62.5  # 500ms = 0.5s
        delay_beta = 20  # 500ms = 0.5s

        # time of next change
        change_time_alpha = current_time + delay_alpha
        change_time_beta = current_time + delay_beta
        # 200
        show_alpha = True
        show_beta = True
        while self.on_race_menu:
            self.screen.fill(C.LGREY)
            pygame.draw.circle(self.screen, C.WHITE, self.button_list[0].center, 420)
            pygame.draw.circle(self.screen, C.WHITE, self.button_list[1].center, 420)

            # --- updates ---
            current_time = pygame.time.get_ticks()

            # is time to change ?
            if show_alpha:
                pygame.draw.circle(self.screen, C.BLACK, self.button_list[1].center, 400)

            if show_beta:
                pygame.draw.circle(self.screen, C.BLACK, self.button_list[0].center, 400)

            if current_time >= change_time_alpha:
                # time of next change
                change_time_alpha = current_time + delay_alpha
                show_alpha = not show_alpha

            if current_time >= change_time_beta:
                # time of next change
                change_time_beta = current_time + delay_beta
                show_beta = not show_beta

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.on_race_menu = False

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_BACKSPACE:
                        pressed = True
                        while pressed:
                            self.screen.fill(C.BLACK)
                            pygame.display.update()
                            for event1 in pygame.event.get():
                                if event1.type == pygame.KEYUP:
                                    pressed = False
            pygame.display.update()

