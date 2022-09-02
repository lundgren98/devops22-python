
X = 1 
Y = 4 
addresses = {"Adam": "Ormvägen 5", 
        "Bella": "Klockgatan 1", 
        "Cornelia": "Vikingagatan 3"} 
cars = ["Volvo", "Opel", "BMW"] 
numbers1 = {1, 2, 3, X, 6} 
numbers2 = {Y, 2, 3, 4, 7} 

def q1():
    print(type(X)) # int
    print(type(Y)) # int

def q2():
    print(type(addresses)) # dict

def q3():
    print(addresses["Bella"])

def q4():
    # Vi lägger till ett nytt key:value par i addresses 
    addresses["Daniel"] = "Prinsgränd 2"
    print(addresses["Daniel"])

def q5():
    l = len(addresses)
    print(l)
    # 5.1
    name = sorted(addresses)[-1]
    print(addresses[name])
    # 5.2
    addresses_reversed = { v: k for k, v in addresses.items() }
    address = sorted(addresses_reversed)[0]
    print(addresses_reversed[address])

def q6():
    print(type(cars)) # list

def q7():
    print(cars[X])

def q8():
    print(cars[Y])

def q9():
    cars.sort()
    print(cars[0]) # BMW

def q10():
    cars_2 = cars
    cars_3 = []
    cars_3.extend(cars)
    cars.append("Saab")
    
    print(cars)
    print(cars_2)
    print(cars_3)
    cars.extend(cars)
    cars.sort(reverse=True)
    print(cars)
    unique_cars = list(set(cars))
    print(unique_cars)

def q11():
    print(type(numbers1)) # set
    print(type(numbers2)) # set

def q12():
    print((numbers1)) # set
    print((numbers2)) # set

def q13():
    print(numbers1.intersection(numbers2))

def q14():
    print(numbers1.union(numbers2))

def q15():
    print(numbers1.symmetric_difference(numbers2))

if __name__ == "__main__":
    print("Q1")
    q1()
    print("Q2")
    q2()
    print("Q3")
    q3()
    print("Q4")
    q4()
    print("Q5")
    q5()
    print("Q6")
    q6()
    print("Q7")
    q7()
    #print("Q8")
    #q8()
    print("Q9")
    q9()
    print("Q10")
    q10()
    print("Q11")
    q11()
    print("Q12")
    q12()
    print("Q13")
    q13()
    print("Q14")
    q14()
    print("Q15")
    q15()
