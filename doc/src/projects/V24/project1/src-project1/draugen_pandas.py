#%%
import numpy as np 
import pandas as pd
import pathlib
import matplotlib.pyplot as plt

# A function to return a dataframe containin only a specific field
def df_field(name,datafile='field_production_gross_monthly.xlsx',col=0):
    folder = pathlib.Path.cwd().parent.joinpath('data')
    filename = folder.joinpath(datafile)
    df = pd.read_excel(filename)
    columns = df.columns
    return columns, df[df[df.columns[col]] == name]

def prod_data(name):
    columns, df2 = df_field(name)
    Year = df2['Year']
    Month = df2['Month']
    OilProd=df2[columns[3]]
    #Assume 30 days in each month and 365 in year
    Year = Year + Month*30/365
    return Year, OilProd

def well_data(name, datafile='wellbore_development_all.xlsx'):
    columns, df2 = df_field(name,datafile,col=14)
    Year = df2[columns[32]]
    Nowells=[]
    NewY=[]
    wells=1
    y_old=0
    for y in Year:
        try:
            index = NewY.index(y)
            Nowells[index] += 1
        except:
            NewY.append(y)
            Nowells.append(1.)
    NewY,Nowells = zip(*sorted(zip(NewY, Nowells)))
    
    return NewY, np.cumsum(Nowells)

name='OSEBERG'
#columns, df2 = df_field(name,datafile='wellbore_development_all.xls',col=14)
#print(columns)

Ny,Nw=well_data(name)
    
#print(df_field('OSEBERG'))
      

def plot_prod_data(name,well=False):
    Year,OilProd=prod_data(name)
    fig, ax1 = plt.subplots()
    plt.title(name)

    ax1.set_ylabel(r'MSm$^3$/month')
    ax1.set_xlabel('Years of production')


    lns=ax1.plot(Year,OilProd, 'b--o', label='Oil Production')
    if(well):
        Yw,Nw=well_data(name)
        ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
        ax2.set_ylabel(r'Number of Wells')
        lns2=ax2.plot(Yw,Nw, 'r--o', label='No wells')
        lns =  lns+lns2
    ax1.set_xlim(min(Year),max(Year))
    # added these three lines
    
    labs = [l.get_label() for l in lns]
    ax1.legend(lns, labs, loc=0)
 #   plt.grid()
    plt.show()
    plt.close()

def plot_cum_data(name):
    Year,OilProd=prod_data(name)
    fig, ax1 = plt.subplots()
    plt.title(name)

    ax1.set_ylabel(r'Cummulative production MSm$^3$')
    ax1.set_xlabel('Number of wells')

    Year,OilProd=prod_data(name)
    Yw,Nw=well_data(name)

    Nw = np.interp(Year,Yw,Nw)
    CumOil=np.cumsum(OilProd)

    ax1.plot(Nw,CumOil, 'r--o')

    plt.grid()
    plt.show()
    plt.close()
    
plot_prod_data(name,True)
plot_cum_data(name)

name = 'DRAUGEN'
Year,OilProd=prod_data(name)

from scipy.optimize import curve_fit

def exp_decline(x,A,D):
    return A*np.exp(-D*x)

#start at 0
ProdStart = Year.iloc[0]
Year = Year-ProdStart
# only choose data from the decline phase (i.e. after approx. 8 years)
T0 = 8
# extract indexes 
ind = Year > T0;
# cooresponding X and Y-value
NewY = Year[ind]-T0; #important to start at 0
NewP = OilProd[ind];

CumOilProd = np.cumsum(OilProd)
popt, pcov = curve_fit(exp_decline, NewY, NewP)

model = exp_decline(NewY,popt[0],popt[1])

#plt.clf()
fig, ax1 = plt.subplots()

plt.title('Draugen production profile')
ax1.set_ylabel(r'MSm$^3$/month')
ax1.set_xlabel('Years of production')

ax1.plot(Year,OilProd, 'b--o')
ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
ax2.set_ylabel(r'Cumulative production [MSm$^3$]')
ax2.plot(Year,CumOilProd, 'r--o')
ax1.plot(NewY+T0,model, 'k-',lw='2',label="model")
ax1.legend(loc=(0.75,0.75))
plt.show()





# %%
_,df_dr=df_field('DRAUGEN')
# %%
df_dr.to_csv('./draugen.csv', index=False)
# %%
a=np.loadtxt('../data/draugen.txt',skiprows=1)
# %%
with open("../data/draugen.txt") as my_file:
     for line in my_file:
     	 print(line)
# %%
year=[] # empty list
oe=[] # empty list
read_first_line=False
with open("../data/draugen.txt") as my_file:
    for line in my_file:
        if read_first_line:
            data_list=line.split('\t')
            year.append(float(data_list[0])+float(data_list[1])/12)
        read_first_line=True
	 

# %%
data_dict={'year':[], 'month':[],'oil':[],'gas':[],'cond':[],'oe':[],'wat':[]}
read_first_line=False
with open("../data/draugen.txt") as my_file:
    for line in my_file:
        if read_first_line:
            data_list=line.split('\t')
            for key,data in zip(data_dict,data_list):
                data_dict[key].append(float(data))
        read_first_line=True

# %%
import sys
sys.path.append('../data/')
from draugen_data import year,month,oil,gas,wat,cond,oe

# %%
import matplotlib.pyplot as plt

plt.plot(year,oe)
# %%
import pandas as pd
field='JOTUN'
col='Field (Discovery)'
df=pd.read_excel('../data/field_production_gross_monthly.xlsx')
df2=df[df[col] == field]
# %%
cols=[1,2,3,4,6,7]
names=['years','months','oil_gross','gas_gross','oe_gross','wat_prod']

with open(field.lower()+'_data.py','w') as f:
    for col,coln in zip(cols,names):
        f.write(coln+'=')
        f.write(str(list(df2.iloc[:,col])))
        f.write('\n')




# %%
from jotun_data import years, months, oil_gross,gas_gross, oe_gross, wat_prod
# %%
import matplotlib.pyplot as plt
plt.plot(years,oe_gross,'-o',c='g',label='Oil Equivalents')
plt.xlabel('Years')
plt.ylabel('Produced volumes [10$^6$ Sm$^3$] per month')
plt.title('Jotun')
plt.grid()
plt.legend()
plt.savefig('../fig-project1/jotun.png')
# %%
import numpy as np
xx=np.array(oil_gross)+np.array(gas_gross)
print(xx[:10])
oe_gross[:10]
# %%
years_np=np.array(years)
oe_np=np.array(oe_gross)
y_un=np.unique(years_np)
oe_tot=[]
for y in y_un:
    oe_tot.append(np.sum(oe_np[years_np==y]))

plt.bar(y_un,oe_tot,label='Oil Equivalents')
plt.xlabel('Years')
plt.ylabel('Produced volumes [10$^6$ Sm$^3$] per year')
plt.title('Jotun')
plt.grid()
plt.legend()
plt.savefig('../fig-project1/jotun_oe.png')
# %%

np.sum(oe_np[years_np==2000])

# %%
my_dict={'year':years,'month':months,'oil':oil_gross,
         'gas':gas_gross,'wat':wat_prod,'oe':oe_gross}

for key in my_dict:
    print(key)
    print(my_dict[key])
# %%
df=pd.DataFrame(my_dict)
df.groupby('year').sum()
# %%
df.groupby('year').sum()
# %%
import pathlib as pt
def get_data(field):
    """
    Extracts data for a specific field
    """
    field = field.upper() #optional
    df_prod=pd.read_excel('../data/field_production_gross_monthly.xlsx')
    df= df_prod[df_prod['Field (Discovery)'] == field]
    if df.empty: #optional
        print('No data for ', field)
    return df
field='JOTUN'
df=get_data(field)
data_folder=pt.Path('tmp_data')
data_folder.mkdir(exist_ok=True)
new_name=str.replace(field,'/','')
new_path=data_folder / new_name
new_path.mkdir(exist_ok=True)
df2=df[df[df.columns[0]]==field]
df2.to_excel(new_path/'production_data.xlsx',index=False)
# %%
def write_data(field):
    df=get_data(field)
    data_folder=pt.Path('tmp_data')
    data_folder.mkdir(exist_ok=True)
    new_name=str.replace(field,'/','')
    new_path=data_folder / new_name
    new_path.mkdir(exist_ok=True)
    df2=df[df[df.columns[0]]==field]
    try:
        df2.to_excel(new_path/'production_data.xlsx',index=False)
    except:
        print('Failed to save data, for field ')
    return 

write_data('JOTUN')
# %%
df=pd.read_excel('../data/field_production_gross_monthly.xlsx')
fields=df[df.columns[0]].unique() #skip duplicates
data_folder=pt.Path('tmp_data')
data_folder.mkdir(exist_ok=True)
for field in fields:
    new_name=str.replace(field,'/','')
    new_path=data_folder / new_name
    new_path.mkdir(exist_ok=True)
    df2=df[df[df.columns[0]]==field]
    file=new_name+'.xlsx'
    df2.to_excel(new_path/file,index=False)
# %%
def find_files_of_type(dir='.',extensions=['.xlsx','.txt','.INC']):
    """
    return a list files of type defined in extensions
    """
    p=pt.Path(dir)
    files=[]
    for ext in extensions:
        for x in p.rglob("*"+ext):
            if x.is_file():
                files.append(x.absolute())
    return files

import shutil 
p=pt.Path('.')
trash_folder=pt.Path('Trash')
trash_folder.mkdir(exist_ok=True)
for x in p.rglob('*.xlsx'):
    if x.is_file():
        shutil.move(x,trash_folder)
# %%
import numpy as np
import matplotlib.pyplot as plt
class DeclineCurve:
    def __init__(self,q,tau):
        self.q=q 
        self.tau=tau
    
    def f(self,t):
        return self.q*np.exp(-t/self.tau)

    def plot(self):
        t=np.linspace(0,10,1000)
        y=self.f(t)
        plt.plot(t,y)
        plt.grid()
        plt.xlabel('t')
        plt.ylabel('f(t)')
        plt.savefig('../fig-project1/decline.png')    
A=DeclineCurve(1,1)
A.plot()
# %%
