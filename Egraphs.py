import numpy as np 
import matplotlib.pyplot as plt
import math
from DoublePendulum import DP #imports useful modules and double pendulum class from DoublePendulum.py
import json
import pandas as pd
import copy
from pathlib import Path
from matplotlib.animation import FuncAnimation 
import GraphFunc as func


Data = np.load(Path.cwd()/'Datafiles'/'datafile.npy', allow_pickle=True)
graphtitle = 'Total Energy over 500 seconds Euler-Cromer at dt = 0.01s'
graphname = 'graph.png'



kin1 = func.getKE1(Data)
kin2 = func.getKE2(Data)
pot1 = func.getPE1(Data)
pot2 = func.getPE2(Data)
Timelist = func.getTime(Data)
Elist = func.getE(Data)


plt.plot(Timelist, Elist, 'k-', lw = 1)
#plt.plot(Timelist, kin1, 'r-', lw = 1)
#plt.plot(Timelist, kin2, 'b-', lw = 1)
#plt.plot(Timelist, pot1, 'y-', lw = 1)
#plt.plot(Timelist, pot2, 'g-', lw = 1)

ymax = math.ceil( max([max(Elist),max(kin1),max(kin2),max(pot1),max(pot2)]) /10 ) * 10
ymin = min([min(Elist),min(kin1),min(kin2),min(pot1),min(pot2)])

plt.xlim(min(Timelist), max(Timelist))
plt.ylim(ymin, ymax)
plt.title(graphtitle)
plt.xlabel('Time (s)')
plt.ylabel('Energy (J)')
plt.legend(['TotalE','KE1','KE2','PE1', 'PE2' ], loc = 'upper left')
plt.savefig(graphname)
print(Elist)