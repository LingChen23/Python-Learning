my_list = ["itheia", "itcast", "python"]
print(f"索引{my_list.index("itheia")}")

my_list[1] = "heool"
print(my_list)

my_list.insert(1, "python")
print(my_list)

my_list.append("123")
print(my_list)

my_list2 = [123, 456, 789]
my_list2.extend(my_list)
print(my_list2)

my_list = ["itheia", "itcast", "python"]
del my_list[2]
print(my_list)

lelment = my_list.pop(0)
print(my_list)
print(lelment)

my_list = ["itheia", "itcast", "python","itheia", "itcast", "python"]
my_list.remove("python")
print(my_list)

my_list.clear()
print(my_list)

my_list = ["itheia", "itcast", "python","itheia", "itcast", "python"]
print(my_list.count("python"))

length = len(my_list)
print(length)