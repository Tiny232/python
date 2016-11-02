class Employee:
    num_of_emps = 0
    raise_amt = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        Employee.num_of_emps += 1
    @property
    def email(self):
        return '{}.{}@company.com'.format(self.first, self.last)
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    def __repr__(self):
        return '{} {} {}'.format(self.first, self.last, self.email)
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount
class Developers(Employee):
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang
    def full(self):
        return '{} {} {} {} {}'.format(self.first, self.last, self.email, self.pay, self.prog_lang)
emp_1 = Employee('corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)
emp_3 = Employee('murtaz', 'murtaziani', 9999999)
dev_1 = Developers('dev1', 'dev11', 8764389, 'Python')
print (emp_1.email)