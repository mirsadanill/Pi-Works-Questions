import pandas as pd
import numpy as np
df = pd.read_csv("./country_vaccination_stats.csv")


min=df.groupby('country')['daily_vaccinations'].min()

NaN=np.where(df.daily_vaccinations.isnull()) 

for i in NaN:
    df["daily_vaccinations"][i]=min[df['country'][i]] 

NaNForNoValues=np.where(df.daily_vaccinations.isnull())

if(len(NaNForNoValues)):
    for i in NaNForNoValues:
        df.daily_vaccinations[i]=0

country_median = df.groupby('country').median()
top_3_country = country_median.sort_values('daily_vaccinations', ascending=False).iloc[:3]
country_names = top_3_country.index
country_names = list(country_names)
print(top_3_country)
print(country_names)
