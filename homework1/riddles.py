print('Введите первое число: ')
a = float(input())
print('Введите второе число: ')
b = float(input())
print('"+" или "-" ? ')
symbol = raw_input()
if symbol == '-':
    s = a - b
elif symbol == '+':
    s = a + b
print(s)