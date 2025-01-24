import math
### part one
r = 5
a = math.pi * 5 ** 2
v = (4 / 3) * math.pi * r ** 3
a_side = 3
b_side = 4
pyt = math.sqrt(a_side ** 2 + b_side ** 2)
first = "Kennedy"
last = "Capote"
full_name = (first + " " + last)
name_len = len(full_name)
print(a, v, pyt, name_len, full_name, full_name.upper(), full_name.lower())

age = 24
height_ft = 5.25
height_in = 63
weight = 109
bmi = weight / height_in ** 2 * 703
print(type(age), type(height_ft), type(height_in), type(weight))
print(bmi)