#%%
import numpy as np
a=np.array([0,1])
b=np.array([2,3])

a+b
# %%
a='1'
b='2'
float(a)+float(b)
# %%
import sys
sys.path.append('../data/')
from draugen_data import years,months,oil,gas,wat,cond,oe

[year+month/12 for month,year in zip(months,years)]
# %%
data={} #just an empty dictionary
for year,o in zip(years,oe):
    key=year
    if key in data: #key exists
       data[key] += o #add oil equivalents
    else: # new key
       data[key] = o  #set equal to first month	    	  

# %%
print(data)
# %%
import matplotlib.pyplot as plt
oe_per_year=[data[key] for key in data] #list comprehension
plt.plot(years,oe_per_year)
# %%
oe_per_year=[data[key] for key in data] #list comprehension
year=[key for key in data]
plt.plot(year,oe_per_year)
plt.bar(year,oe_per_year,color='orange')
plt.grid()
# %%
years=np.array(years) # cast to Numpy array
oe=np.array(oe) # ditto
unique_list=np.unique(years) #remove duplicates
oe_tot=[] # empty list
for year in unique_list:
    oe_tot.append(np.sum(oe[years==year]))
#make the plot
plt.plot(unique_list,oe_tot)
plt.bar(unique_list,oe_tot,color='orange')

# %%
import pandas as pd
df=pd.DataFrame()
df['Year']=years
df['oe']=oe
df2=df.groupby(by='Year').sum()

# %%
df2.plot.bar()
# %%
