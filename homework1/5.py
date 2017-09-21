print('Введите первое число: ')
a = int(input())
print('Введите второе число: ')
b = int(input())
i = a
for i in range (a,b):
    if i%5 == 0:
        print(i)
        i += 1