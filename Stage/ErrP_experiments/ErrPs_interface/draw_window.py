from logging.handlers import TimedRotatingFileHandler
import pygame
import os
import random
from datetime import datetime
import time

pygame.init()
pygame.font.init()
pygame.mixer.init()

#Window initialization
WIDTH, HEIGHT = 400,780


#LOAD IMAGES
#squares
RED_SQUARE = pygame.transform.scale(pygame.image.load(os.path.join("assets","red_square.png")),(150,150))
GREEN_SQUARE = pygame.transform.scale(pygame.image.load(os.path.join("assets","green_square.png")),(150,150))
BLUE_SQUARE = pygame.transform.scale(pygame.image.load(os.path.join("assets","blue_square.png")),(150,150))
YELLOW_SQUARE = pygame.transform.scale(pygame.image.load(os.path.join("assets","yellow_square.png")),(150,150))
#circles
RED_CIRCLE = pygame.transform.scale(pygame.image.load(os.path.join("assets","red_circle.png")),(150,150))
GREEN_CIRCLE = pygame.transform.scale(pygame.image.load(os.path.join("assets","green_circle.png")),(150,150))
BLUE_CIRCLE = pygame.transform.scale(pygame.image.load(os.path.join("assets","blue_circle.png")),(150,150))
YELLOW_CIRCLE = pygame.transform.scale(pygame.image.load(os.path.join("assets","yellow_circle.png")),(150,150))
#triangles
RED_TRIANGLE = pygame.transform.scale(pygame.image.load(os.path.join("assets","red_triangle.png")),(190,160))
GREEN_TRIANGLE = pygame.transform.scale(pygame.image.load(os.path.join("assets","green_triangle.png")),(190,160))
BLUE_TRIANGLE = pygame.transform.scale(pygame.image.load(os.path.join("assets","blue_triangle.png")),(190,160))
YELLOW_TRIANGLE = pygame.transform.scale(pygame.image.load(os.path.join("assets","yellow_triangle.png")),(190,160))
#results
CLASH = pygame.transform.scale(pygame.image.load(os.path.join("assets","clash.png")),(350,400))
MATCH = pygame.transform.scale(pygame.image.load(os.path.join("assets","match.png")),(350,400))
BRAVO = pygame.transform.scale(pygame.image.load(os.path.join("assets","bravo.png")),(350,350))
DOMMAGE = pygame.transform.scale(pygame.image.load(os.path.join("assets","dommage.png")),(350,350))

#sound
#sound = pygame.mixer.Sound(os.path.join("assets","la.mp3"))
#DO = pygame.mixer.Sound(os.path.join("assets","do.mp3"))
#MI = pygame.mixer.Sound(os.path.join("assets","mi.mp3"))
sound = pygame.mixer.Sound("test_porte_scipy.wav")
sound.set_volume(0.02)

COMPONENTS = [RED_SQUARE,GREEN_SQUARE,BLUE_SQUARE,YELLOW_SQUARE,RED_CIRCLE,GREEN_CIRCLE,BLUE_CIRCLE,YELLOW_CIRCLE,RED_TRIANGLE,GREEN_TRIANGLE,BLUE_TRIANGLE,YELLOW_TRIANGLE]
#dictionnaire qui à chaque couleur relie les composants de mêmes couleurs
COLORS_DICO = {"red":(RED_SQUARE,RED_TRIANGLE,RED_CIRCLE),"blue":(BLUE_CIRCLE,BLUE_SQUARE,BLUE_TRIANGLE),"green":(GREEN_CIRCLE,GREEN_SQUARE,GREEN_TRIANGLE),"yellow":(YELLOW_CIRCLE,YELLOW_TRIANGLE,YELLOW_SQUARE)}
SHAPE_DICO = {"square":(RED_SQUARE,BLUE_SQUARE,YELLOW_SQUARE,GREEN_SQUARE),"triangle":(RED_TRIANGLE,BLUE_TRIANGLE,YELLOW_TRIANGLE,GREEN_TRIANGLE),"circle":(RED_CIRCLE,BLUE_CIRCLE,YELLOW_CIRCLE,GREEN_CIRCLE)}
#general parameters
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GRAY = (229,229,229)
ORANGE = (255,128,51)
GREEN = (60,255,51)
FPS = 60

#fonts
big_font = pygame.font.SysFont("linuxlibertinegdisplayregular", 100)
main_font = pygame.font.SysFont("linuxlibertinegdisplayregular", 50)
little_font = pygame.font.SysFont("linuxlibertinegdisplayregular",20)
clock_font = pygame.font.SysFont("trebuchetms",20) 

#################################### FONCTIONS ############################################

def accueil(WIN):
    title = main_font.render("Speed Images",1,WHITE)
    WIN.blit(title, (WIDTH/2 - title.get_width()/2, 690))
    WIN.blit(GREEN_CIRCLE,(32,36))
    WIN.blit(BLUE_SQUARE,(200,250))
    WIN.blit(RED_TRIANGLE,(12,450))
    pygame.display.update()

def choice(sec,a,b):
    l = len(COMPONENTS)
    if sec%3 <= 1/FPS: 
        
        r1 = random.randint(0,l-1)
        r2 = random.randint(0,l-1)
        #on veut une probabilité plus forte que 2 formes identiques apparaissent
        n = random.random()
        if n > 0.7:
            r1=r2
        #affichage composants
        #sound.play()
    else :
        r1,r2=a,b
    
    return r1,r2

#affichage de 2 composants préalablement sélectionnés
def choice_display(WIN,sec,r1,r2,log,tim,inputs_attendus,trigger): 
    timing = sec%3
    if timing >0.5/FPS and timing < 1.5/FPS:
        #trigger affichage
        sound.play()
        trigger.append("Affichage")
        print("play")
        if r1 == r2:
            log.append("identiques")
            print("MATCH")
            inputs_attendus.append("match")
            #tim.append(datetime.fromtimestamp(time.time()))
            #print("Identiques")
        else:
            k=0
            #print("CLASH")
            inputs_attendus.append("clash")
            if test_colors(COMPONENTS[r1]) == test_colors(COMPONENTS[r2]):
                log.append("couleurs") 
                k=1 
                #print("couleurs")
            if test_shapes(COMPONENTS[r1]) == test_shapes(COMPONENTS[r2]):
                log.append("formes")
                k=1
                #print("formes")
            if k==0:
                log.append("None")
                #print("NONE pour vérifier")
        tim.append(datetime.fromtimestamp(time.time()))   
    if timing > 1/FPS and timing <= 1.5:
        WIN.blit(COMPONENTS[r1],(WIDTH/2 - COMPONENTS[r1].get_width()/2,164))
        WIN.blit(COMPONENTS[r2],(WIDTH/2 - COMPONENTS[r2].get_width()/2,400))
        
    return log,tim,inputs_attendus,trigger

def feedbacks(WIN,sec,same,points,liste_events,time_click,input_player,p1,p2,err1,err2,r,u,k,trigger):
    #intervalle pour la décision à prendre
    timing = sec%3
    #réinitialisation
    if timing ==0:
        liste_events = []
    key = None
    #construction de la liste des events
    if timing > 0 and timing <2:
        k = 0    
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                #la liste peut avoir une taille énorme, mais c'est le 1er élément qui nous intéresse
                liste_events.append(event.key)
                if len(liste_events)==1:
                    #trigger clic
                    sound.play()
                    trigger.append("Clic")
                    print("play clic")
                    time_click.append(datetime.fromtimestamp(time.time()))
                    
                    #print("click")

    if timing > 0 and timing <=3:
        if len(liste_events) != 0:
            key = liste_events[0]
        if len(liste_events) == 0:
            key = None

        if timing >(2-1.5/FPS) and timing < 2: 
            #print("je suis passée par là")
            if len(liste_events)==0:
                print("pas de clic")
                
                time_click.append("None")

        if key != None :
            
            #Choix du feedback 1 et output decision 1 avec prise en compte de l'erreur   
            if key == pygame.K_RIGHT:
                button,aff = feedback_1m(WIN,timing,MATCH,CLASH,r,p1,err1,time_click)
                
            if key == pygame.K_LEFT:
                button,aff = feedback_1m(WIN,timing,CLASH,MATCH,r,p1,err1,time_click)

            #gestion des misclics  
            if key != pygame.K_LEFT and key != pygame.K_RIGHT :
                button = DOMMAGE

            #Choix du feedback 2 d'après l'output decision 1 en prenant en compte l'erreur
            
            if timing >= 2 and timing < 3 :   
                           
                if button == MATCH:
                    print("######pipeline affichage 2")
                    if same :
                        points,k,trigger = feedback_2(WIN,timing,BRAVO,points,u,p2,err2,k,time_click,trigger)
                    if not same :
                        points,k,trigger = feedback_2(WIN,timing,DOMMAGE,points,u,p2,err2,k,time_click,trigger)
                    if timing == 2:
                        
                        input_player.append([len(time_click),"match"])
                
                if button == CLASH :
                    
                    if not same :
                        points,k,trigger = feedback_2(WIN,timing,BRAVO,points,u,p2,err2,k,time_click,trigger)
                    if same :
                        points,k,trigger = feedback_2(WIN,timing,DOMMAGE,points,u,p2,err2,k,time_click,trigger)
                    if timing == 2:
                        print("enregistrement input player : clash")
                        input_player.append([len(time_click),"clash"])

                if button == BRAVO :
                    if timing == 2:
                        if aff == CLASH :
                            print("enregistrement input player après erreur 1")
                            input_player.append([len(time_click),"clash e1"])
                        if aff == MATCH :
                            print("enregistrement input player après erreur 1")
                            input_player.append([len(time_click),"match e1"])
                        
                        err2.append([len(time_click),None])
                        

        #si le joueur ne prend pas de décision
        if key == None :
            
            if timing == 2:
                print("enregistrement input player : none")
                input_player.append([len(time_click),"None"])
                err1.append([len(time_click),None])
                err2.append([len(time_click),None])
                
    return liste_events,points,time_click,input_player,k,trigger

def feedback_2(WIN,timing, button,points,u,p2,err2,k,time_click,trigger):
    #Erreur 2 : inversion des boutons
    
    if timing >=2 and timing <2+2/FPS and k == 0: 
        
        #trigger feedback 2
        if timing < 2 + 1/FPS :
            k=1
            sound.play() 
            trigger.append("feedback")
            print("play f2 1")
        #contournement du bug
        if timing > 2+1/FPS and timing < 2 + 2/FPS: 
        #trigger feedback 2
            k=1
            sound.play()
            trigger.append("feedback")
            print("play f2 2")
 

    if u < p2:
        
        if timing >3-1.5/FPS and timing <3:
            print("erreur 2")
            err2.append([len(time_click),1])
        if button == BRAVO :
            button = DOMMAGE
        else:
            button = BRAVO

    if u >= p2 :
        if timing >3-1.5/FPS and timing <3:
            #print("pas d'erreur 2")
            err2.append([len(time_click),0])
    if button == BRAVO:
        if timing ==2:
            points+=1
        if timing >2:
            result(WIN,button)
    if button == DOMMAGE:
        if timing ==2:
            points-=1
        if timing >2:
            result(WIN,button)
    return points,k,trigger
    
def feedback_1(WIN,timing,button1,button2,r,p1,err1,time_click):
    #r = choose(r,timing)
    if r < p1:
        button1 = button2
        if timing >2-1.5/FPS and timing <2:
            print("erreur 1")
            
            err1.append([len(time_click),1])
    else:
        if timing >2-1.5/FPS and timing <2:
            #print("pas d'erreur 1")
            err1.append([len(time_click),0])
    if timing < 2:
        WIN.blit(button1,(WIDTH/2 - button1.get_width()/2, HEIGHT/2 - 20 - button2.get_height()/2))
    return button1

def feedback_1m(WIN,timing,button1,button2,r,p1,err1,time_click):
    #r = choose(r,timing)
    #erreur
    aff = BRAVO
    if r < p1:
        aff = button1
        button1 = BRAVO
        
        if timing >2-1.5/FPS and timing <2:
            print("erreur 1")
            
            err1.append([len(time_click),1])
    #pas d'erreur
    else:
        if timing >2-1.5/FPS and timing <2:
            #print("pas d'erreur 1")
            err1.append([len(time_click),0])
    if timing < 2 and button1 != BRAVO:
        WIN.blit(button1,(WIDTH/2 - button1.get_width()/2, HEIGHT/2 - 20 - button2.get_height()/2))
    return button1,aff

def choose(a,timing):
    if timing <= 1/FPS:
        r = random.random()
    else :
        r=a
    
    return r


def result(WIN,button):
    #WIN.blit(button,(WIDTH/2 - button.get_width()/2,HEIGHT - 10 - button.get_height()))
    WIN.blit(button,(WIDTH/2 - button.get_width()/2,HEIGHT/2 - 20 - button.get_height()/2))

def jauge(WIN,points,sec):

    score = little_font.render("SCORE:",1,WHITE)
    best = little_font.render("Best : ",1,RED)
    score = clock_font.render("61:38",1,RED)
    color = RED
    if points >= 10 and points <= 15:
        color = ORANGE
    if points > 15:
        color = GREEN
    time = clock_font.render(str(int(sec))+":"+str(int(100*sec)-int(sec)*100),1, color)
    WIN.blit(score,(10,10))
    WIN.blit(best,(WIDTH - 10 - best.get_width() - score.get_width(),110))
    WIN.blit(score,(WIDTH - 10 - score.get_width(),110))
    WIN.blit(time,(WIDTH-time.get_width() - 10,10))
    pygame.draw.rect(WIN,GRAY,(12,41,377,64))
    pygame.draw.rect(WIN,color,(18,47,(points*(18+363))/20,52))


def test_colors(comp):
    for key in COLORS_DICO.keys():
        for value in COLORS_DICO.get(key):
            if value == comp:                
                return(key)

def test_shapes(comp):
    for key in SHAPE_DICO.keys():
        for value in SHAPE_DICO.get(key):
            if value == comp:
                return(key)

def pause(WIN,msg,clock,duration):
    run = True
    count = 0

    pause = big_font.render(msg,1,WHITE)
    pause_3 = big_font.render("3",1,WHITE)
    pause_2 = big_font.render("2",1,WHITE)
    pause_1 = big_font.render("1",1,WHITE)

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
    