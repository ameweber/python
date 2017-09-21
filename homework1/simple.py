a = input("a: ")
b = range(a+1)
b[1] = 0
lst = []

i = 2
while i <= a:
    if b[i] != 0:
        lst.append(b[i])
        for j in xrange(i, a+1, i):
            b[j] = 0
    i += 1
print lst
