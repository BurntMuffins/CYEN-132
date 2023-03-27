# List comprehension
cubes = []

for i in range(10):
    cubes.append(i * i * i)

print(cubes)

newCubes = [i * i * i for i in range(10) if i > 3]
# [value to append: from the loop]
print(newCubes)


doubleListSum = [x + y for x in [1, 2, 3] for y in [5, 6, 7]]
print(doubleListSum)

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)

# Dictionaries 
office = {
    "Zak": 160,
    "Jim": 144,
    "Pual": 132
}

office["Ryan"] = 212 # Add new things

office["Zak"] = 123 # Change a value

for key in office.keys():
    print(key, '->', office[key])
print()
for key,value in office.items():
    print(key, '->', value)

# Dictionary comprehension
dictCubes = {i:i*i*i for i in range(10)}
print(dictCubes)