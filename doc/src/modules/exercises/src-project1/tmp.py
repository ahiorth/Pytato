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
import pathlib as pt
p=pt.Path('../data/draugen.txt')
print(p.exists()) # will print True if yes
# %%
import sys
sys.path.append('../data/')
# %%
p=pt.Path('draugen.txt')
# %%
p.exists()
# %%
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Define the nonlinear function (Gaussian function as an example)
def nonlinear_function(x, A, mu, sigma):
    return A * np.exp(-(x - mu)**2 / (2 * sigma**2))

# Generate example data
np.random.seed(42)
x_data = np.linspace(-5, 5, 100)
y_data = nonlinear_function(x_data, A=2, mu=0, sigma=1) + 0.2 * np.random.normal(size=len(x_data))

# Fit the nonlinear function to the data using curve_fit
params, covariance = curve_fit(nonlinear_function, x_data, y_data)

# Extract the optimal parameters
A_fit, mu_fit, sigma_fit = params

# Generate y values using the fitted parameters
y_fit = nonlinear_function(x_data, A_fit, mu_fit, sigma_fit)

# Plot the original data and the fitted curve
plt.scatter(x_data, y_data, label='Original Data')
plt.plot(x_data, y_fit, label='Fitted Curve', color='red', linestyle='--')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Nonlinear Function Fitting')
plt.legend()
plt.show()

# Display the fitted parameters
print(f"Fitted Parameters:\nA: {A_fit}\nmu: {mu_fit}\nsigma: {sigma_fit}")

# %%
