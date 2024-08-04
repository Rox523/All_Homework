#first, ssecond,third
first = 1
second = 3
third = 5
a = int(input('Введите первое число'))
b = int(input('Введите второе число '))
c = int(input('Введите третье число '))
if a % 3 == 0 and  a % 4 == 0 and  a % 6 == 0:
    print(3)
elif b % 3 == 0 or b % 4== 0 or b % 6 == 0:
    print(2)
elif c % 3 == 0 or b % 4== 0 or b % 6 == 0:
    print(0)

