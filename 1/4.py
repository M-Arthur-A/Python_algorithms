"""
Определить, является ли год, который ввел пользователь, високосным или не високосным.
"""
a = int(input('Введите год: '))
is_leap = False
if a % 4 == 0:
    if a % 100 == 0:
        if a % 400 == 0:
            is_leap = True
    else:
        is_leap = True
if is_leap:
    print(f'{a} -- високосный')
else:
    print(f'{a} не високосный')
