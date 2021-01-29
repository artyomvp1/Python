import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('countries.csv')
print(df.head(1))

us = df[df.country == 'United States']
ch = df[df.country == 'China']
af = df[df.country == 'Afghanistan']
fr = df[df.country == 'France']

plt.figure(figsize=(11, 5))
plt.plot(us.year, us.population / us.population.iloc[0] * 100)
plt.plot(ch.year, ch.population / ch.population.iloc[0] * 100)
plt.plot(af.year, af.population / af.population.iloc[0] * 100)
plt.plot(fr.year, fr.population / fr.population.iloc[0] * 100)

plt.title('Population Growth')
plt.xlabel('Year')
plt.ylabel('Population %')
plt.legend(['United States', 'China', 'Afghanistan', 'France'])
plt.yticks(np.arange(0, 500, 50))

df.to_excel('output.xlsx', merge_cells=False)

plt.show()
