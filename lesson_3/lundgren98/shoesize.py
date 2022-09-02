names = []
ages  = []
sizes = []
res = input("Please enter name for person 1 ")
names.append(res.title())
res = input("Please enter age for person 1 ")
ages.append(int(res))
res = input("Please enter shoe size for person 1 ")
sizes.append(int(res))
res = input("Please enter name for person 2 ")
names.append(res.title())
res = input("Please enter age for person 2 ")
ages.append(int(res))
res = input("Please enter shoe size for person 2 ")
sizes.append(int(res))
res = input("Please enter name for person 3 ")
names.append(res.title())
res = input("Please enter age for person 3 ")
ages.append(int(res))
res = input("Please enter shoe size for person 3 ")
sizes.append(int(res))

age_to_name = {
        str(ages[0]): names[0],
        str(ages[1]): names[1],
        str(ages[2]): names[2]
        }
age_to_size = {
        str(ages[0]): str(sizes[0]),
        str(ages[1]): str(sizes[1]),
        str(ages[2]): str(sizes[2])
        }
name_to_size = {
        names[0]: str(sizes[0]),
        names[1]: str(sizes[1]),
        names[2]: str(sizes[2])
        }
eldest_age = str(sorted(ages)[-1])
eldest_name = age_to_name[eldest_age]
eldest_size = age_to_size[eldest_age]

size_to_age = {v: k for k, v in age_to_size.items()}
biggest_size = str(sorted(sizes)[1])
biggest_age = size_to_age[biggest_size]
biggest_name = age_to_name[biggest_age]

name_to_age = {v: k for k, v in age_to_name.items()}
size_to_name = {v: k for k, v in age_to_name.items()}

commands = {
        "name": [name_to_age, name_to_size],
        "age": [age_to_name, age_to_size],
        "size": [size_to_age, size_to_name]
        }

present_order = {
        "name": ["age", "size"],
        "age": ["name", "size"],
        "size": ["age", "name"]
        }

print(f'The oldest person is {eldest_name} who has shoe size {eldest_size}')
print(f'The person with median shoe size is {biggest_name} who is {biggest_age} years old')
res = input('Please enter search value, name, age or size followed by value: ')
the_input = res.split()
my_key = the_input[0]
my_value = the_input[1]

print('Found Person')
print(f'{my_key}: {my_value}')
print(f'{present_order[my_key][0]}: {commands[my_key][0][my_value]}')
print(f'{present_order[my_key][1]}: {commands[my_key][1][my_value]}')
