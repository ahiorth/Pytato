#%%
import pandas as pd 

dict={'col1':['aa', ' aa ', 'a b c '],'col2':[1,2,3]}
df=pd.DataFrame(dict)
df['col1'].apply(lambda x: x.strip())
#%%
def remove_space(x):
    return x.strip()
print(df)
df['col1']=df['col1'].apply(remove_space)
print(df)
# %%
df.loc[:,'col1']

# %%
dict={'col1':['aa', ' aa ', 'a b c '],'col2':[1,2,3]}
df=pd.DataFrame(dict)
print(df)
df['col1'].str.strip()
print(df)
# %%
remove_space=lambda x : x.strip()
remove_space('  a a ')
# %%
