import pandas as pd
import matplotlib.pyplot as plt


df_small = pd.read_csv("final_30x10_dataset.csv")


df_sorted = df_small.sort_values(by='Age')


plt.plot(df_sorted['Age'], df_sorted['Fare'])


plt.xlabel("Age")
plt.ylabel("Fare")
plt.title("Age vs Fare Distribution")


plt.grid(True)


plt.show()
