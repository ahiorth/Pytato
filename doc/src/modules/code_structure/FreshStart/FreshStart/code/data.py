import os
import numpy as np

def get_co2_data():
    """
    reads co2 emmissions for Snorre field per year
    """
    absolute_path = os.path.dirname(__file__)
    co2_data=os.path.join(absolute_path,'../data/snorre_co2.dat')

    return np.loadtxt(co2_data)