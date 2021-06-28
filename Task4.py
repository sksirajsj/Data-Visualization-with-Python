import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv(r'birthYearly.csv')
print(df)

#converting the data into matrix format so that heatmap could read the data

dataP = df.pivot("month","year",'births')
print(dataP)
#annot=true,so that we can see datafeilds in matrix
#fmt is format of data shown,d for decimal
sns.heatmap(dataP,annot=True,fmt="d")
plt.show()