def check_age(age):
    if age > 18:
        return "success"
    else:
        return None

result = check_age(17)
if not result:
    print("未成年，不可以进入")

name = None