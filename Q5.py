import pandas as pd

excel_file= "./country_vaccination_stats.csv"
df=pd.read_csv(excel_file)
df.fillna(value=0,inplace=True)
print(df.info())

country_median = df.groupby('country').median()
top_3_country = country_median.sort_values('daily_vaccinations', ascending=False).iloc[:3]
country_names = top_3_country.index
country_names = list(country_names)
print(top_3_country)
print(country_names)