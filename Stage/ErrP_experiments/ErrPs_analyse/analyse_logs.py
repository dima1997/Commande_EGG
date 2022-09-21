import os
import numpy as np
from datetime import datetime

origin = "Logs"
file = "6478"

#IMPORTATIONS DES FICHIERS
classes = np.loadtxt(os.path.join(origin,file,"log.txt"),dtype = str)
temps_classe = np.loadtxt(os.path.join(origin,file,"apparition_classe.txt"),dtype = 'datetime64[ms]',delimiter =",")
error1 = np.loadtxt(os.path.join(origin,file,"error_1.txt"),delimiter = ",",dtype = str)
error2 = np.loadtxt(os.path.join(origin,file,"error_2.txt"),delimiter = ",",dtype = str)
attendus = np.loadtxt(os.path.join(origin,file,"inputs_attendus.txt"),dtype = str, delimiter = ",")
player = np.loadtxt(os.path.join(origin,file,"inputs_player.txt"),dtype = str, delimiter = ",")
time_click = np.loadtxt(os.path.join(origin,file,"time_click.txt"),delimiter =",",dtype = str)

#conversion du time_click au bon format (prise en compte des None)
l = len(time_click)
new_time_click = np.empty((l),dtype = 'datetime64[ms]')
for t in range(0,len(time_click)):
  if time_click[t] == 'None':
    new_time_click[t] == 0
  else:
    time = time_click[t]
    new_time_click[t] = datetime.strptime(time,"%Y-%m-%d %H:%M:%S.%f")
#print("nouveaux temps clic = ", new_time_click)
#nombre de cycles de l'expérimentation étudiés
liste_sizes = [classes.shape,temps_classe.shape,error1.shape,error2.shape,attendus.shape,player.shape,new_time_click.shape]
min = np.min(liste_sizes)[0]
print("MIN=",min)

#apparition des erreurs
count_1,count_2 = 0,0
for k in range(min):
  if error1[k][1]=='1':
    count_1 += 1
  if error2[k][1]=='1':
    count_2 += 1
print("il y a eu",count_1," erreurs 1 et ",count_2," erreurs 2 sur",min," essais en tout (représentant donc",count_1/min*100,"et",count_2/min*100,"%)")
count_sim = 0
for k in range(min):
  if error1[k][1]=='1' and error2[k][1]=='1':
    count_sim += 1
print("il y a eu",count_sim,"erreurs simultanées")

#erreurs joueurs
count_error = 0
for k in range(min):
  if attendus[k]!=player[k][1]:
    count_error += 1
print("le joueur a commis ",count_error-count_1," erreurs (les erreurs 1 ont été retirées)")

#temps de réaction moyen
reac = []
count = 0
for k in range(min):
  #print(type(new_time_click[k]))
  if new_time_click[k] >  datetime.strptime('1970-01-01T00:00:00.000','%Y-%m-%dT%H:%M:%S.%f'):
    reac.append(new_time_click[k]-temps_classe[k])
    count += 1
print("le temps moyen de réaction est :",np.mean(reac),"ms (",count,") cycles ont été pris en compte","(",np.round(np.std(np.array(reac).astype(float)))," ms en écart type)")

#temps de réaction pour les clashs et pour les matchs
reac_clash = []
reac_match = []
reac_wrong = []
reac_right = []
count_clash,count_match,count_wrong,count_right = 0,0,0,0
for k in range(min):
  #print(type(new_time_click[k]))
  if new_time_click[k] >  datetime.strptime('1970-01-01T00:00:00.000','%Y-%m-%dT%H:%M:%S.%f'):
    if player[k][1]=="match" and attendus[k]=="match" and error1[k][1]=='0':
      count_match += 1
      #print("je suis passée par là")
      reac_match.append(new_time_click[k]-temps_classe[k])
    if player[k][1]=="clash" and attendus[k]=="clash" and error1[k][1]=='0':
      count_clash += 1
      reac_clash.append(new_time_click[k]-temps_classe[k])
      #print("je suis passée par là")
    if player[k][1]!=attendus[k] and error1[k][1] == '0':
      reac_wrong.append(new_time_click[k]-temps_classe[k])
      count_wrong+=1
    if player[k][1]==attendus[k] and error1[k][1] == '0':
      reac_right.append(new_time_click[k]-temps_classe[k])
      count_right+=1
print("le temps moyen de réaction pour les match est",np.mean(reac_match),"(",np.round(np.std(np.array(reac_match).astype(float)))," ms en écart type)"," et pour les clash", np.mean(reac_clash),"(",np.round(np.std(np.array(reac_clash).astype(float))),"ms en écart type)")
print("le temps de réaction moyen pour les erreurs est",np.mean(reac_wrong),"ms","(",np.round(np.std(np.array(reac_wrong).astype(float)))," ms en écart type)")
print("le temps de réaction moyen pour les réussites est",np.mean(reac_right),"ms""(",np.round(np.std(np.array(reac_right).astype(float)))," ms en écart type)")
print("comptes clash,match,wrong,right =",count_clash,count_match,count_wrong,count_right)
results = [[min,"erreurs =",count_error-count_1,"erreur 1 =",count_1,"erreur 2 =",count_2,],["reaction général =", np.mean(reac), np.round(np.std(np.array(reac).astype(float))),count,],["matchs réussis",np.mean(reac_match),np.round(np.std(np.array(reac_match).astype(float))),count_match],["clashs réussis",np.mean(reac_clash),np.round(np.std(np.array(reac_clash).astype(float))),count_clash],["réussites",np.mean(reac_right),np.round(np.std(np.array(reac_right).astype(float))),count_right],["échecs",np.mean(reac_wrong),np.round(np.std(np.array(reac_wrong).astype(float))),count_wrong]]
print(results)