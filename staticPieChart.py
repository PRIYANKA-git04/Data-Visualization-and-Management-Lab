import matplotlib.pyplot as plt

Name = ['A', 'B', 'C', 'D']
Age = [20, 30, 25, 25]

plt.pie(Age, labels=Name, autopct='%1.1f%%')

plt.title("Static Pie Chart")
plt.show()