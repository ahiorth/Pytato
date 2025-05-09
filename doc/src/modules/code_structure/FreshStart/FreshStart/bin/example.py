#%%
import numpy as np
import matplotlib.pyplot as plt
import FreshStart

x=np.linspace(-np.pi,np.pi)
y=np.sin(x)

FreshStart.my_plot(x,y)
A=FreshStart.SomeStuff()
A.my_plot(x,y)

print(FreshStart.replace_chars('Å Æ Ø'))
# or get function directly from subfolder
print(FreshStart.code.util.replace_chars('Å Æ Ø'))

data=FreshStart.get_co2_data()
plt.plot(data[:,0],data[:,1],'-*')
plt.xlabel('Years')
plt.ylabel('CO2 emission to air')
plt.grid()
plt.title('SNORRE field')
# %%
