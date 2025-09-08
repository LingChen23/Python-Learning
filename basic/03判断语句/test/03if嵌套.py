# if int(input("你的身高是多少")) > 120:
#     print("身高超出限制，但是vip级别大于3可以免费")
#
#     if int(input("你的vip级别是多少")) >= 3:
#         print("恭喜你，可以免费")
#     else:
#         print("不可以免费")
#
# else:
#     print("欢迎小朋友，免费游玩")
print(214.1499/60)
age = int(input("请输入你的年龄"))
if age >= 18:
    print("成年人")
    if age < 30:
        print("年龄达标")
        if int(input("请输入你的入职时间"))>2:
            print("恭喜你获得礼物")
        elif int(input("请输入你的级别")) >3:
            print("级别大于3")
        else:
            print("入职时间和职务不符合")

    else:
        print("年龄大了")

else:
    print("年龄小了")