import pygame
import os


def Loadify(img):
    return pygame.image.load(img).convert_alpha()


def TransformImage(img, x, y):
    return pygame.transform.scale(img, [x,y])


def LoadUpgradeBars(): # Not used
    bar_list = []
    upgrade_bar = pygame.image.load("Images/UpgradeBars/Upgrade bar unlit.png").convert_alpha()
    upgrade_bar = TransformImage(upgrade_bar, 400, 75)
    bar_list.append(upgrade_bar)
    for image in range(10):
        upgrade_bar = pygame.image.load("Images/UpgradeBars/Upgrade bar t" + str(image+1) + ".png").convert_alpha()
        upgrade_bar = TransformImage(upgrade_bar, 400, 75)
        bar_list.append(upgrade_bar)
    return bar_list


def LoadUpgradeButtons(): # Not used
    button_list = []
    for image in range(9):
        button = pygame.image.load("Images/Buttons/Upgrade Button" + str((image + 1)) + ".png")
        button = TransformImage(button, 120, 60)
        button_list.append(button)
    button_list_1 = button_list[::-1]
    button_list = button_list + button_list_1
    return button_list


def LoadUpgradeLevels(): # Not used
    level_list = []
    for image in range(11):
        level = Loadify("Images/UpgradeLevel/upgrade level " + str(image) + ".png")
        level = TransformImage(level, 80, 80)
        level_list.append(level)
    return level_list









