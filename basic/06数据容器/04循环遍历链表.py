def list_while_func():
    my_list = ["itheia", "itcast", "python"]
    index = 0
    while index < len(my_list):
        print(my_list[index])
        index += 1


def list_for_func():
    my_list = ["itheia12345", "itcast", "python"]
    for element in my_list:
        print(element)

list_for_func()
list_while_func()