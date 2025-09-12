def add(x, y):
    result = x + y
    print(f"x + y = {result}")

add(2,1222)

def check(tem):
    if tem > 37.5:
        print("体温过高")
    elif tem < 36:
        print("体温过低")
    else:
        print("<UNK>")

check(12)
check(123)
check(37)