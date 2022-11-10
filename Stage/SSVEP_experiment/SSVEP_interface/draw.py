from cv2 import displayOverlay
import pygame
import time
import os
import random
import numpy as np
from datetime import datetime


pygame.font.init()

WIDTH,HEIGHT = 1200, 750
FPS = 60
#buttons creation

#fonts
button_font_size = 30
button_font = pygame.font.SysFont(os.path.join('fonts','LinBiolinum_R.ttf'), button_font_size)
HEIGHT_BUTTONS = button_font_size + 20
level_font = pygame.font.SysFont(os.path.join('fonts','LinBiolinum_R.ttf'), 50)
level_x,level_y=20,30
#colors
CYAN = (4,196,217)
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)

def consigne(WIN,sec,liste_consigne):
    WIN.fill(BLACK)
    width,height = 200,150
    x,y = 30, HEIGHT - height - 30
    
    #cadre rouge + texte
    rectangle = pygame.Rect(x,y,width,height)
    pygame.draw.rect(WIN,RED,rectangle,5,5)
    consigne_text = button_font.render("Consigne:",1,WHITE)
    WIN.blit(consigne_text,(x+10,y+10))
    
    #ordre dans lequel il faut les regarder
    #consigne à afficher
    num = np.int(sec//20)
    if num >= len(liste_consigne):
        run = False
    else :
        display = liste_consigne[num]
        consigne_2nd = button_font.render(display,1,WHITE)
        WIN.blit(consigne_2nd,(x+width/2-consigne_2nd.get_width()/2,y+height/2-consigne_2nd.get_height()/2))
    

def window(WIN,count,f_a,f_b,WHITE,sec_g,tabs):
    
    common_size = 200
    #button_a = pygame.Rect(WIDTH/2-2*common_size,HEIGHT/2-common_size/2,200,200)
    #button_b = pygame.Rect(WIDTH/2+common_size,HEIGHT/2-common_size/2,200,200)
    f_a_o,f_b_o=f_a,f_b
    rest = (count/FPS)%20
    
    f_b = (FPS/f_b)/2
    f_a = (FPS/f_a)/2
    #print("dans la fonction, f_a,f_b=",f_a,f_b)
    #periode de consigne - 3 sec - no blink
    if rest <=3:
        pygame.draw.circle(WIN,CYAN,(WIDTH/2-common_size,HEIGHT/2),common_size/2)
        pygame.draw.circle(WIN,CYAN,(WIDTH/2+common_size,HEIGHT/2),common_size/2)
        if rest == 3:
            #temps début clignottement
            ligne = np.int(sec_g//20)+15
            #print("ligne =",ligne)
            t = datetime.fromtimestamp(time.time())
            #t = time.time()
            tabs[1][ligne][0] = t

    #periode de blinking - 12 sec
    
    if rest >3 and rest <=15:
        if (count//f_a)%2 == 1:
            pygame.draw.circle(WIN,CYAN,(WIDTH/2-common_size,HEIGHT/2),common_size/2)
        if (count//f_b)%2 == 1:
            pygame.draw.circle(WIN,CYAN,(WIDTH/2+common_size,HEIGHT/2),common_size/2)
        if rest == 15:
            ligne = np.int(sec_g//20)+15
            #print("ligne fin =",ligne)
            #temps fin clignottement
            tabs[0][ligne][0] = f_a_o
            tabs[0][ligne][1] = f_b_o
            t = datetime.fromtimestamp(time.time())
            #t = time.time()
            tabs[1][ligne][1] = t
            #print(tabs)

    #periode de repos - ecran noir - 5 sec
    if rest >15 and rest <=20:
        rest = level_font.render('Repos',1,WHITE)
        WIN.blit(rest,(np.int(WIDTH/2 - rest.get_width()/2),np.int(HEIGHT/2-rest.get_height()/2)))




def level(level,WIN):
   
    level_text = level_font.render("Niveau " + str(level),1,WHITE)
    WIN.blit(level_text,(level_x,level_y))

def essai(essai,WIN):
    level_text = level_font.render(essai,1,WHITE)
    WIN.blit(level_text,(WIDTH - 2*level_text.get_width(),HEIGHT-2*level_text.get_height()))
    #pygame.display.update()



def display_pause(WIN,titleFont):
    WIN.fill(BLACK)
    text = titleFont.render("PAUSE",1,WHITE)
    #affichage
    WIN.blit(text,(WIDTH/2-text.get_width()/2,HEIGHT/2 - text.get_height()/2))
    
def window_distance(WIN,count,f_a,f_b,WHITE,distance,sec_g,tabs):
    #WIN.fill(BLACK)
    common_size = 200

    rest = (count/FPS)%20
    f_a_o,f_b_o=f_a,f_b
    #WIN.fill(BLACK)
    #adaptation à la FPS
    f_b = (FPS/f_b)
    f_a = (FPS/f_a)
    #periode de consigne - 3 sec - no blink
    if rest <=3:
        
        pygame.draw.circle(WIN,CYAN,(WIDTH/2-distance/2,HEIGHT/2),common_size/2)
        pygame.draw.circle(WIN,CYAN,(WIDTH/2+distance/2,HEIGHT/2),common_size/2)
        if rest == 3:
            #temps début clignottement
            ligne = np.int(sec_g//20)+15
            #print("ligne début =",ligne)
            t = datetime.fromtimestamp(time.time())
            #t = time.time()
            tabs[1][ligne][0] = t

    #periode de blinking - 12 sec
    if rest >3 and rest <=15:
        if (count//f_a)%2 == 1:
            #pygame.draw.rect(WIN,CYAN,button_a)
            pygame.draw.circle(WIN,CYAN,(WIDTH/2-distance/2,HEIGHT/2),common_size/2)
        if (count//f_b)%2 == 1:
            #pygame.draw.rect(WIN,CYAN,button_b)
            pygame.draw.circle(WIN,CYAN,(WIDTH/2+distance/2,HEIGHT/2),common_size/2)
        if rest == 15:
            ligne = np.int(sec_g//20)+15
            #print("ligne fin =",ligne)
            #temps fin clignottement
            tabs[0][ligne][0] = f_a_o
            tabs[0][ligne][1] = f_b_o
            t = datetime.fromtimestamp(time.time())
            #t = time.time()
            tabs[1][ligne][1] = t
    
    #periode de repos - ecran noir - 5 sec
    if rest >15 and rest <=20:
        rest = level_font.render('Repos',1,WHITE)
        WIN.blit(rest,(np.int(WIDTH/2 - rest.get_width()/2),np.int(HEIGHT/2-rest.get_height()/2)))
    

def unique(WIN,count,f_a,WHITE,sec_g,tabs):
    
    common_size = 200
    #button_a = pygame.Rect(WIDTH/2-2*common_size,HEIGHT/2-common_size/2,200,200)
    #button_b = pygame.Rect(WIDTH/2+common_size,HEIGHT/2-common_size/2,200,200)
    f_a_o=f_a
    rest = (count/FPS)%20
    
    f_a = (FPS/f_a)/2
    #print("dans la fonction, f_a,f_b=",f_a,f_b)
    #periode de consigne - 3 sec - no blink
    if rest <=3:
        pygame.draw.circle(WIN,CYAN,(WIDTH/2,HEIGHT/2),common_size/2)
        if rest == 3:
            #temps début clignottement
            ligne = np.int(sec_g//20)
            #print("ligne =",ligne)
            t = datetime.fromtimestamp(time.time())
            print("fréquence =",f_a,"ligne =",ligne,"sec_g=",sec_g)
            #t = time.time()
            tabs[1][ligne][0] = t

    #periode de blinking - 12 sec
    
    if rest >3 and rest <=15:
        if (count//f_a)%2 == 1:
            pygame.draw.circle(WIN,CYAN,(WIDTH/2,HEIGHT/2),common_size/2)
            
        if rest == 15:
            ligne = np.int(sec_g//20)
            #print("ligne fin =",ligne)
            
            tabs[0][ligne][0] = f_a_o
            tabs[0][ligne][1] = f_a_o
            t = datetime.fromtimestamp(time.time())
            #temps fin clignottement
            tabs[1][ligne][1] = t
           

    #periode de repos - ecran noir - 5 sec
    if rest >15 and rest <=20:
        rest = level_font.render('Repos',1,WHITE)
        WIN.blit(rest,(np.int(WIDTH/2 - rest.get_width()/2),np.int(HEIGHT/2-rest.get_height()/2)))