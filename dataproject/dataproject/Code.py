#Import packages:
from pandas_datareader import wb
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib_venn import venn2

#Import GDP data from World bank:
gdps_wb = wb.download(indicator='NY.GDP.PCAP.KD', country=['US'], start=1990, end=2018)
gdps_wb = gdps_wb.rename(columns = {'NY.GDP.PCAP.KD':'gdp'})
gdps_wb = gdps_wb.reset_index()
gdps_wb.year = gdps_wb.year.astype(int)
gdps_wb.head(10)

gdpgrowth_wb = wb.download(indicator='NY.GDP.MKTP.KD.ZG', country=['US'], start=1990, end=2018)
gdpgrowth_wb = gdpgrowth_wb.rename(columns = {'NY.GDP.MKTP.KD.ZG':'gdp_growth'})
gdpgrowth_wb = gdpgrowth_wb.reset_index()
gdpgrowth_wb.year = gdpgrowth_wb.year.astype(int)
gdpgrowth_wb.head(10)

#Import unemployment data from excel file:
unempl = pd.read_excel('Data.xlsx')
print(unempl)

#Change type:
gdpgrowth_wb.year = gdpgrowth_wb.year.astype(int)
gdps_wb.year = gdps_wb.year.astype(int)
unempl.year = unempl.year.astype(int)

#Merge data:
mergeddata = pd.merge(unempl, gdpgrowth_wb, how='outer', on = ['year'])
print(unempl.shape)
print(gdpgrowth_wb.shape)
print(mergeddata.shape)
mergeddata.sample(10)

#Sort data:
mergeddata.sort_index()

#Clean data (drop if missing data) and convert to float:
mergeddata = mergeddata.dropna()
mergeddata.Unemployment = mergeddata.Unemployment.astype('float')
mergeddata.gdp_growth = mergeddata.gdp_growth.astype('float')

#Statistics (from problem set):
mergeddata['gdp_growth'].describe()
mergeddata['Unemployment'].describe()

#Calculate correlation
mergeddata.corr(method='pearson')

#Look at the years with increasing unemployment:
I = mergeddata['Unemployment'] > 0
mergeddata.loc[I, :].head()


# 1. take logs
#mergeddata['log_gdp_growth'] =  np.log(mergeddata['gdp_growth'])
#mergeddata['log_Unemployment'] =  np.log(mergeddata['Unemployment'])

# 2. figur: log differences
#xy = mergeddata.plot(x = 'log_gdp_growth', y = 'log_Unemployment', kind = 'scatter') 
#xy.set_xlabel('log difference in gdp_growth') 
#xy.set_ylabel('log difference in Unemployment')

#Scatter plot
xy = mergeddata.plot(x = 'Unemployment', y = 'gdp_growth', kind = 'scatter') 
xy.set_xlabel('gdp_growth') 
xy.set_ylabel('Unemployment')

#Plot timeseries
def plot(mergeddata):
   mergeddata_indexed = mergeddata.set_index('year')
   mergeddata_indexed.plot(legend=True)
    
plot(mergeddata)

#Import packages:
from numpy import arange,array,ones
from scipy import stats

#Regression:
x = mergeddata['Unemployment'] 
y = mergeddata['gdp_growth']

# Generated linear fit
slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
line = slope*x+intercept

plt.plot(x,y,'o', x, line)
ax = plt.gca()
fig = plt.gcf()
ax.set_ylabel('gdp_growth') 
ax.set_xlabel('Unemployment')

#Testing the model:

