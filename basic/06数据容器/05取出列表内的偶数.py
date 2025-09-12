num = [1, 2, 3, 4,5 ,6, 7, 8, 9, 10]

def for_list():
    even = []
    for element in num:
        if element % 2== 0:
            even.append(element)

    print(even)


def while_list():
    even = []
    index = 0
    while index < len(num):
        if num[index] % 2 == 0:
            even.append(num[index])
        index += 1

    print(even)

for_list()
while_list()

