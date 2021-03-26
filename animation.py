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


Data = np.load(Path.cwd()/'datafile.npy', allow_pickle=True)



time = func.getTime(Data)
xa = func.getx1(Data)
xb = func.getx2(Data)                                                       #
ya = func.gety1(Data)                                                       #
yb = func.gety2(Data)                                                       #
timeInt = func.getInterval(Data)  
                                                                            
fig = plt.figure()                                                          #
ax = fig.add_subplot(111, autoscale_on=False, xlim=(-2, 2), ylim=(-2, 2))   #
ax.grid()
line, = ax.plot([], [], 'o-', lw=2, color = 'black', ms = 8)
time_template = 'time = %.1fs'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes, )
def init():
    line.set_data([], [])
    time_text.set_text('')
    return line, time_text
def animate(i):
    thisx = [0, xa[i], xb[i]]
    thisy = [0, ya[i], yb[i]]
    line.set_data(thisx, thisy)
    time_text.set_text("t = " + str(time[i]))
    return line, time_text
ani = FuncAnimation( 
    fig,
    animate,
    np.arange(1, len(Data)),
    interval=timeInt,
    blit=True,
    init_func=init
    )
plt.show()
