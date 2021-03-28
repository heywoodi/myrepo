import math
# unit testing of the updCartesian(self) function is shown below
# on specific initial conditions. 
def updCartesian():      
    a1 = math.radians(90)   # 
    a2 = math.radians(90)   # setting initial conditions required
    l1 = 1                  # for the pytest. includes
    l2 = 2                  # angles, lengths, and
    w1 = 1                  # angular velocities
    w2 = -2                 #
    #                       #############
    x1 = l1 * math.sin(a1)              # 
    x2 = x1 + l2 * math.sin(a2)         # actual upCartesian()
    y1 = -l1 * math.cos(a1)             # function found in 
    y2 = y1 - l2 * math.cos(a2)         # the double pendulum class.
    xy1 = [x1, y1]                      # 
    xy2 = [x2, y2]                      # first blcok of code
    #                                   # updates cartesian locations
    vx1 = w1 * l1 * math.cos(a1)        # second group updates cartesian velocities.
    vy1 = w1 * l1 * math.sin(a1)        # (self.) and (DP.) variables have been
    vx2 = vx1 + w2 * l2 * math.cos(a2)  # removed since no longer working from DP class
    vy2 = vy1 + w2 * l2 * math.sin(a2)  # 
    v1 = [vx1,vy1]                      # returns both masses velocities and 
    v2 = [vx2,vy2]                      # position vectors to test the
    return v1, v2 , xy1, xy2            # 

def test(): # Defining a test function for testing
    v1, v2, xy1, xy2 = updCartesian()               # retrives variables from function
    assert xy1[0] == 1                              # assertion of mass1 x position
    assert xy2[0] == 3                              # assertion of mass2 x position
    assert 0-0.0000000001 < xy1[1] < 0+0.0000000001 # assertion of mass1 y position
    assert 0-0.0000000001 < xy2[1] < 0+0.0000000001 # assertion of mass2 y position
    #                                               # all assertions are to +-1*10-10 at most
    assert 0-0.0000000001 < v1[0] < 0+0.0000000001  # assertion of mass1 x-velocity 
    assert 0-0.0000000001 < v2[0] < 0+0.0000000001  # assertion of mass2 x-velocity
    assert v1[1] == 1                               # assertion of mass1 y-velocity
    assert v2[1] == -3                              # assertion of mass2 y-velocity