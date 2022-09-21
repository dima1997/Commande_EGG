import os
import numpy as np
from sklearn.preprocessing import normalize
import matplotlib.pyplot as plt
#essais considérés : 84,26,305,12,15,6478

#récupération des données 
l = ['84','305','26','12','15','6478']
feedback_84 = np.genfromtxt(os.path.join("Results","difference",'84'+"feedback"+".txt"))
clic_84 = np.genfromtxt(os.path.join("Results","difference",'84'+"clic"+".txt"))
feedback_305 = np.genfromtxt(os.path.join("Results","difference",'305'+"feedback"+".txt"))
clic_305 = np.genfromtxt(os.path.join("Results","difference",'305'+"clic"+".txt"))
feedback_26 = np.genfromtxt(os.path.join("Results","difference",'26'+"feedback"+".txt"))
clic_26 = np.genfromtxt(os.path.join("Results","difference",'26'+"clic"+".txt"))
feedback_12 = np.genfromtxt(os.path.join("Results","difference",'12'+"feedback"+".txt"))
clic_12 = np.genfromtxt(os.path.join("Results","difference",'12'+"clic"+".txt"))
feedback_15 = np.genfromtxt(os.path.join("Results","difference",'15'+"feedback"+".txt"))
clic_15 = np.genfromtxt(os.path.join("Results","difference",'15'+"clic"+".txt"))
feedback_6478 = np.genfromtxt(os.path.join("Results","difference",'6478'+"feedback"+".txt"))
clic_6478 = np.genfromtxt(os.path.join("Results","difference",'6478'+"clic"+".txt"))

#normalisation
feedback_84b = feedback_84
X = np.linspace(-0.3,1,feedback_84.shape[1])
zero = np.zeros((feedback_84.shape[1]))
feedback_84 = normalize(feedback_84,axis=1,norm='l2')
clic_84 = normalize(clic_84,axis=1,norm='l2')
feedback_305 = normalize(feedback_305,axis=1,norm='l2')
clic_305 = normalize(clic_305,axis=1,norm='l2')
feedback_26 = normalize(feedback_26,axis=1,norm='l2')
clic_26 = normalize(clic_26,axis=1,norm='l2')
feedback_12 = normalize(feedback_12,axis=1,norm='l2')
clic_12 = normalize(clic_12,axis=1,norm='l2')
feedback_15 = normalize(feedback_15,axis=1,norm='l2')
clic_15 = normalize(clic_15,axis=1,norm='l2')
feedback_6478 = normalize(feedback_6478,axis=1,norm='l2')
clic_6478 = normalize(clic_6478,axis=1,norm='l2')

#affichage des clics
plt.plot(X,clic_84[1],label='84')
plt.plot(X,clic_305[1],label='305')
plt.plot(X,clic_26[1],label='26')
plt.plot(X,clic_12[1],label='12')
plt.plot(X,clic_15[1],label='15')
plt.plot(X,clic_6478[1],label='6478')
plt.plot(X,zero,label='0',color='r')
plt.title("Comparaison des différences entre les essais avec erreur 1 et les essais sans erreur 1 pour 6 participant.e.s")
plt.legend()
plt.show()


plt.plot(X,feedback_84[1],label='84')
plt.plot(X,feedback_305[1],label='305')
plt.plot(X,feedback_26[1],label='26')
plt.plot(X,feedback_12[1],label='12')
plt.plot(X,feedback_15[1],label='15')
plt.plot(X,feedback_6478[1],label='6478')
plt.plot(X,zero,label='0',color='r')
plt.title("Comparaison des différences entre les essais avec erreur 2 et les essais sans erreur 2 pour 6 participant.e.s")
plt.legend()
plt.show()
