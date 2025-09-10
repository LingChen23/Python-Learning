for i in range(1, 6):
    print("语句1")

    for j in range(5):
        print("<UNK>2")
        continue
        print("<UNK>3")

    print("Yuju4")

for i in range(100):
    print("语句1")
    break
    print("语句2")

print("语句3")

for i in range(6):
    print("语句1")

    for j in range(5):
        print("语句2")
        break
        print("<UNK>3")

    print("Yuju4")