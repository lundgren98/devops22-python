class Person:
    def __init__(self, street_name, street_number, postal_code, country):
        self.address = (street_name, street_number, postal_code, country)

class Employee:
    def __init__(self, street_name, street_number, postal_code, country,
                 employee_number, salary):
        super().__init__(street_name, street_number, postal_code, country)
        self.number = employee_number
        self.salary = salary
