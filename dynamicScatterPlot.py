import matplotlib.pyplot as plt

n = int(input("Enter number of employees: "))

experience = []
salary = []

for i in range(n):
    exp = float(input("Enter years of experience: "))
    sal = float(input("Enter salary: "))
    experience.append(exp)
    salary.append(sal)

plt.scatter(experience, salary)

plt.xlabel("Experience (Years)")
plt.ylabel("Salary")
plt.title("Dynamic Scatter Plot")

plt.grid(True)
plt.show()