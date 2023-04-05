import pandas as pd
import csv
import matplotlib.pyplot as plt
import numpy as np

rows = []

with open("main.csv","r") as f:
    df = csv.reader(f)

    for row in df:
        rows.append(row)
    

#print(rows)

headers = rows[0]
print(headers)

pd_rows= rows[1:]
print(pd_rows)

solar_system_planet_count = {}

for i in pd_rows:
    if solar_system_planet_count.get(i[11]):
        solar_system_planet_count[i[11]]+=1
    else:
        solar_system_planet_count[i[11]]=1

max_value = max(solar_system_planet_count,key=solar_system_planet_count.get)
print(max_value)

pl_mass = []
pl_radius = []

for i in pd_rows:
    pl_mass.append(i[3])
    pl_radius.append(i[7])

print(pl_mass)
print(pl_radius)

fig = plt.scatter(x=pl_radius,y=pl_mass)
fig.show()