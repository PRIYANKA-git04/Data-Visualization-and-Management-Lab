import matplotlib.pyplot as plt

# Salary data
salaries = [10000, 15000, 15000, 20000, 25000, 25000, 25000, 30000, 30000, 40000]

# Draw histogram
plt.hist(salaries)

# Labels and title
plt.xlabel("Salary Range")
plt.ylabel("Number Of Employees")
plt.title("Salary Distribution")

# Show plot
plt.show()