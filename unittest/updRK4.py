import math 
import numpy as np 

# unit testing of the 4th order multivariable 
# Runge-Kutta (RK4) algorithm from the Double Pendulum class.
# The function RK4DashArray(...) creates np array of system ODES to
# update each cycle. the function updRungeKutta(...) cycles through.
# instances of (self.) and (DP.) have been removed in order
# as rrunning algorithm from initial conditions rather than a DP(...) object
# from Double Pendulum Class

def RK4XDashArray(w1, w2, theta1, theta2):
    l1 = 1  ################
    l2 = 2  # some intial conditions
    m1 = 1  # from which to run
    m2 = 2  # the unit testing
    g = 9.81# below two lines are the acceleration of the system (ODE's), below that are the angle derivatives (ODE's)
    w1dash = (-g*(2*m1 + m2)*math.sin(theta1) - m2*g*math.sin(theta1-2*theta2) - 2*math.sin(theta1-theta2)*m2*(w2*w2 * l2 + w1*w1 * l1 * math.cos(theta1-theta2)))/(l1*(2*m1 + m2 - m2*math.cos(2*theta1-2*theta2)))
    w2dash = (2*math.sin(theta1 - theta2)*(w1*w1 * l1 * (m1 + m2) + g*(m1+m2)*math.cos(theta1) + w2 *w2 * l2*m2*math.cos(theta1-theta2))) / (l2*(2*m1 + m2 - m2*math.cos(2*theta1-2*theta2)))
    theta1dash = w1                                             # returns a numpy array of first order ODES and
    theta2dash = w2                                             # accelerations and angular velocities
    return np.array([w1dash, w2dash, theta1dash, theta2dash])   # for use in multivaribale RK4

def updRungeKutta(h):   # This function is the actual RK4 algorithm
    a1 = math.radians(60)   # some initial conditions 
    a2 = math.radians(60)   # from which to run 
    w1 = 5                  # the unit testing
    w2 = -5                 #
    Xn = np.array([w1, w2, a1, a2])     # creating an array of the variables to update
    an = RK4XDashArray(w1, w2, a1, a2)  # next 4 lines create the arrays for the RK4 algorithm steps# an
    bn = RK4XDashArray(w1 + 0.5*h*an[0], w2 + 0.5*h*an[1], a1 + 0.5*h*an[2], a2 + 0.5*h*an[3])      # bn
    cn = RK4XDashArray(w1 + 0.5*h*bn[0], w2 + 0.5*h*bn[1], a1 + 0.5*h*bn[2], a2 + 0.5*h*bn[3])      # cn
    dn = RK4XDashArray(w1 + h*cn[0], w2 + h*cn[1], a1 + h*cn[2], a2 + h*cn[3])                      # dn
    #                                               # This code cycles through the multivariable RK4 method (an-dn)
    Xn += ( 1/6 ) * h * (an + 2*bn + 2*cn + dn)     # with each step being applied to all 4 ODES simultaneously
    #                                               # and updates the array of variables 
    w1 = Xn[0]                                 # updating the
    w2 = Xn[1]                                 # angles and
    a1 = Xn[2]                                 # angular velocities
    a2 = Xn[3]                                 # from Xn array of variables
    return w1, w2, a1, a2                      # Returns values to unit test

def test():
    h = 0.01 # set the timestep
    w1,w2,a1,a2 = updRungeKutta(h)
    assert 4.8369088160 <w1< 4.8369088162
    assert -4.9544893806 <w2< -4.9544893804
    assert 1.0965080691 <a1< 1.0965080693
    assert 0.9973519112 <a2< 0.9973519114