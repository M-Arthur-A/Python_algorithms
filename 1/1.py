"""
Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
"""
a = input('Введите начальный символ: ')
b = input('Введите конечный символ: ')
print(f'Между {a} и {b} находится {ord(b) - ord(a)} знака(ов)')
