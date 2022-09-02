people = [
        {
            "name": input("Please enter name for person 1: "),
            "age": input("Please enter age for person 1: "),
            "size": input("Please enter shoe size for person 1: "),
        },
        {
            "name": input("Please enter name for person 2: "),
            "age": input("Please enter age for person 2: "),
            "size": input("Please enter shoe size for person 2: "),
        },
        {
            "name": input("Please enter name for person 3: "),
            "age": input("Please enter age for person 3: "),
            "size": input("Please enter shoe size for person 3: "),
        }
        ]

# Find the oldest person
eldest = sorted(people, key=lambda person : person["age"])[-1]
# Find the median shoe sized person
median_size = sorted(people, key=lambda person : person["size"])[1]

print(f'The oldest person is {eldest["name"]} who has shoe size {eldest["size"]}')
print(f'The person with median shoe size is {median_size["name"]} who is {eldest["age"]} years old')
res = input('Please enter search value, name, age or size followed by value: ')
com, val = res.split()

# Case insensitive
com = com.lower()
val = val.title()

searched = sorted(people, key=lambda person : person[com] == val)[-1]
print(f'Found person\n\tName: {searched["name"]}\n\tAge: {searched["age"]}\n\tSize: {searched["size"]}')
