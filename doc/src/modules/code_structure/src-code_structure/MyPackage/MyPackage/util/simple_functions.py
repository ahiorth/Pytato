import numpy as np
import matplotlib.pyplot as plt

def myplot(x,y):
    """
    A very simple function
    """
    plt.plot(x,y,label='My special plot')
    plt.grid()
    plt.legend()