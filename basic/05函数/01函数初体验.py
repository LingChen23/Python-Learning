str1 = "ithe"
str2 = "wrefd"
str3 = "asdfghjk"

count = 0
for i in str1:
    count += 1

print(count)

def my_len(data):
    count = 0
    for i in data:
        count += 1
    print(f"{data}长度时{count}<UNK>")

my_len(str1)
my_len(str2)
my_len(str3)

