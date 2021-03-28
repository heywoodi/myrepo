import numpy as np 
import matplotlib.pyplot as plt
import math
import json
import pandas as pd
import copy
from pathlib import Path
from matplotlib.animation import FuncAnimation 
import GraphFunc as func

class DP():

    g = 9.81 # gravitational acceleration constant g (can refer back as DP.g)

    def __init__(self, m1, m2, l1, l2, a1, a2, xy1, xy2, v1, v2, w1, w2, KE1, KE2, PE1, PE2, totalE, p1, p2):
        ''' initialization of a double pendulum class variables '''
        self.m1 = m1
        self.m2 = m2
        self.l1 = l1
        self.l2 = l2
        self.a1 = a1
        self.a2 = a2
        self.xy1 = [0,0]
        self.xy2 = [0,0]
        self.vel1 = [0,0]
        self.vel2 = [0,0]
        self.w1 = w1
        self.w2 = w2
        self.KE1 = KE1
        self.KE2 = KE2
        self.PE1 = PE1
        self.PE2 = PE2
        self.totalE = totalE
        self.p1 = [0,0]
        self.p2 = [0,0]


    def __str__(self):
        ''' setting a print string for the class object'''
        return "A double pendulum with masses m1 = {} and m2 = {}, lengths l1 = {} and l2 = {}, and angles a1 = {} and a2 = {}".format(
            str(self.m1), str(self.m2), str(self.l1), str(self.l2), str(self.a1), str(self.a2)
        )


    def updCartesian(self):
        ''' Updates cartesian coords and linear velocities of the souble pendulum masses
        based on the polar coords of radius (pendulum length) and angle '''

        x1 = self.l1 * math.sin(self.a1)            #
        x2 = x1 + self.l2 * math.sin(self.a2)       # This Group of code is 
        y1 = -self.l1 * math.cos(self.a1)           # responsible for updating
        y2 = y1 - self.l2 * math.cos(self.a2)       # cartesian coords o
        self.xy1 = [x1, y1]                         # the masses
        self.xy2 = [x2, y2]                         #


        vx1 = self.w1 * self.l1 * math.cos(self.a1)         #
        vy1 = self.w1 * self.l1 * math.sin(self.a1)         # This group of code is
        vx2 = vx1 + self.w2 * self.l2 * math.cos(self.a2)   # responsible for updating
        vy2 = vy1 + self.w2 * self.l2 * math.sin(self.a2)   # linear velocities of
        self.v1 = [vx1,vy1]                                 # the masses
        self.v2 = [vx2,vy2]                                 #


    def updEnergies(self):
        ''' updates the kinetic, potential, and total eenrgy of the system based on linear 
        velocities, mass, and cravitational constant DP.g '''
        self.KE1 = 0.5 * self.m1 * (self.v1[0]*self.v1[0] + self.v1[1]*self.v1[1])  # updating Kinetic Energies
        self.KE2 = 0.5 * self.m2 * (self.v2[0]*self.v2[0] + self.v2[1]*self.v2[1])  #

        self.PE1 = self.m1 * DP.g * (self.l1+self.xy1[1])                           # updating potential energies as mgh
        self.PE2 = self.m2 * DP.g * (self.l1+self.l2+self.xy2[1])                   # h is set so that rest PE's are both 0

        self.totalE = self.PE1 + self.KE1 + self.PE2 + self.KE2                     # updating total energy

    def updMomentum(self):
        ''' updates the momentum of the pendulum masses '''
        self.p1 = [ self.m1 * self.v1[0] , self.m1 * self.v1[1] ]       # updates momentum of mass 1
        self.p2 = [ self.m2 * self.v2[0] , self.m2 * self.v2[1] ]       # updates momentum of mass 2


    def updEuler(self, deltaT):
        ''' Numerical integration based on the Euler Method'''
        aa1 = (-DP.g*(2*self.m1 + self.m2)*math.sin(self.a1) - self.m2*DP.g*math.sin(self.a1-2*self.a2) - 2*math.sin(self.a1-self.a2)*self.m2*(self.w2*self.w2 * self.l2 + self.w1*self.w1 * self.l1 * math.cos(self.a1-self.a2)))/(self.l1*(2*self.m1 + self.m2 - self.m2*math.cos(2*self.a1-2*self.a2)))
        aa2 = (2*math.sin(self.a1 - self.a2)*(self.w1*self.w1 * self.l1 * (self.m1 + self.m2) + DP.g*(self.m1+self.m2)*math.cos(self.a1) + self.w2 *self.w2 * self.l2*self.m2*math.cos(self.a1-self.a2))) / (self.l2*(2*self.m1 + self.m2 - self.m2*math.cos(2*self.a1-2*self.a2)))
        #                                 above two lines process the angular acceleration of both masses
        self.a1 += self.w1*deltaT       # first step in euler, 
        self.a2 += self.w2*deltaT       # update angles

        self.w1 += aa1 * deltaT         # second step in euler
        self.w2 += aa2 * deltaT         # update angular velocities


    def updEulerCromer(self, deltaT):
        ''' Numerical integration based on the Euler-Cromer Method '''
        aa1 = (-DP.g*(2*self.m1 + self.m2)*math.sin(self.a1) - self.m2*DP.g*math.sin(self.a1-2*self.a2) - 2*math.sin(self.a1-self.a2)*self.m2*(self.w2*self.w2 * self.l2 + self.w1*self.w1 * self.l1 * math.cos(self.a1-self.a2)))/(self.l1*(2*self.m1 + self.m2 - self.m2*math.cos(2*self.a1-2*self.a2)))
        aa2 = (2*math.sin(self.a1 - self.a2)*(self.w1*self.w1 * self.l1 * (self.m1 + self.m2) + DP.g*(self.m1+self.m2)*math.cos(self.a1) + self.w2 *self.w2 * self.l2*self.m2*math.cos(self.a1-self.a2))) / (self.l2*(2*self.m1 + self.m2 - self.m2*math.cos(2*self.a1-2*self.a2)))
        #                                 above two lines process the angular acceleration of both masses
        self.w1 += aa1 * deltaT         # first step in euler-cromer
        self.w2 += aa2 * deltaT         # update angular velocities

        self.a1 += self.w1*deltaT       # second step in euler cromer
        self.a2 += self.w2*deltaT       # update angles

    def RK4XDashArray(self, w1, w2, theta1, theta2):
        ''' returns a numpy array of the four first order ODEs that make up the double pendulum system
        as set-up for the multivariable runge kutta '''
        w1dash = (-DP.g*(2*self.m1 + self.m2)*math.sin(theta1) - self.m2*DP.g*math.sin(theta1-2*theta2) - 2*math.sin(theta1-theta2)*self.m2*(w2*w2 * self.l2 + w1*w1 * self.l1 * math.cos(theta1-theta2)))/(self.l1*(2*self.m1 + self.m2 - self.m2*math.cos(2*theta1-2*theta2)))
        w2dash = (2*math.sin(theta1 - theta2)*(w1*w1 * self.l1 * (self.m1 + self.m2) + DP.g*(self.m1+self.m2)*math.cos(theta1) + w2 *w2 * self.l2*self.m2*math.cos(theta1-theta2))) / (self.l2*(2*self.m1 + self.m2 - self.m2*math.cos(2*theta1-2*theta2)))
        theta1dash = w1                                             # createa a numpy array of first order ODES
        theta2dash = w2                                             # ang accelerations and angular velocities
        return np.array([w1dash, w2dash, theta1dash, theta2dash])   # for use in multivaribale RK4

    def updRungeKutta(self, h):
        ''' uses RK4DashArray() to perform numerical integration based on
        the 4th order multi-variable Runge-Kutta Method '''

        Xn = np.array([self.w1, self.w2, self.a1, self.a2])     # creating an array of the variables to update
        #                                                       # 
        an = self.RK4XDashArray(self.w1, self.w2, self.a1, self.a2) 
        bn = self.RK4XDashArray(self.w1 + 0.5*h*an[0], self.w2 + 0.5*h*an[1], self.a1 + 0.5*h*an[2], self.a2 + 0.5*h*an[3])
        cn = self.RK4XDashArray(self.w1 + 0.5*h*bn[0], self.w2 + 0.5*h*bn[1], self.a1 + 0.5*h*bn[2], self.a2 + 0.5*h*bn[3])
        dn = self.RK4XDashArray(self.w1 + h*cn[0], self.w2 + h*cn[1], self.a1 + h*cn[2], self.a2 + h*cn[3])
        #                                               # This code cycles through the multivariable RK4 method (an-dn)
        Xn += ( 1/6 ) * h * (an + 2*bn + 2*cn + dn)     # with each step being applied to all 4 ODES simultaneously
        #                                               # and updates the array of variables 
        #
        self.w1 = Xn[0]                                 # updating the
        self.w2 = Xn[1]                                 # angles and
        self.a1 = Xn[2]                                 # anglular velocities
        self.a2 = Xn[3]                                 # from Xn array of variables
            





