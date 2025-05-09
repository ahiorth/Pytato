#%%
import matplotlib.pyplot as plt
import numpy as np
import itertools

class SomeStuff:

    def my_plot(self,x,y):
        plt.plot(x,y)
        plt.title('My Plot Class XXX')
        plt.grid()
        plt.show()
        

def my_plot(x,y):
    plt.plot(x,y)
    plt.title('My Plot')
    plt.grid()
    plt.show()



def replace_chars(name, chars=[" ", "/","Å", "Ø", "Æ"], new_chars=["_","_","AA","O","AE"]):
    ''' replace Norwegian characters and space in names'''
    new_name = name
    for ch,nch in zip(chars,new_chars):
        new_name = new_name.replace(ch, nch)
    return new_name


if __name__ == '__main__':
    x=np.linspace(-1,1,100)
    y=x*x
    my_plot(x,y)

    A=SomeStuff()
    A.my_plot(x,y)
# %%
