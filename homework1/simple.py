n = input("n: ")
lst = []
for i in xrange(2, n+1):
    for j in xrange(2, i):
        if i % j == 0:        
            break
    else:
        lst.append(i)
print lst
