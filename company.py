from employee import Employee, SalaryEmployee, HourlyEmployee, CommisionEmployee

class Company:
    def __init__(self):
        self.employees = []
    
    def add_employee(self, new_employee):
        self.employees.append(new_employee)
    
    def display_employees(self):
        print("The current employees of our company are:")
        for i in self.employees:
            print(i.fname, i.lname)
        print("----------------------------------------")    

    def employee_paycheck(self):
        print("The weekly paycheck for our employees is:")
        for i in self.employees:
            print("The paycheck for", i.fname, i.lname, "is:")
            print(f'${i.calculate_paycheck():,.2f}')
            print("------------------------------------------")

def main():
    my_company = Company()

    employee1 = SalaryEmployee("John", "Watson", 40000)
    employee2 = HourlyEmployee("Sherlock", "Holmes", 40, 100)
    employee3 = CommisionEmployee("James", "Moriarty", 1, 6000, 10)

    my_company.add_employee(employee1)
    my_company.add_employee(employee2)
    my_company.add_employee(employee3)

    my_company.display_employees()
    my_company.employee_paycheck()

main()