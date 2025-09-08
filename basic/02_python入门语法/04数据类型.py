# 使用print直接输出类型信息
print(type("你好"))
print(type(666))
print(type(13.14))

# 使用变量存储type()语句的结果
string_type = type("你好")
int_type = type(666)
float_type = type(13.14)

print(string_type, int_type, float_type)

# 使用type()语句，查看变量中存储的数据类型信息
name = "泰拉瑞亚"
name_type = type(name)
print(name_type)