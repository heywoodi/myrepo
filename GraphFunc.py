import numpy as np
import json
#module of graphing functions



def getTime(Data):
    ''' returns an np array
    of time values from
    data file '''
    time = []
    for n in Data:
        time.append(n[0])
    return np.array(time)

def getx1(Data):
    ''' returns an np array
    of x1 position values from
    data file '''
    x1 = []
    for n in Data:
        x1.append(n[6])
    return np.array(x1)

def getx2(Data):
    ''' returns an np array
    of x2 position values from
    data file '''
    x2 = []
    for n in Data:
        x2.append(n[7])
    return np.array(x2)

def gety1(Data):
    ''' returns an np array
    of y1 position values from
    data file '''
    y1 = []
    for n in Data:
        y1.append(n[8])
    return np.array(y1)

def gety2(Data):
    ''' returns an np array
    of y2 position values from
    data file '''
    y2 = []
    for n in Data:
        y2.append(n[9])
    return np.array(y2)

def getInterval(Data):
    ''' Findthe correct time interval from
    config file '''
    with open('config.json') as config_file:
        initdata = json.load(config_file)
    timeStep = initdata['Time Step']
    interval = timeStep*1000
    return interval

def getE(Data):
    ''' returns an np array
    of total energy from
    data file '''
    E = []
    for n in Data:
        E.append(n[1])
    return np.array(E)

def getKE1(Data):
    ''' returns an np array
    of kinetic energy of
    mass 1 from data file '''
    ke1 = []
    for n in Data:
        ke1.append(n[2])
    return np.array(ke1)

def getKE2(Data):
    '''  returns an np array
    of kinetic energy of
    mass 2 from data file  '''
    ke2 = []
    for n in Data:
        ke2.append(n[3])
    return np.array(ke2)

def getPE1(Data):
    '''  returns an np array
    of potential energy of
    mass 1 from data file  '''
    pe1 = []
    for n in Data:
        pe1.append(n[4])
    return np.array(pe1)

def getPE2(Data):
    '''  returns an np array
    of potential energy of
    mass 2 from data file  '''
    pe2 = []
    for n in Data:
        pe2.append(n[5])
    return np.array(pe2)

def getP11(Data):
    ''' returns numpy array of
    i-momentum for mass 1 '''
    P11 = []
    for n in Data:
        P11.append(n[10])
    return np.array(P11)

def getP12(Data):
    ''' returns numpy array of
    j-momentum for mass 1'''
    P12 = []
    for n in Data:
        P12.append(n[11])
    return np.array(P12)

def getP21(Data):
    ''' returns numpy array of
    i-momentum for mass 2 '''
    P21 = []
    for n in Data:
        P21.append(n[12])
    return np.array(P21)

def getP22(Data):
    ''' returns numpy array of
    j-momentum for mass 2 '''
    P22 = []
    for n in Data:
        P22.append(n[13])
    return np.array(P22)