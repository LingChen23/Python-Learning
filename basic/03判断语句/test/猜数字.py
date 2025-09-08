# 构建随机数字变量
import random
num = random.randint(1, 10)

guess_num = int(input("请输入你要猜测的数字"))
if guess_num == num:
    print("1正确")
else:
    if guess_num > num:
        print("大了")
    elif guess_num < num:
        print("小了")

    guess_num = int(input("请再次输入你要猜测的数字"))
    if guess_num == num:
        print("2正确")
    else:
        if guess_num > num:
            print("大了")
        elif guess_num < num:
            print("小了")

        guess_num = int(input("请最后输入你要猜测的数字"))

        if guess_num == num:
            print("3正确")
        else:
            print(f"错了，数字是{num}")