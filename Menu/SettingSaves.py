import pygame

def GetRes():
    res_file = open("Data/Settings/visual", "r")
    res_list = res_file.read().splitlines()
    res_file.close()
    return res_list
