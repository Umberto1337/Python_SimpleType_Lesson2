'''Строки и способы их записи'''
# txt = 'Книга называется "Война и мир".'

# class str(object):
#     '''
#     str(object='') -> str
#     str(bytes_or_buffer[, encoding[, errors]]) -> str
#     ...
#     '''
    
'''Конкатинация строк'''
# LIMIT = 120
# ATTENTION = 'Внимание!'
# name = input('Твоё имя? ')
# age = int(input('Твой возраст? '))
# text = ATTENTION + 'Хоть тебе и осталось ' + str(100 - age) +\
#     " до ста лет, но длинна строки не должна превышать " + str(LIMIT) + ' символов.'
# print(text)

'''Размер строки в памяти методом object.__sizeoff__() - размер объекта в байтах''',
# empty_str = ''
# en_str = 'Text'
# ru_str = 'Текст'
# unicode_str = '😂🙈🤗😋'
# print(empty_str.__sizeof__())
# print(en_str.__sizeof__())
# print(ru_str.__sizeof__())
# print(unicode_str.__sizeof__())