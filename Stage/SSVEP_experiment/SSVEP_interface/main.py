import secrets
import pygame
import numpy as np
import os
import time
import random
import draw as d
from datetime import datetime


#initialisations
pygame.init()
pygame.font.init()

###GENERAL PARAMETERS
#window parameters
WIDTH,HEIGHT = 1200, 750
WIN = pygame.display.set_mode ((WIDTH,HEIGHT))
pygame.display.set_caption("SSVEP")
#display
FPS = 60 #to be sure to master stimulation frequencies
#fonts
timeFont = pygame.font.SysFont(os.path.join('fonts','LinBiolinum_R.ttf'),20)
titleFont = pygame.font.Font(os.path.join('fonts','LinBiolinum_R.ttf'),80)
#time
clock = pygame.time.Clock()
#colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
    

#frequencies
f_a = 15
f_b = 10
#adaptation à la FPS
f_b = (FPS/f_b)/2
f_a = (FPS/f_a)/2



time_protocole = [0,120,300,600]

def tableau():
    A = np.zeros((87,4))
    B = np.empty((87,2),dtype = 'datetime64[ms]')
    for k in range(87):
        #lumière
        if k >=21 and k <=36:
            A[k][3] = True
        if k <21 or k > 36:
            A[k][3] = False
        #distance
        if k < 15:
            A[k][2] = 0
        if k>=15 and k < 53 :
            A[k][2] = 360
        if k >=53 and k < 69:
            A[k][2] = 240
        if k >=69 and k < 75:
            A[k][2] = 120
        if k >=75 and k < 81:
            A[k][2] = 800
        if k >=81 and k < 87:
            A[k][2] = 500
        #frequences
        #fréquences
        if k < 5:
            A[k][0]=13
            A[k][1]=0
        if k >= 5 and k<10:
            A[k][0]=15
            A[k][1]=0
        if k <= 10 and k < 15:
            A[k][0]=17
            A[k][1]=0
        if (k>=15 and k < 33) or k >= 63:
            #gauche
            A[k][0] = 13
            #droite
            A[k][1] = 17
    return A,B



#tableau de suivi de l'expérience
def tablea_former():
    A = np.zeros((72,4))
    B = np.empty((72,2),dtype = 'datetime64[ms]')
    
    #préremplissage du tableau
    for k in range(72):
        
        #data type pour le temps
        """A[k][0] = A[k][0].astype('datetime64[ms]')
        A[k][1] = A[k][1].astype('datetime64[ms]')"""
        #fréquences
        if k < 18 or k >= 48:
            #gauche
            A[k][0] = 13
            #droite
            A[k][1] = 17
        #distance
        if k < 48 :
            A[k][2] = 360
        if k >=48 and k < 54:
            A[k][2] = 240
        if k >=54 and k < 60:
            A[k][2] = 120
        if k >=60 and k < 66:
            A[k][2] = 800
        if k >=66 and k < 72:
            A[k][2] = 500
        # lumière
        if k >=6 and k <=11:
            A[k][3] = True
        if k <6 or k > 11:
            A[k][3] = False

    return A,B
    
    
def consigne_generation():
    pos = ["gauche","droite"]
    consignes=[]
    
    for i in range(4):
        if i <=1:
            for k in range(3): #chaque composant est montré 3 fois
                r=random.sample(range(0,len(pos)),len(pos))
                for i in range(len(pos)):
                    consignes.append(pos[r[i]])
        else:
            for k in range(3*5): #chaque composant est montré 3 fois, avec 5 paramètres différents
                r=random.sample(range(0,len(pos)),len(pos))
                for i in range(len(pos)):
                    consignes.append(pos[r[i]])

        
    return consignes
time_o = 340 #duration essai 0
time_level = [0,180,360,1020,1620] #en secondes

def unit():
    #3 affichages unitaires de l'essai 0
    run = True
    count_g,count = 0,0
    t1 = time.time()
    tabs = tableau()
    while run :
        np.savetxt(os.path.join('Test','essai.txt'),tabs[0],delimiter =",")
        np.savetxt(os.path.join('Test','time.txt'),tabs[1],fmt='%s', delimiter = ',')
        clock.tick(FPS)
        count_g += 1
        sec_g = count_g/FPS

        #run = false
        if sec_g > time_o:
            run = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pause = False
        if (sec_g > 100 and sec_g<=120) or (sec_g>220 and sec_g<=240): #pauses
            pause = True
        else :
            pause = False

        if pause:
            d.display_pause(WIN,titleFont)
        if not pause:
            WIN.fill(BLACK)
            #temps sans compter les pauses
            count += 1
            sec = count/FPS
            d.level(0,WIN)
            if sec < 100:
                f=13
                d.essai("Essai 0.1",WIN)
            if sec > 100 and sec<200:
                f = 15
                d.essai("Essai 0.2",WIN)
            if sec >200 and sec < 300:
                f=17
                d.essai("Essai 0.3",WIN)
            d.unique(WIN,count,f,WHITE,sec,tabs)
        pygame.display.update()

    return tabs


def main14(tabs):
   
    run = True 
    count_g,count = 0,0

    #generation de toutes les consignes aléatoires
    consignes=consigne_generation()
    np.savetxt(os.path.join('Test','consignes.txt'),consignes,fmt='%s',delimiter =",")
    print(consignes)
    
    
    t1 = time.time()
    while run:
        np.savetxt(os.path.join('Test','essai.txt'),tabs[0],delimiter =",")
        np.savetxt(os.path.join('Test','time.txt'),tabs[1],fmt='%s', delimiter = ',')
        clock.tick(FPS)

        #temps depuis le début de la simulation
        count_g += 1
        #temps en secondes depuis le début de l'expérimentation
        sec_g = count_g/FPS

        if sec_g >time_level[-1]:
            run = False

        pause = False
        if (sec_g >120 and sec_g <=180) or (sec_g >300 and sec_g <=360) or (sec_g >960 and sec_g <=1020): #3 pauses d'une minute
            print("Pause après", sec_g,"ou",time.time()-t1,"secondes")
            pause = True
        else :
            pause = False

        if pause :
            #black screen
            d.display_pause(WIN,titleFont)
        
        if not pause :
        
            #temps sans compter les pauses
            count += 1
            sec = count/FPS

            if sec_g <= time_level[1]:
                level = 1
                f_a = 13
                f_b = 17
                #adaptation à la FPS
                """f_b = (FPS/f_b)/2
                f_a = (FPS/f_a)/2"""
                d.consigne(WIN,sec,consignes) 
                d.essai("Essai 1.1, affichage "+str(sec//20),WIN)
                d.level(level,WIN)
                d.window(WIN,count,f_a,f_b,WHITE,sec,tabs)

            if sec_g > time_level[1] and sec_g <= time_level[2]:
                level = 2
                f_a = 13
                f_b = 17
                #adaptation à la FPS
                """f_b = (FPS/f_b)/2
                f_a = (FPS/f_a)/2"""
                d.consigne(WIN,sec,consignes) 
                d.essai("Essai 2.1, affichage "+str(sec//20),WIN)
                d.level(level,WIN)
                d.window(WIN,count,f_a,f_b,WHITE,sec,tabs)

            if sec_g > time_level[2] and sec_g <= time_level[3]:
                level = 3
                freq=[[13,17],[14,16],[12,18],[10,20],[15,20]]
                level_time = sec_g - time_level[2] #temps en secondes depuis le début du niveau
                #print("temps écoulé depuis le début du niveau 3 =",level_time)
                trial_time = [40*3,40*6,40*9,40*12,40*15]

                d.consigne(WIN,sec,consignes)
                d.level(level,WIN)

                if level_time <= trial_time[0]:
                    f_a,f_b = freq[0]
                    d.window(WIN,count,f_a,f_b,WHITE,sec,tabs)
                    print("f_a,f_b=", f_a,f_b)
                    d.essai("Essai 3.1",WIN)
                if level_time > trial_time[0] and level_time <= trial_time[1]:
                    f_a,f_b = freq[1]
                    d.window(WIN,count,f_a,f_b,WHITE,sec,tabs)
                    print("f_a,f_b=", f_a,f_b)
                    d.essai("Essai 3.2",WIN)
                if level_time > trial_time[1] and level_time <= trial_time[2]:
                    f_a,f_b = freq[2]
                    d.window(WIN,count,f_a,f_b,WHITE,sec,tabs)
                    print("f_a,f_b=", f_a,f_b)
                    d.essai("Essai 3.3",WIN)
                if level_time > trial_time[2] and level_time <= trial_time[3]:
                    f_a,f_b = freq[3]
                    d.window(WIN,count,f_a,f_b,WHITE,sec,tabs)
                    d.essai("Essai 3.4",WIN)
                if level_time > trial_time[3] and level_time <= trial_time[4]:
                    f_a,f_b = freq[4]
                    d.window(WIN,count,f_a,f_b,WHITE,sec,tabs)
                    d.essai("Essai 3.5",WIN)
                

            if sec_g > time_level[3] and sec_g <= time_level[4]:
                level = 4
                distance = [360,240,120,800,500]
                f_a = 13
                f_b = 17
                level_time = sec_g - time_level[3] #temps en secondes depuis le début du niveau
                #print("temps depuis le début du niveau =",level_time)
                #print("temps depuis le début du niveau =", level_time)
                trial_time = [40*3,40*6,40*9,40*12,40*15]

                d.consigne(WIN,sec,consignes)
                d.level(level,WIN)

                if level_time <= trial_time[0]:
                    d.window_distance(WIN,count,f_a,f_b,WHITE,distance[0],sec,tabs)
                    d.essai("Essai 4.1",WIN)
                if level_time > trial_time[0] and level_time <= trial_time[1]:
                    d.window_distance(WIN,count,f_a,f_b,WHITE,distance[1],sec,tabs)
                    d.essai("Essai 4.2",WIN)
                if level_time > trial_time[1] and level_time <= trial_time[2]:
                    d.window_distance(WIN,count,f_a,f_b,WHITE,distance[2],sec,tabs)
                    d.essai("Essai 4.3",WIN)
                if level_time > trial_time[2] and level_time <= trial_time[3]:
                    d.window_distance(WIN,count,f_a,f_b,WHITE,distance[3],sec,tabs)
                    d.essai("Essai 4.4",WIN)
                if level_time > trial_time[3] and level_time <= trial_time[4]:
                    d.window_distance(WIN,count,f_a,f_b,WHITE,distance[4],sec,tabs)
                    d.essai("Essai 4.5",WIN)
                    print("Essai 4.5 ongoing")

                if level_time > trial_time[4] :
                    print("je suis passée par là")
                    run = False
                
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        
        pygame.display.update()
    print("temps total de l'expérimentation =", time.time()-t1)
    pygame.quit()

def pause(WIN,clock,duration):
    run = True
    count = 0

    pause = titleFont.render("Début dans...",1,WHITE)
    pause_3 = titleFont.render("3",1,WHITE)
    pause_2 = titleFont.render("2",1,WHITE)
    pause_1 = titleFont.render("1",1,WHITE)

    while run:
        clock.tick(FPS)
        sec = count/FPS
        count += 1
        WIN.fill(BLACK)
        WIN.blit(pause,(WIDTH/2 - pause.get_width()/2,HEIGHT/2 - pause.get_height()/2))
        
        if sec >= duration - 3 and sec < duration - 2:
            WIN.blit(pause_3,(WIDTH/2 - pause_3.get_width()/2,HEIGHT/2 + pause.get_height()))
        if sec >= duration - 2 and sec < duration - 1:
            WIN.blit(pause_2,(WIDTH/2 - pause_2.get_width()/2,HEIGHT/2 + pause.get_height()))
        if sec >= duration - 1 and sec < duration :
            WIN.blit(pause_1,(WIDTH/2 - pause_1.get_width()/2,HEIGHT/2 + pause.get_height()))
        
        #fin
        if sec >=duration:
            run = False
        for event in pygame.event.get() : 
            if event.type == pygame.QUIT : 
                run = False
                pygame.quit()
        pygame.display.update()

def general():
    pause(WIN,clock,5)
    tabs = unit()
    pause(WIN,clock,5)
    main14(tabs)

general()