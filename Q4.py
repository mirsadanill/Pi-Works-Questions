import pandas as pd
import numpy as np
df = pd.read_csv("./country_vaccination_stats.csv")
df['date'] = pd.to_datetime(df['date'])


min=df.groupby('country').min().reset_index().set_index('country')['daily_vaccinations']

NaN=np.where(df.daily_vaccinations.isnull()) 


for i in NaN:
    df.daily_vaccinations[i]=min[df.country[i]] 


NaNForNoValues=np.where(df.daily_vaccinations.isnull())
if(len(NaNForNoValues)):
    for y in NaNForNoValues:
        df.daily_vaccinations[y]=0
