import pygame
from Tools.FontRender import RenderFont
from Tools.PictureUploads import Loadify, TransformImage
import Initialise
import colors as C


# To do. Add a button for the screen to go black. Increase contrast and size of left and right side
# Replace tanks with other images. Have adjustable frequencies
# Live read from a file.

class MapTest(object):
    def __init__(self, screen):
        self.background_image = Loadify("Images/Backgrounds/map.jpg")
        self.background_image = TransformImage(self.background_image, Initialise.width, Initialise.height)
        self.tank1= Loadify("Images/models/tank1.png")
        self.tank1 = TransformImage(self.tank1, 325, 325)
        self.tank2=Loadify("Images/models/tank2.png")
        self.tank2 = TransformImage(self.tank2, 325, 325)
        self.tank3=Loadify("Images/models/tank3.png")
        self.tank3 = TransformImage(self.tank3, 400, 400)
        self.tank4=Loadify("Images/models/tank4.png")
        self.tank4 = TransformImage(self.tank4, 400, 400)
        self.tankblackdown= Loadify("Images/models/tank1.png")
        self.tankblackdown = TransformImage(self.tankblackdown, 325, 325)
        self.tankreddown=Loadify("Images/models/tank2.png")
        self.tankreddown = TransformImage(self.tankreddown, 325, 325)
        self.tankblackleft=Loadify("Images/models/tank3.png")
        self.tankblackleft = TransformImage(self.tankblackleft, 400, 400)
        self.tankredleft=Loadify("Images/models/tank4.png")
        self.tankredleft = TransformImage(self.tankredleft, 400, 400)
        self.tankgreendown= Loadify("Images/models/tankgreendown.png")
        self.tankgreendown = TransformImage(self.tankgreendown, 325, 325)
        self.tankgreenleft=Loadify("Images/models/tankgreenleft.png")
        self.tankgreenleft = TransformImage(self.tankgreenleft, 400, 400)
        self.heli1=Loadify("Images/models/helired.png")
        self.heli1 = TransformImage(self.heli1, 250, 250)
        self.heliblack=Loadify("Images/models/heliblack.png")
        self.heliblack = TransformImage(self.heliblack, 250, 250)
        self.heligreen=Loadify("Images/models/heligreen.png")
        self.heligreen = TransformImage(self.heligreen, 250, 250)
        self.helired=Loadify("Images/models/helired.png")
        self.helired = TransformImage(self.helired, 250, 250)
        #############
        self.screen = screen
        self.on_race_menu = True
        self.screen_width, self.screen_height = pygame.display.get_surface().get_size()
        self.button_list = []
        self.templeft = RenderFont("β", 300, C.WHITE)
        self.tempright = RenderFont("α", 300, C.WHITE)


    def DisplayWindow(self):
        self.screen.blit(self.background_image, [0, 0])

        click = False
        current_time = pygame.time.get_ticks()
        # 100
        # how long to show or hide
        delay_alpha = 95  # 500ms = 0.5s
        delay_beta = 150  # 500ms = 0.5s
        delay_theta = 50  # 500ms = 0.5s

        # time of next change
        change_time_alpha = current_time + delay_alpha
        change_time_beta = current_time + delay_beta
        change_time_theta = current_time + delay_theta
        helicoords = [900, 50]
        tank1coords = [300, 200]
        tank3coords = [1300, 500]
        # 200
        show_alpha = True
        show_beta = True
        show_theta = True
        while self.on_race_menu:
            self.screen.blit(self.tank1, tank1coords)
            self.screen.blit(self.tank3, tank3coords)
            self.screen.blit(self.heliblack, helicoords)
            alpha_detected = False
            beta_detected = True
            mx, my = pygame.mouse.get_pos()
            click = False
            # --- updates ---

            current_time = pygame.time.get_ticks()

            # is time to change ?
            if show_alpha:
                self.screen.blit(self.tank2, tank1coords)

            if show_beta:
                self.screen.blit(self.tank4, tank3coords)

            if show_theta:
                self.screen.blit(self.heli1, helicoords)

            if current_time >= change_time_alpha:
                # time of next change
                change_time_alpha = current_time + delay_alpha
                show_alpha = not show_alpha

            if current_time >= change_time_beta:
                # time of next change
                change_time_beta = current_time + delay_beta
                show_beta = not show_beta

            if current_time >= change_time_theta:
                # time of next change
                change_time_theta = current_time + delay_theta
                show_theta = not show_theta

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.on_race_menu = False
                    if event.key == pygame.K_1:
                        alpha_detected = 1
                        self.tank2 = self.tankgreendown
                    if event.key == pygame.K_2:
                        beta_detected = 1
                        self.tank4 = self.tankgreenleft
                    if event.key == pygame.K_3:
                        theta_detected = 1
                        self.heli1 = self.heligreen
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_1:
                        alpha_detected = 1
                        self.tank2 = self.tankreddown
                    if event.key == pygame.K_2:
                        alpha_detected = 1
                        self.tank4 = self.tankredleft
                    if event.key == pygame.K_3:
                        theta_detected = 1
                        self.heli1 = self.helired

            pygame.display.update()

