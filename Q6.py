import pandas as pd

excel_file= "./country_vaccination_stats.csv"
df=pd.read_csv(excel_file)
df.fillna(value=0,inplace=True)

print(df[df['date']=='1/6/2021']['daily_vaccinations'].sum())