# unit testing of the updEnergies(self) function is shown below
# on specific initial conditions. 
def updEnergies():
    m1 = 1      # 
    m2 = 2      # initial conditions upon which 
    v1 = [1,1]  # to run the unit test
    v2 = [2,2]  # 
    xy1 = [0,1] # 
    xy2 = [0,2] # 
    g = 9.81    # 
    l1 = 1      #
    l2 = 1      ##################################### 
    KE1 = 0.5 * m1 * (v1[0]*v1[0] + v1[1]*v1[1])    # the actual function from 
    KE2 = 0.5 * m2 * (v2[0]*v2[0] + v2[1]*v2[1])    # double pendulum class.
    PE1 = m1 * g * (l1+xy1[1])                      # modified such that "self."
    PE2 = m2 * g * (l1+l2+xy2[1])                   # and "DP." have been removed
    totalE = PE1 + KE1 + PE2 + KE2                  # and now returns the total Energy
    return totalE                                   # for testing puposes

def test(): # the test to assert an answer for pytest
    assert 107.1000000000001 > updEnergies() > 107.0999999999999
    # the test asserts that the total energy is found to within +-1x10^-13