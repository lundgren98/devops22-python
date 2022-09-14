class Animal:
    def __init__(self, age):
        self.age = age

class Dog(Animal):
    def __init__(self, age, fav_toy):
        super().__init__(age)
        self.fav_toy = fav_toy

class Supermarket:
    def __init__(self, employees, customers, products):
        self.employees = employees
        self.customers = customers
        self.products = products

class Coop(Supermarket):
    def __init__(self, employees, customers, products, members):
        super().__init__(employees, customers, products)
        self.members = members

if __name__ == '__main__':
    dog = Dog(4, 'squeaky')
    coop = Coop(10, 400, 2000, 50)
