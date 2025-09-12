age = [21, 25, 21, 23,22, 20]
age.append(31)

age_1 = [29, 33, 30]
age.extend(age_1)

print(age[0])
print(age[-1])
print(age.index(31))