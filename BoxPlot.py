import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('final_30x10_dataset.csv')

age = df['Age'].dropna().tolist()

plt.boxplot(age)
plt.xlabel('Age')
plt.title('Box plot of Age')
plt.show()
