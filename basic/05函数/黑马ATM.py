money = 5000000
name = None

def query():
    print(f"{name}余额{money}")
    return money

def saving(num):
    global money
    money += num
    print(f"存款成功")
    query()

def get_money(num):
    global money
    money -= num
    query()
        

