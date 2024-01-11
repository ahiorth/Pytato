#%%
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

class ProdData:
    """
    A class to extract production data from FactPages
    """
    def __init__(self):
        self.df_prod=pd.read_excel('../../import/data/field_production_gross_monthly.xlsx')
    
    def get_data(self,field):
        """
        Extracts data for a specific field
        """
        field=field.upper()
        df= self.df_prod[(self.df_prod['Field (Discovery)'] == field)]
        if df.empty:
             print('No data for ', field)
        return df
    
    def plot(self,field,cols=[3,4,5,6,7]):
        """
        Plots the different columns in the DataFrame
        """
        df=self.get_data(field)
        xcol=df['Year']+df['Month']/12
        for col in cols:
            plt.plot(xcol,df.iloc[:,col],label=df.columns[col])
        plt.legend(loc='center', bbox_to_anchor=(0.5,-.3),
          ncol=3, fancybox=True, shadow=True)
        plt.title(field)
        plt.xlabel('Years')
        plt.ylabel('mill Sm$^3$')
        plt.grid()


        
ff=ProdData()
ff.plot('DRAUGEN')

# %%
df=pd.read_excel("https://factpages.sodir.no/public?/Factpages/external/tableview/field_production_gross_monthly&rs:Command=Render&rc:Toolbar=false&rc:Parameters=f&IpAddress=not_used&CultureCode=en&rs:Format=EXCELOPENXML&Top100=false")
# %%
def get_data(field):
        """
        Extracts data for a specific field
        """
        df_prod=pd.read_excel('../../import/data/field_production_gross_monthly.xlsx')
        df= df_prod[df_prod['Field (Discovery)'] == field]
        return df

df=get_data('DRAUGENx')
# %%
