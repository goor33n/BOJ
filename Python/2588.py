a = input()
b = input()

#print(int(a) * int(b[2]))
#print(int(a) * int(b[1]))
#print(int(a) * int(b[0]))
#print(int(a) * int(b))

for i in reversed(b):
    print(int(a) * int(i))
print(int(a) * int(b))
