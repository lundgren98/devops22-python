

cars = [
        "volvo",
        "saab",
        "bmw",
        "ford",
        "toyota",
        "tesla",
        "opel",
        "skoda",
        "lada",
        "mitsubihsi"
        ]

print(cars)
# 1
print(sorted(cars))
# 2
cars.sort()
print(cars)
# 3
print(sorted(cars, reverse=True))
cars.sort(reverse=True)
print(cars)

# 4
cars = [
        ("volvo", "xc90"),
        ("saab", "9000"),
        ("bmw", "z3"),
        ("ford", "focus"),
        ("toyota", "prius"),
        ("tesla", "x"),
        ("opel", "combo"),
        ("skoda", "octavia"),
        ("lada", "samara"),
        ("mitsubihsi", "500")
        ]
print(sorted(cars, key=lambda x : x[0]))
print(sorted(cars, key=lambda x : x[1]))
