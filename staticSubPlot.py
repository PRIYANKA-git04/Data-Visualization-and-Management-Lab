import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr"]
sales = [100, 150, 200, 180]
expenses = [80, 120, 160, 140]

plt.subplot(1, 2, 1)
plt.plot(months, sales)
plt.title("Monthly Sales")

plt.subplot(1, 2, 2)
plt.bar(months, expenses)
plt.title("Monthly Expenses")

plt.tight_layout()  
plt.show()