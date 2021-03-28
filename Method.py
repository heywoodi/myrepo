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

#accessing configuration file (config.JSON)
with open('config.json') as config_file:
    initdata = json.load(config_file)

#retrieving variables from config file
initMA = initdata['Mass A']
initMB = initdata['Mass B']
initLA = initdata['Length A']
initLB = initdata['Length B']
initAA = initdata['Angle A']
initAB = initdata['Angle B']
method = initdata['Method']
timeStep = initdata['Time Step']
nCycles = initdata['Number of Cycles']

# Setting Initial Conditions based on the config file
pend = DP(initMA,initMB,initLA,initLB,math.radians(initAA),math.radians(initAB),[0,0],[0,0],[0,0],[0,0],0,0,1,1,1,1,1,1,1)
pend.updCartesian() # initial cartesians
pend.updEnergies()  # inital energies
data = []           #create empty data list
time = 0            # inital time
x1 = 0              #
x2 = 0              # initial x and y
y1 = 0              # variables
y2 = 0              #

# 'if' statement checks which method to use for simulation
if method == 1:                     # method 1 == euler method
    for n in range(nCycles):            # iterates through the number of cycles
        time += timeStep                # increases time each time with timestep
        pend.updEuler(timeStep)         # updates the system based on euler method
        pend.updCartesian()             # updates the cartesian properties
        pend.updEnergies()              # updates the energy properties
        pend.updMomentum()              # updates the momentum properties
        x1 = pend.xy1[0]                # 
        x2 = pend.xy2[0]                # separates out the x and
        y1 = pend.xy1[1]                # y variables of position for storing
        y2 = pend.xy2[1]                #
        p11 = pend.p1[0]                #
        p12 = pend.p1[1]                # seperates out i and j comp
        p21 = pend.p2[0]                # of momentums for storing
        p22 = pend.p2[1]                #
        item = [time, copy.deepcopy(pend.totalE), copy.deepcopy(pend.KE1), copy.deepcopy(pend.KE2), copy.deepcopy(pend.PE1), copy.deepcopy(pend.PE2), copy.deepcopy(x1), copy.deepcopy(x2), copy.deepcopy(y1), copy.deepcopy(y2), copy.deepcopy(p11), copy.deepcopy(p12), copy.deepcopy(p21), copy.deepcopy(p22)]
        data.append(item)               # appends data with item list  

elif method == 2:                   # method 2 == euler cromer
    for n in range(nCycles):            # iterates through the number of cycles
        time += timeStep                # increases time each time with timestep
        pend.updEulerCromer(timeStep)   # updates the system based on euler-cromer method
        pend.updCartesian()             # updates the cartesian properties
        pend.updEnergies()              # updates the momentum properties
        pend.updMomentum()              # separates out the x and
        x1 = pend.xy1[0]                # y variables of position for storing
        x2 = pend.xy2[0]                #
        y1 = pend.xy1[1]                #
        y2 = pend.xy2[1]                #
        p11 = pend.p1[0]                #
        p12 = pend.p1[1]                # seperates out i and j comp
        p21 = pend.p2[0]                # of momentums for storing
        p22 = pend.p2[1]                #
        item = [time, copy.deepcopy(pend.totalE), copy.deepcopy(pend.KE1), copy.deepcopy(pend.KE2), copy.deepcopy(pend.PE1), copy.deepcopy(pend.PE2), copy.deepcopy(x1), copy.deepcopy(x2), copy.deepcopy(y1), copy.deepcopy(y2),copy.deepcopy(p11),copy.deepcopy(p12),copy.deepcopy(p21),copy.deepcopy(p22)]
        data.append(item)               # appends data with item list  

elif method == 3:                   # method 3 == RK4
    for n in range(nCycles):            # iterates through the number of cycles
        time += timeStep                # updates the time 
        pend.updRungeKutta(timeStep)    # updates the system ODES based on RK4 method
        pend.updCartesian()             # updates cartesian properties
        pend.updEnergies()              # updates energy properties
        pend.updMomentum()              # updates momentum properties
        x1 = pend.xy1[0]                # 
        x2 = pend.xy2[0]                # seperates x and y variables
        y1 = pend.xy1[1]                # of position for storing
        y2 = pend.xy2[1]                #
        p11 = pend.p1[0]                #
        p12 = pend.p1[1]                # separates i and j comps
        p21 = pend.p2[0]                # of momenutm for storing
        p22 = pend.p2[1]                #
        item = [time, copy.deepcopy(pend.totalE), copy.deepcopy(pend.KE1), copy.deepcopy(pend.KE2), copy.deepcopy(pend.PE1), copy.deepcopy(pend.PE2), copy.deepcopy(x1), copy.deepcopy(x2), copy.deepcopy(y1), copy.deepcopy(y2),copy.deepcopy(p11),copy.deepcopy(p12),copy.deepcopy(p21),copy.deepcopy(p22)]
        data.append(item)               # appends data with item list 
else:
    print('invalid method selection, update config file')   # incase config selection is wrong,
    exit()                                                  # avoid corrupt datafile

np.save(Path.cwd()/'datafile', data, allow_pickle=True)     # pickles list of data
print('data file saved')                                    # tells you when code is done



