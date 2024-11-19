import numpy as np
import matplotlib.pyplot as plt


def sech(x):
    """ 
    Input: x, float64/float32 
    Output: sech(x), flaot64/float32
    """
    return 2*np.cosh(x)/(np.cosh(2*x)+1)

def soliton_solution(x,t,c=1,x0=0):
    """ 
    Input: 
    position x, float64/float32 
    time t, float64/float32
    optional:
    speed c, float64/float32
    start position x0, float64/float32
 
    Output: 
    Solution to KdV for the point x, and t: u(x,t), flaot64/float32
    """
    return -c/2*sech(1/2*np.sqrt(c)*(x-c*t-x0))**2

