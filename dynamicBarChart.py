import matplotlib.pyplot as plt

n = int(input("Enter number of categories: "))

Employees = []
Salaries = []

for i in range(n):
    Employee = input(f"Enter name of category {i+1}: ")
    Salary = int(input(f"Enter value for {Employee}: "))
    
    Employees.append(Employee)
    Salaries.append(Salary)

plt.bar(Employee,Salary)

plt.xlabel("Employee")
plt.ylabel("Salary")
plt.title("Dynamic Bar Chart")


plt.show()