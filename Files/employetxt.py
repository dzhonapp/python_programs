def employee():
    employee_quantity = int(input("How many employee data you want to create? "))
    file = open("emplyee.txt", 'w')
    for employees in range(1, employee_quantity+1):
        employee_name = input("Employee name? ")
        employee_salary = input("Employee Salary! ")
        file.write(employee_name + "\n")
        file.write(employee_salary + "\n")
    file.close()

employee()

def readFile(filename):
    fileopen = open(filename, 'r')
    a = fileopen.readlines()
    fileopen.close()
    return a

print(readFile("emplyee.txt"))



def appendToFile(filename):
    file = open(filename, 'a')
    employee_quantity = int(input("How many employee data you want to create? "))
    for employees in range(1, employee_quantity+1):
        employee_name = input("Employee name? ")
        employee_salary = input("Employee Salary! ")
        file.write(employee_name + "\n")
        file.write(employee_salary + "\n")
    file.close()

appendToFile("emplyee.txt")
print(readFile("emplyee.txt"))

