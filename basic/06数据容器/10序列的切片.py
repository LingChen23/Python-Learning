my_list = [0, 1, 2, 3, 4, 5]
result1 = my_list[1:4]
print(result1)

my_tuple = (0, 1, 2, 3, 4, 5)
result2 = my_tuple[:]
print(result2)

str = "012345678"
result3 = str[::2]
print(result3)

result4 = str[::-2]
print(result4)
result5 = my_list[3:1:-1]
print(result5)

result6 = my_tuple[::-2]
print(result6)

test = "万过薪月，元序程马黑来，nohtyp学"

t1 = test[::-1].split("，")[1].strip("来")
print(t1)