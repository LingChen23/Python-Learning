t1 = (1, "hello", True)
t2 = ()
t3 = tuple()

t4 = ("hello", )
t5 = ((1, 2, 3), (4, 5, 6))
num = t5[1][2]
print(num)

print(t1.index(1))
print(t1.count("hello"))
print(t1.count(1))
print(len(t1))

index = 0
while index < len(t1):
    print(t1[index])
    index += 1

for element in t1:
    print(element)

t9 = (1, 2, [1,2,3])
t9[2][1]=999
print(t9)