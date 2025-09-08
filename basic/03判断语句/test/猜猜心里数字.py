num = 1

if int(input("请输入第一次猜想的数字")) == num:
    print("1猜对啦")
elif int(input("不对，再猜一次")) == num:
    print("2猜对啦")
elif int(input("不对，最后次")) == num:
    print("3对啦")
else:
    print(f"全错啦，我想的是{num}")