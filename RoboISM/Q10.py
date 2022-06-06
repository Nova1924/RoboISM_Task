a = int(input("value of a"))
b = int(input("value of b"))

print('a : ', a)
print('b : ', b)

a ^= b
b ^= a
a ^= b

print('a : ', a)
print('b : ', b)