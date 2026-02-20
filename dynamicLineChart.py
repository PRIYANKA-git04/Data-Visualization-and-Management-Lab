import matplotlib.pyplot as plt

x = []
y = []

plt.xlabel("X-axis")
plt.ylabel("Y-axis")

n = int(input("Enter number of points"))

for i in range(n):
    val1 = int(input("Enter x cordinate"))
    val2 = int(input("Enter y cordinate"))

    x.append(val1)
    y.append(val2)

    plt.plot(x, y)

plt.show()
