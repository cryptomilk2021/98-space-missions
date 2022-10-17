import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from misc import scrub_it
import csv

df = scrub_it()

for i in range(len(df['Date'])):
    a_string = df['Date'][i]
    df['Date'][i] = a_string[12:16]

a = df['Origin'].value_counts()

new_frame = a.to_frame()
list5countries = new_frame.index.tolist()
list5countries = list5countries[0:5]

df = df[df.Origin.isin(list5countries)]

del df['Location']
del df['Detail']
del df['Unnamed: 0.1']
del df['Unnamed: 0']
del df['Price']
del df['Rocket_Status']
del df['Organisation']
del df['Mission_Status']

list1 = df.values.tolist()

df2 = df.groupby(['Date', 'Origin'])['Date'].count()    #aggregates well

df2 = df2.to_frame()

df2.to_csv('df4.csv')
with open('df4.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

list_years = [i[0] for i in data]
list_countries = [i[1] for i in data]
list_nbr = [i[2] for i in data]
list_years.pop(0)
list_countries.pop(0)
list_nbr.pop(0)
list_years = [int(x) for x in list_years]
list_nbr = [int(x) for x in list_nbr]

df = pd.DataFrame({
    'Years': list_years,
    'Country': list_countries,
    'Launches': list_nbr,
})

piv_df = df.pivot(index='Years',columns='Country',values='Launches')

piv_df.plot.bar()

plt.show()
