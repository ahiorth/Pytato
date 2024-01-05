#%%
import pathlib as pt 

p=pt.Path('../')
# %%
p.cwd()
p=p/'data'

# %%
p.absolute()
# %%
import matplotlib.pyplot as plt
x=[1,2,3,4]
y=[1,2,3,4]
plt.title('A linear function')
plt.plot(x,y,'-o',label='y=x')
plt.xlabel('x-values')
plt.ylabel('y-values')
plt.grid()
plt.legend()
plt.savefig('../fig-import/ex1.png', bbox_inches='tight',transparent=True)
# %%
N=100 # 100 points
dx=6/(N-1)
x=[-3+i*dx for i in range(N)]
y=[i**3 for i in x]
plt.title('A non linear function')
plt.plot(x,y,label='$y=x^3$') # if you want you can add legend and grid lines
plt.xlabel('x-values')
plt.ylabel('y-values')
plt.grid()
plt.legend()
plt.savefig('../fig-import/ex2.png', bbox_inches='tight',transparent=True)

# %%
import numpy as np
N=100
x=np.linspace(-3,3,N)
y=x**3
plt.title('A non linear function')
plt.plot(x,y,label='$y=x^3$') # if you want you can add legend and grid lines
plt.xlabel('x-values')
plt.ylabel('y-values')
plt.grid()
plt.legend()

# %%
import sys
sys.path.append('../data/')
from draugen_data import years,months,oil,gas,wat,cond,oe
# %%
plt.plot(years,oe)
# %%
import pandas as pd
df=pd.read_excel('../data/field_production_gross_monthly.xlsx')
field='DRAUGEN'
file_out='../data/'+field+'.xlsx'
df2=df[df[df.columns[0]]==field]
df2.to_excel(file_out,index=False)
# %%
fields=df[df.columns[0]].unique()
for field in fields:
    new_name=str.replace(field,'/','')
    file_out='../data/'+new_name+'.xlsx'
    df2=df[df[df.columns[0]]==field]
    df2.to_excel(file_out,index=False)


# %%
import pathlib as pt
df=pd.read_excel('../data/field_production_gross_monthly.xlsx')
fields=df[df.columns[0]].unique() #skip duplicates
data_folder=pt.Path('../tmp_data')
data_folder.mkdir(exist_ok=True)
for field in fields:
    new_name=str.replace(field,'/','')
    new_path=data_folder / new_name
    new_path.mkdir(exist_ok=True)
    df2.to_excel(new_path/'production_data.xlsx',index=False)

# %%
