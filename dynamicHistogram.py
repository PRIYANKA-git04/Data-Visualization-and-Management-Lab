import matplotlib.pyplot as plt

n = int(input("Enter number of employees: "))

salaries = []

for i in range(n):
    salary = float(input("Enter salary: "))
    salaries.append(salary)

plt.hist(salaries)

plt.xlabel("Salary Range")
plt.ylabel("Number Of Employees")
plt.title("Salary Distribution")

plt.show()