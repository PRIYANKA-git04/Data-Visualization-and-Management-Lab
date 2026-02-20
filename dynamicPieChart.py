import matplotlib.pyplot as plt

n = int(input("Enter number of persons: "))

Name = []
Age = []

for i in range(n):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    Name.append(name)
    Age.append(age)

plt.pie(Age, labels=Name, autopct='%1.1f%%')
plt.title("Dynamic Pie Chart")
plt.show()