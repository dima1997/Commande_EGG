import Initialise
import pygame
from Tools.FontRender import RenderFontBold
from Tools.PictureUploads import Loadify, TransformImage
from FreqTest import FreqTest
from MapTest import MapTest
from LeftRightTest import LeftRightTest
from Menu.SettingSaves import GetRes
from SettingsMenuEEG import ParameterMenu

"""Main Menu"""
def MainMenu(screen):
    background_image = Loadify("Images/Backgrounds/nebula.png")
    background_image = TransformImage(background_image, Initialise.width, Initialise.height)

    LBLUE = (0, 204, 204)
    WHITE = (255,255,255)

    width = int(GetRes()[0])
    height = int(GetRes()[1])

    font1 = RenderFontBold("Frequency Test", 57, WHITE)
    font2 = RenderFontBold("Left/Right Test", 57, WHITE)
    font3 = RenderFontBold("Map Test", 57, WHITE)
    font4 = RenderFontBold("Settings", 30, WHITE)
    font4 = pygame.transform.rotate(font4, -90)

    button_width = 500
    button_length = 250

    font1coords = [width/2-button_width/2, (4*height)/18-button_length/2, button_width, button_length]
    font2coords = [width/2-button_width/2, (9*height)/18-button_length/2, button_width, button_length]
    font3coords = [width/2-button_width/2, (14*height)/18-button_length/2, button_width, button_length]
    font4coords = [width/2-button_width/2+button_width+25, (14*height)/18-button_length/2, button_width/5, button_length]
    button_list = []
    button_list.append(pygame.Rect(font1coords))
    button_list.append(pygame.Rect(font2coords))
    button_list.append(pygame.Rect(font3coords))
    button_list.append(pygame.Rect(font4coords))


    on_main_menu = True
    click = False
    while on_main_menu:

        screen.blit(background_image, [0, 0])

        mx, my = pygame.mouse.get_pos()
        for button in button_list:
            pygame.draw.rect(screen, (180, 180, 180), button,10)
            if button.collidepoint(mx, my):
                pygame.draw.rect(screen, (50, 200, 100), button,6)
                if click:
                    show =True
                    if button_list.index(button) == 0:
                        FreqTest(screen).DisplayWindow()

                    if button_list.index(button) == 1:
                        LeftRightTest(screen).DisplayWindow()

                    if button_list.index(button) == 2:
                        MapTest(screen).DisplayWindow()

                    if button_list.index(button) == 3:
                        ParameterMenu(screen).DisplayWindow()


        screen.blit(font1, [font1coords[0]+45,font1coords[1]+95])
        screen.blit(font2, [font2coords[0]+45,font2coords[1]+95])
        screen.blit(font3, [font3coords[0]+125,font3coords[1]+95])

        screen.blit(font4, [font4coords[0] + 35, font4coords[1] + 50])

        click = False
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Game quits if user presses escape on the main screen
                    pygame.quit()
                    quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()


MainMenu(Initialise.screen)
