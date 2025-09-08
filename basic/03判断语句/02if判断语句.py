# age = int(input("请输入你的年龄"))
#
# if age >= 18:
#     print("您已成年，需要买票")
# else:
#     print("未成年")
# print("欢迎今日")

# height = int(input("请输入你的身高"))
# vip_level = int(input("vip等级"))
# day = int(input("今天几号"))

if int(input("请输入你的身高")) < 120:
    print("您的身高小于120，免费")
elif int(input("vip等级")) >= 3:
    print("vip级别大于3，免费")
elif int(input("今天几号")) == 1:
    print("1号免费")
else:
    print("购票")
print("祝您游玩愉快")

