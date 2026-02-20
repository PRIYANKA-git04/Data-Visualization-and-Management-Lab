import matplotlib.pyplot as plt

n = int(input("Enter number of months: "))

months = []
temperature = []
rainfall = []

for i in range(n):
    month = input("Enter month name: ")
    temp = float(input("Enter temperature: "))
    rain = float(input("Enter rainfall: "))
    
    months.append(month)
    temperature.append(temp)
    rainfall.append(rain)

plt.subplot(1, 2, 1)
plt.plot(months, temperature)
plt.xlabel("Months")
plt.ylabel("Temperature")
plt.title("Monthly Temperature")

plt.subplot(1, 2, 2)
plt.bar(months, rainfall)
plt.xlabel("Months")
plt.ylabel("Rainfall")
plt.title("Monthly Rainfall")

plt.tight_layout()
plt.show()