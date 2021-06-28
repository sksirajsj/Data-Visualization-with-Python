import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


dataframe = pd.read_json(r'./rain.json')

plt.figure(figsize= (20,5))
plt.plot(dataframe['Month'],dataframe['Rainfall'],label = 'Rainfall')
plt.legend()
plt.show()


#We create a plot with both temaparature and rainfall on Y axis Together
plt.figure(figsize= (20,5))
#figsize sets the widht and height of plot
plt.plot(dataframe['Month'],dataframe['Temperature'],label = 'Temperature')
plt.plot(dataframe['Month'],dataframe['Rainfall'],label = 'Rainfall')
plt.legend()
#legend function is used for different colours for different Y axis members
plt.show()


