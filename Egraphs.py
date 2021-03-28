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


Data = np.load(Path.cwd()/'datafile.npy', allow_pickle=True)    # retrieves data
graphtitle = 'Pendulum energies over time at dt = 0.01s'        # and sets name
graphname = 'egraph.png'                                        # 



kin1 = func.getKE1(Data)            # 
kin2 = func.getKE2(Data)            # 
pot1 = func.getPE1(Data)            # retrieves specific
pot2 = func.getPE2(Data)            # datalists from
Timelist = func.getTime(Data)       # datafile
Elist = func.getE(Data)             #


plt.plot(Timelist, Elist, 'k-', lw = 1) # 
plt.plot(Timelist, kin1, 'r-', lw = 1)  # plots data with
plt.plot(Timelist, kin2, 'b-', lw = 1)  # respect to time
plt.plot(Timelist, pot1, 'y-', lw = 1)  # 
plt.plot(Timelist, pot2, 'g-', lw = 1)  # 

ymax = math.ceil( max([max(Elist),max(kin1),max(kin2),max(pot1),max(pot2)]) /10 ) * 10  # creates min and
ymin = min([min(Elist),min(kin1),min(kin2),min(pot1),min(pot2)])                        # max y limits

plt.xlim(min(Timelist), max(Timelist))  # creates min and max x limits
plt.ylim(ymin, ymax)                    # sets y limits 
plt.title(graphtitle)                   # set title
plt.xlabel('Time (s)')                  # sets x and y labels
plt.ylabel('Energy (J)')                # set legend
plt.legend(['TotalE','KE1','KE2','PE1', 'PE2' ], loc = 'upper left')
plt.savefig(graphname)                  # saves graph