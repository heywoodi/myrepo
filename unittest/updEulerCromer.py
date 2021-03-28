import math

# unit testing of the Euler-Cromer-method algorithm
# almost the same as euler-method
deltaT = 0.01
def updEuler(deltaT):   #updEuler function
    a1 = math.radians(60)  #
    a2 = math.radians(60)  # 
    l1 = 1  ################
    l2 = 2  # intial conditions from which 
    m1 = 1  # to run the updEulerCromer()
    m2 = 2  # unit testing
    w1 = 5  #
    w2 = -5 #
    g = 9.81#
    #       # below two lines are the acceleration due to gravity of the system
    aa1 = (-g*(2*m1 + m2)*math.sin(a1) - m2*g*math.sin(a1-2*a2) - 2*math.sin(a1-a2)*m2*(w2*w2 * l2 + w1*w1 * l1 * math.cos(a1-a2)))/(l1*(2*m1 + m2 - m2*math.cos(2*a1-2*a2)))
    aa2 = (2*math.sin(a1 - a2)*(w1*w1 * l1 * (m1 + m2) + g*(m1+m2)*math.cos(a1) + w2 *w2 * l2*m2*math.cos(a1-a2))) / (l2*(2*m1 + m2 - m2*math.cos(2*a1-2*a2)))
    #                       # the actual updEulerCromer(Self, deltaT) function is here
    w1 += aa1 * deltaT      # updates angular velocities
    w2 += aa2 * deltaT      # based on acceleration first
    a2 += w2*deltaT         # then updates the angles based
    a1 += w1*deltaT         # on angular velocities.
    return a1, a2, w1, w2   # returns values the function should update


def test(): # test function for pytest
    a1, a2, w1, w2 = updEuler(deltaT)       # retrieving the values from updEulerCromer()
    assert  1.096347980<a1< 1.096347981     # asserting the values of a1, a2, w1, w2
    assert  0.9971975511 <a2< 0.9971975513  # to within +- 1x10^-9 of calculated each
    assert 4.915042907 <w1< 4.915042909     #
    assert -4.999999999 > w2 > -5.000000001 #

test()