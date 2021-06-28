import pandas as pd
import matplotlib.pyplot as plt

#create a data frame using thr json file
datafile = pd.read_json(r'./rain.json')
print(datafile)

print("datafile stats",datafile.describe())

datafile.plot(x="Month",y="Temperature")
datafile.plot(x="Month",y="Rainfall")
plt.show()