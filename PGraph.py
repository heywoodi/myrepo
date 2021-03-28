import numpy as np 
import matplotlib.pyplot as plt
import math
from DoublePendulum import DP
import json
import pandas as pd
import copy
from pathlib import Path
from matplotlib.animation import FuncAnimation 
import GraphFunc as func


Data = np.load(Path.cwd()/'datafile.npy', allow_pickle=True)            #
graphtitle = 'Pendulum momentums over 10 seconds (RK4 at dt = 0.01s)'   # retrieves data file
graphname = 'pgraph.png'                                                # and sets title



P11 = func.getP11(Data)         #
P12 = func.getP12(Data)         # retrives list of data
P21 = func.getP22(Data)         # to plot
P22 = func.getP22(Data)         #
Timelist = func.getTime(Data)   #

P1 = []                                                         #
P2 = []                                                         #
Ptot = []                                                       # ammends the data to usable (x,y)
for i in range(len(P11)):                                       # coordinate style data
    P1.append( math.sqrt(P11[i] *P11[i] + P12[i] * P12[i]) )    #
    P2.append( math.sqrt(P21[i] *P21[i] + P22[i] * P22[i]) )    #
    Ptot.append( P1[i] + P2[i])

plt.plot(Timelist, P1, 'b-', lw = 1)                    # plots momentum 1 blue
plt.plot(Timelist, P2, 'r-', lw = 1)                    # plots momentum 2 red
plt.plot(Timelist, Ptot, 'k-', lw = 1)                  # plots total momentum black


plt.title(graphtitle)                                   #
plt.xlabel('Time (s)')                                  # sets the graph style
plt.ylabel('Momentum (KG*m/s)')                         # title, axes and legend
plt.legend(['M1','M2','Mtot'], loc = 'upper left')      #
plt.savefig(graphname)                                   #

