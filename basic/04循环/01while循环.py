i = 1
sum = 0

while i <= 100:
    sum += i
    i += 1

print(sum)

import random
num = random.randint(1, 100)
count = 0
flag = True
while flag:
    guess_num = int(input("q请输入你要猜的数字"))
    count += 1
    if guess_num == num:
        print("猜中了")
        flag = False
    else:
        if guess_num > num:
            print("大了")
        else:
            print("小了")

print(f"你总共猜猜{count}次")

