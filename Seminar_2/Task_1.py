# import sys

# data = [42, 73.0, 'Hello World', True, 42, 'Hello World!', 256, 2 ** 8, 1, 'Привет, мир!']
# for n, item in enumerate(data, 1):
#     # print(n, item)
#     check_int = 'Число явялется целым' if isinstance(item, int) else ''
#     check_str = 'Это строка' if isinstance(item, str) else ''
#     check_float = 'Это вещественное число' if isinstance(item, float) else ''
#     print(f'{n}. Объект {item}\nАдрес: {id(item)}\tРазмер: {sys.getsizeof(item)}\t'
#           f'Хэш: {hash(item)} {check_int}{check_str}{check_float}')
    