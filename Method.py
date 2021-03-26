import numpy as np 
import matplotlib as plt
import math
from DoublePendulum import DP #imports useful modules and double pendulum class from DoublePendulum.py
import json
import pandas as pd
import copy
from pathlib import Path

#accessing config file
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
pend.updCartesian()
pend.updEnergies()
data = []
time = 0
x1 = 0
x2 = 0
y1 = 0
y2 = 0

if method == 1:
    for n in range(nCycles):
        #print(n)
        time += timeStep
        pend.updEuler(timeStep)
        pend.updCartesian()
        pend.updEnergies()
        pend.updMomentum()
        x1 = pend.xy1[0]
        x2 = pend.xy2[0]
        y1 = pend.xy1[1]
        y2 = pend.xy2[1]
        p11 = pend.p1[0]
        p12 = pend.p1[1]
        p21 = pend.p2[0]
        p22 = pend.p2[1]
        print(p22)
        item = [time, copy.deepcopy(pend.totalE), copy.deepcopy(pend.KE1), copy.deepcopy(pend.KE2), copy.deepcopy(pend.PE1), copy.deepcopy(pend.PE2), copy.deepcopy(x1), copy.deepcopy(x2), copy.deepcopy(y1), copy.deepcopy(y2), copy.deepcopy(p11), copy.deepcopy(p12), copy.deepcopy(p21), copy.deepcopy(p22)]
        data.append(item)
elif method == 2:
    for n in range(nCycles):
        print(n)
        time += timeStep
        pend.updEulerCromer(timeStep)
        pend.updCartesian()
        pend.updEnergies()
        pend.updMomentum()
        x1 = pend.xy1[0]
        x2 = pend.xy2[0]
        y1 = pend.xy1[1]
        y2 = pend.xy2[1]
        p11 = pend.p1[0]
        p12 = pend.p1[1]
        p21 = pend.p2[0]
        p22 = pend.p2[1]
        item = [time, copy.deepcopy(pend.totalE), copy.deepcopy(pend.KE1), copy.deepcopy(pend.KE2), copy.deepcopy(pend.PE1), copy.deepcopy(pend.PE2), copy.deepcopy(x1), copy.deepcopy(x2), copy.deepcopy(y1), copy.deepcopy(y2),copy.deepcopy(p11),copy.deepcopy(p12),copy.deepcopy(p21),copy.deepcopy(p22)]
        data.append(item)
elif method == 3:
    for n in range(nCycles):
        print(n)
        time += timeStep
        pend.updRungeKutta(timeStep)
        pend.updCartesian()
        pend.updEnergies()
        pend.updMomentum()
        x1 = pend.xy1[0]
        x2 = pend.xy2[0]
        y1 = pend.xy1[1]
        y2 = pend.xy2[1]
        p11 = pend.p1[0]
        p12 = pend.p1[1]
        p21 = pend.p2[0]
        p22 = pend.p2[1]
        item = [time, copy.deepcopy(pend.totalE), copy.deepcopy(pend.KE1), copy.deepcopy(pend.KE2), copy.deepcopy(pend.PE1), copy.deepcopy(pend.PE2), copy.deepcopy(x1), copy.deepcopy(x2), copy.deepcopy(y1), copy.deepcopy(y2),copy.deepcopy(p11),copy.deepcopy(p12),copy.deepcopy(p21),copy.deepcopy(p22)]
        data.append(item)
else:
    print('invalid method selection, update config file')
    exit()

np.save(Path.cwd()/'datafile', data, allow_pickle=True)
print('data file saved')



