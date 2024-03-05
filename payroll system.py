class Employee:
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name

    def calculate_payroll(self):
        raise NotImplementedError("Subclass must implement abstract method")


class SalaryEmployee(Employee):
    def __init__(self, employee_id, name, weekly_salary):
        super().__init__(employee_id, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary


class HourlyEmployee(Employee):
    def __init__(self, employee_id, name, hours_worked, hourly_rate):
        super().__init__(employee_id, name)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hourly_rate


class CommissionEmployee(SalaryEmployee):
    def __init__(self, employee_id, name, weekly_salary, commission):
        super().__init__(employee_id, name, weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        return super().calculate_payroll() + self.commission


# Example usage:
if __name__ == "__main__":
    salary_employee = SalaryEmployee(1, "abel watoka", 1000)
    print("Salary Employee Payroll:", salary_employee.calculate_payroll())  # Output: 1000

    hourly_employee = HourlyEmployee(2, "hope king", 40, 20)
    print("Hourly Employee Payroll:", hourly_employee.calculate_payroll())  # Output: 800

    commission_employee = CommissionEmployee(3, "hiden tig", 1200, 300)
    print("Commission Employee Payroll:", commission_employee.calculate_payroll())  # Output: 1500
