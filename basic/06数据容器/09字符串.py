my_str = "itheima  ang ni"
v1 = my_str[1]
v2 = my_str[2]
print(v1, v2)
# index 方法
print(my_str.index("ang"))
# 字符串的替换 replace
v3 = my_str.replace("ang","i")
print(v3)
# split方法：按照指定的分隔符字符串，将字符串划分为多个字符串，并存入列表对象中
my_split = my_str.split(" ")
print(my_split)
# strip()：去前后空格以及回车符
# strip(字符串)：去前后指定字符串,分割成一小块内容
my_str = "it he aesf iu"
my_strip = my_str.strip("iu")
print(my_strip)
# count
print(my_str.count("it"))
# len
print(len(my_str))

my_str = "黑马程序员"
index = 0
while index < len(my_str):
    print(my_str[index])
    index += 1

for i in my_str:
    print(i)

str = "itheima itcast boxuegu"
print(str.count("it"))
str1 = str.replace(" ","|")
print(str1)
str2 = str1.split("|")
print(str2)