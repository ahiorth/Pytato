#%%
import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv('../data/WHO-COVID-19-global-data.csv')
df['Date_reported']=pd.to_datetime(df['Date_reported'])

#%%
t=df['Date_reported']
y=df['New_cases']
plt.plot(t,y)
# %%
df.plot(x='Date_reported',y='New_cases')
# %%
df.plot(x='Date_reported',y='New_deaths')
#få det til å se fint ut
# %%
#df=df.set_index('Date_reported')
# %%
df2=df[df['Country']=='Norway']
# %%
df2.plot(x='Date_reported',y='New_deaths')

# %%
