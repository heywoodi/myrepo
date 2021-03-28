import math

# unit testing of the Euler-method algorithm

deltaT = 0.01
def updEuler(deltaT):   #updEuler function
    a1 = math.radians(60)  #
    a2 = math.radians(60)  # 
    l1 = 1  ################
    l2 = 2  # intial conditions from which 
    m1 = 1  # to run the updEuler()
    m2 = 2  # unit testing
    w1 = 5  #
    w2 = -5 #
    g = 9.81#
    #       # below two lines are the acceleration due to gravity of the system
    aa1 = (-g*(2*m1 + m2)*math.sin(a1) - m2*g*math.sin(a1-2*a2) - 2*math.sin(a1-a2)*m2*(w2*w2 * l2 + w1*w1 * l1 * math.cos(a1-a2)))/(l1*(2*m1 + m2 - m2*math.cos(2*a1-2*a2)))
    aa2 = (2*math.sin(a1 - a2)*(w1*w1 * l1 * (m1 + m2) + g*(m1+m2)*math.cos(a1) + w2 *w2 * l2*m2*math.cos(a1-a2))) / (l2*(2*m1 + m2 - m2*math.cos(2*a1-2*a2)))
    #                       # the actual updEuler(Self, deltaT) function is here
    a1 += w1*deltaT         # updates angles first, 
    a2 += w2*deltaT         # then updates angular 
    w1 += aa1 * deltaT      # velocities based on 
    w2 += aa2 * deltaT      # acceleration of masses
    return a1, a2, w1, w2   # returns values to function should update


def test(): # test function for pytest
    a1, a2, w1, w2 = updEuler(deltaT)       # retrieving the values from updEuler()
    assert 1.097197550 <a1< 1.097197552     # asserting the values of a1, a2, w1, w2
    assert 0.997197550 <a2< 0.997197552     # to within +- 1x10^-9 each
    assert 4.915042907 <w1< 4.915042909     #
    assert -4.999999999 > w2 > -5.000000001 #