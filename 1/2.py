"""
Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
"""
a = input('Введите символ: ')
print(f'{a} это {ord(a) - 96} символ алфавита')
