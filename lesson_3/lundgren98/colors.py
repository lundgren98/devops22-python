

colors = []
red = "red"
colors.append(red)
print(colors[0])
colors.extend(["green", "blue"])
print("red" in colors)
print("black" not in colors)
colors2 = ["cyan", "magenta", "yellow"]
print(colors + colors2)
colors3 = ["red", "yellow"]
colors3 *= 3
print(colors3)
print(colors3[:4])
print(colors3.count("red"))
print(colors3.index("yellow"))
print(len(colors))
print(len(colors2))
print(len(colors3))
numbers = [5, 12, 23, -3, 27, 33, 22]
print(min(numbers))
print(max(numbers))
