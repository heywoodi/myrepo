# unit testing of the updMomentum(self) function from
# double pendulum class on specific initial condition
def updMomentum(): #function to be tested on
    m1 = 1      # setting initial conditions
    m2 = 2      # for the pytest
    v1 = [1,2]  #
    v2 = [3,4]  #
    #           ######################### actual updMomentum(self) function
    p1 = [ m1 * v1[0] , m1 * v1[1] ]    # from double pendulum class. All (self.)
    p2 = [ m2 * v2[0] , m2 * v2[1] ]    # instances removed to work with initial
    return p1,p2                        # conditions, and returns both momentums

def test():     # test function for unit testing
    p1,p2 = updMomentum()   #
    assert p1[0] == 1       # asserting the values of momentum
    assert p1[1] == 2       # x and y components.
    assert p2[0] == 6       # exact values are able to
    assert p2[1] == 8       # be asserted