class Employee:
    raise_amount = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def Fullname(self):
        return '{} {}'.format(self.first, self.last)
    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount) # or self.raise_amaout

emp_1 = Employee('rick', 'dan', 40000)
emp_2 = Employee('anolf', 'swaz', 50000)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

# print(emp_1.pay)
#
# print(emp_1.pay)

# print(emp_1)
# print(emp_2)
#
#
#
# print(emp_1.email)
# print(emp_2.email)
#
# print(emp_1.Fullname())
# # print(emp_2.Fullname())
# emp_2.Fullname()
# print(Employee.Fullname(emp_1)) # this function do the same thing

# print('{} {}'.format(emp_1.first, emp_1.last))

