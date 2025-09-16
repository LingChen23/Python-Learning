my_dict = {"小红": 99, "小明": 12, "林俊杰": 77}
my_dict["张学良"] = 100
print(my_dict)

my_dict["小红"] = 109
print(my_dict)

score = my_dict.pop("小红")
print(my_dict)

# 清空元素
# print(my_dict.clear())
key = my_dict.keys()
print(key)

# 遍历字典 获取全部key
for i in key:
    print(my_dict[i])

for key in my_dict:
    print(my_dict[key])

# y元素数量
print(len(my_dict))
