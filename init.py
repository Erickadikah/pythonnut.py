class Employee:
    def __init__(self,first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
       return '{} {}'.format(self.first, self.last)

em_1 = Employee('erick', 'adikah', 5000)
em_2 = Employee('joshua', 'muuo', 7000)
print(em_1.pay)
print(em_1.email)
print(em_2.email)
print()
print(em_1.fullname())