import pygame
import os
import draw_window as d
import numpy as np
import time

pygame.init()
pygame.font.init()
pygame.mixer.init()
#Window initialization
WIDTH, HEIGHT = 400,780
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Speed Images")

PATH = 'Test'

#general parameters
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GRAY = (229,229,229)

FPS = 60
clock = pygame.time.Clock()

def save(classe,timing,time_click,inputs_attendu,inputs_player,err1,err2,trigger):
    np.savetxt(os.path.join(PATH,'log.txt'),classe,delimiter =",",fmt='%s')
    np.savetxt(os.path.join(PATH,'apparition_classe.txt'),timing,delimiter =",",fmt='%s')
    np.savetxt(os.path.join(PATH,'time_click.txt'),time_click,delimiter =",",fmt='%s')
    np.savetxt(os.path.join(PATH,'inputs_attendus.txt'),inputs_attendu,delimiter =",",fmt='%s')
    np.savetxt(os.path.join(PATH,'inputs_player.txt'),inputs_player,delimiter =",",fmt='%s')
    np.savetxt(os.path.join(PATH,'error_1.txt'),err1,delimiter =",",fmt='%s')
    np.savetxt(os.path.join(PATH,'error_2.txt'),err2,delimiter =",",fmt='%s')
    np.savetxt(os.path.join(PATH,'trigger.txt'),trigger,delimiter =",",fmt='%s')
    




def manche(p1,p2,classe,timing,time_click,inputs_attendu,inputs_player,err1,err2,trigger):
    t1 = time.time()

    run = True

    count = 0
    k = 0
    r1,r2 =0,0
    r,u = 0,0
    points = 0
    liste_events =[]
    

    while run:
        
        WIN.fill(BLACK)

        for event in pygame.event.get() : 
            if event.type == pygame.QUIT : 
                run = False
                save(classe,timing,time_click,inputs_attendu,inputs_player,err1,err2,trigger)
                pygame.quit()
           
        #horloge du jeu       
        clock.tick(FPS)
        #secondes ramenées à la FPS depuis le début de la manche
        sec = count/FPS
        #nombre de tours depuis le début de la manche
        count +=1
              
        #choix et affichage des composants
        r1,r2 = d.choice(sec,r1,r2)
        classe,timing,inputs_attendu,trigger = d.choice_display(WIN,sec,r1,r2,classe,timing,inputs_attendu,trigger) 
        
        #management des clicks
        r = d.choose(r,sec%3)
        u = d.choose(u,sec%3)
        #print("r=",r)
        liste_events,points,time_click,inputs_player,k,trigger = d.feedbacks(WIN,sec,r1==r2,points,liste_events,time_click,inputs_player,p1,p2,err1,err2,r,u,k,trigger)

        #décompte des points
        d.jauge(WIN,points,sec)

        pygame.display.update()

        #fin du jeu
        if time.time()-t1 >= 120:
            run = False
            save(classe,timing,time_click,inputs_attendu,inputs_player,err1,err2,trigger)
            
        if points == 20:
            run = False
            save(classe,timing,time_click,inputs_attendu,inputs_player,err1,err2,trigger)
            




def jeu():
    #listes des logs du jeu
    classe = []
    timing = []
    time_click = []
    inputs_attendu = []
    inputs_player = []
    err1 = []
    err2 = []
    trigger = []

    d.pause(WIN,"Début",clock,5)
    manche(0,0,classe,timing,time_click,inputs_attendu,inputs_player,err1,err2,trigger)
    
    d.pause(WIN,"PAUSE",clock,10)
    manche(0.3,0,classe,timing,time_click,inputs_attendu,inputs_player,err1,err2,trigger)

    d.pause(WIN,"PAUSE",clock,10)
    manche(0,0.3,classe,timing,time_click,inputs_attendu,inputs_player,err1,err2,trigger)

    d.pause(WIN,"PAUSE",clock,10)
    manche(0.3,0,classe,timing,time_click,inputs_attendu,inputs_player,err1,err2,trigger)



jeu()

