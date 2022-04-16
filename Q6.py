import pandas as pd
import numpy as np
df = pd.read_csv("./country_vaccination_stats.csv")


min=df.groupby('country').min().reset_index().set_index('country')['daily_vaccinations']
#print(min)

NaN=np.where(df.daily_vaccinations.isnull()) 
#print(NaN)

for i in NaN:
    df["daily_vaccinations"][i]=min[df['country'][i]] 

NaNForNoValues=np.where(df.daily_vaccinations.isnull())

if(len(NaNForNoValues)):
    for i in NaNForNoValues:
        df.daily_vaccinations[i]=0

print(df[df['date']=='1/6/2021']['daily_vaccinations'].sum())
