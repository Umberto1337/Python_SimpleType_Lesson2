# Задание №3
# ✔ Напишите программу, которая получает целое число и возвращает
# его двоичное, восьмеричное строковое представление.
# ✔ Функции bin и oct используйте для проверки своего
# результата, а не для решения.
# Дополнительно:
# ✔ Попробуйте избежать дублирования кода
# в преобразованиях к разным системам счисления
# ✔ Избегайте магических чисел
# ✔ Добавьте аннотацию типов где это возможно

BIN = 2
OCT = 8

num: int = int(input('Введите число: '))

test_num: int = num
result: str = ''
res: str = ''

while test_num:
    cur_num = test_num % BIN
    result = str(cur_num) + result
    test_num //= BIN
    
    cur_num2 = test_num % OCT
    res = str(cur_num2) + res
    test_num //= OCT

print(f'для {BIN} {result=}')
print(f'для {OCT} {res=}')

BIN = 2
OCT = 8

num: int = int(input('Введите число: '))

for div in BIN, OCT:
    test_num: int = num
    result: str = ''
    res: str = ''

    while test_num:
        cur_num = test_num % div
        result = str(cur_num) + result
        test_num //= div
    print(f'для {div} {result=}')
