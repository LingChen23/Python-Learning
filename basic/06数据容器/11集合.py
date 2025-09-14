my_set = {123, "黑马", "黑马", "xiaogou"}
print(my_set)
my_set_empty = set()
print(my_set_empty)

my_set.add("你好")
print(my_set)

my_set.remove("你好")
print(my_set)

ele = my_set.pop()
print(ele)
print(my_set)

my_set.clear()
print(my_set)

set1 = {1, 2, 3}
set2 = {1, 2, 4}
set3 = set1.difference(set2)
print(set1)
print(set2)
print(set3)

# set1.difference_update(set2)
print(set1)
print(set2)

set3 = set1.union(set2)
print(set3)

set1 = {1, 2, 4, 6, 1, 3, 4}
print(len(set1))

for i in set1:
    print(i)

my_list = ["黑马","传智播客","黑马","传智播客","itheima","itcast","itheima","itcast","best"]
my_set = set()
for i in my_list:
    my_set.add(i)
print(my_list)
print(my_set)