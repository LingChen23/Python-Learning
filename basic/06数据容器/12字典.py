# 定义字典
my_dict = {"小红": 99, "小明": 12, "林俊杰": 77}
my_dict1 = {}
my_dict2 = dict()

# 从字典中基于Key获取元素
score = my_dict["小红"]
print(score)

# 嵌套
stu_score_dict = {
    "小红":{
        "语文": 99,
        "数学": 12,
        "英语": 77
    },
    "周杰伦":{
        "语文": 99,
        "数学": 112,
        "英语": 77},
    "林俊杰":{
        "语文": 99,
        "数学": 12,
        "英语": 97
    }
}
print(stu_score_dict)
print(stu_score_dict["周杰伦"]["语文"])