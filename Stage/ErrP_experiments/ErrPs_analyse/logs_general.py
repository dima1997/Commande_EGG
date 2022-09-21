import numpy as np
from datetime import datetime

log_21 = [[73, 'erreurs =', 22, 'erreur 1 =', 3, 'erreur 2 =', 7], ['reaction général =', np.timedelta64(832,'ms'), 245.0, 72], ['matchs réussis', np.timedelta64(771,'ms'), 276.0, 21], ['clashs réussis', np.timedelta64(832,'ms'), 194.0, 25], ['réussites', np.timedelta64(804,'ms'), 237.0, 46], ['échecs', np.timedelta64(906,'ms'), 256.0, 23]]
log_cassandre = [[91, 'erreurs =', 19, 'erreur 1 =', 9, 'erreur 2 =', 10], ['reaction général =', np.timedelta64(578,'ms'), 157.0, 88], ['matchs réussis', np.timedelta64(630,'ms'), 123.0, 9], ['clashs réussis', np.timedelta64(557,'ms'), 116.0, 48], ['réussites', np.timedelta64(569,'ms'), 120.0, 57], ['échecs', np.timedelta64(616,'ms'), 234.0, 22]]
log_12 = [[90, 'erreurs =', 28, 'erreur 1 =', 12, 'erreur 2 =', 12], ['reaction général =', np.timedelta64(751,'ms'), 227.0, 84], ['matchs réussis', np.timedelta64(702,'ms'), 202.0, 10], ['clashs réussis', np.timedelta64(752,'ms'), 223.0, 34], ['réussites', np.timedelta64(741,'ms'), 219.0, 44], ['échecs', np.timedelta64(785,'ms'), 263.0, 28]]
log_32=[[50, 'erreurs =', 8, 'erreur 1 =', 3, 'erreur 2 =', 0], ['reaction général =', np.timedelta64(751,'ms'), 184.0, 49], ['matchs réussis', np.timedelta64(797,'ms'), 269.0, 11], ['clashs réussis', np.timedelta64(725,'ms'), 153.0, 26], ['réussites', np.timedelta64(746,'ms'), 198.0, 37], ['échecs', np.timedelta64(725,'ms'), 103.0, 9]]
log_5 = [[172, 'erreurs =', 28, 'erreur 1 =', 25, 'erreur 2 =', 26], ['reaction général =', np.timedelta64(663,'ms'), 166.0, 165], ['matchs réussis', np.timedelta64(693,'ms'), 220.0, 22], ['clashs réussis', np.timedelta64(668,'ms'), 158.0, 77], ['réussites', np.timedelta64(674,'ms'), 174.0, 99], ['échecs', np.timedelta64(653,'ms'), 168.0, 37]]

general = [log_21]+[log_cassandre]+[log_12]+[log_32]+[log_5]

moyenne = [["réaction générale",0,0],["réaction match",0,0],["réaction clash",0,0],["réaction réussite",0,0],["réaction échec",0,0]]
number_cobaye = len(general)
general_m = [['reaction général =', 0, 0], ['matchs réussis', 0, 0], ['clashs réussis', 0, 0], ['réussites', 0, 0], ['échecs', 0, 0]]
for i in range(number_cobaye):
    general_m[0][1] += general[i][1][1]
    general_m[0][2] += general[i][1][2]
    general_m[1][1] += general[i][2][1]
    general_m[1][2] += general[i][2][2]
    general_m[2][1] += general[i][3][1]
    general_m[2][2] += general[i][3][2]
    general_m[3][1] += general[i][4][1]
    general_m[3][2] += general[i][4][2]
    general_m[4][1] += general[i][5][1]
    general_m[4][2] += general[i][5][2]
for j in range(len(general_m)):
    general_m[j][1] = general_m[j][1]/number_cobaye
    general_m[j][2] = general_m[j][2]/number_cobaye

#print("print=",len(general[0]),general[0][1][1]) 
print(general_m)
#np.timedelta64(0,'ms')

