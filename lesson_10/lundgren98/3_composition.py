class Address:
    def __init__(self, street_name, street_number, postal_code, country):
        self.street_name = street_name
        self.street_number = street_number
        self.postal_code = postal_code
        self.country = country

class Employee:
    def __init__(self, address, number, salary):
        self.address = address
        self.number = number
        self.salary = salary

def main():
    addr = Address('Roadstreet','1','12345','the Republic')
    john_smith = Employee(addr, 42, 20000)

if __name__ == '__main__':
    main()
