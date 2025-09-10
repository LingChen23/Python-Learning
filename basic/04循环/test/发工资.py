import random

balance = 10000
salary = 1000
for i in range(1, 21):
    import random
    num = random.randint(1, 10)

    if num < 5:
        print(f"员工{i}，绩效分{num}，低于5，不发工资，下一位")
        continue
    if balance >= 1000:
        balance = balance - salary
        print(f"员工{i}发放工资{salary}元，账户余额还剩{balance}元")
    else:
        print(f"工资发完了，下个月领取把")
        break