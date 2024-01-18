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
import matplotlib.pyplot as plt
x=[1,2,3,4]
y=[2,4,9,16] # y=x*x
plt.plot(x,y,'-o',label='y=$x^2$')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Title of my plot')
plt.legend() # try to remove and see what happens
plt.grid()   # try to remove and see what happens
plt.savefig('../fig-import/my_plot.png')
# %%
import numpy as np
x=np.array([4,5,7,8,9]) #create numpy array from a list
print(x>5) # [False, False, True, True, True]
print(np.sum(x>5)) # 3
print(x[x>5]) # [7,8,9]
print(np.sum(x[x>5]))
# %%
list1=[10,20,30] # numbers, integers
list2=[0.1,0.2,0.3] # numbers, floats
list3=['dog','cat','mouse'] #strings
# %%
def replace_chars(name,*,chars=[" ", "/"],new_chars=["","_"]):
    '''
    returns a string where chars with new_chars are replaced in name
    '''
    if type(name)!=str:
        raise ValueError('replace_chars: name must be a string')
    if len(chars) != len(new_chars):
        raise ValueError('replace_chars: chars and new_chars must same size')
    new_name = name
    for ch,nch in zip(chars,new_chars):
        new_name = new_name.replace(ch, nch)
    return new_name
def apply(f,list):
    '''
    apply f on each element in the list
    '''
    new_list=[]
    for l in list:
        new_list.append(f(l))
    return new_list
my_list=[' / /', 'a/b/c']
apply(replace_chars,my_list) # ['__','a_b_c']

# %%
def apply(f,list, *args,**kwargs):
    '''
    apply f on each element in the list
    '''
    new_list=[]
    for l in list:
        new_list.append(f(l,*args,**kwargs))
    return new_list
my_list=[' / /', 'a/b/c']
apply(replace_chars,my_list,chars=[' '],new_chars=['X']) # ['X/X/','a/b/c']

# %%
