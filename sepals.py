import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
iris_df=pd.read_csv("Iris.csv")
print(iris_df.head())
sns.scatterplot(data=iris_df,x='SepalLengthCm',y='SepalWidthCm',hue="Species")
plt.show()
