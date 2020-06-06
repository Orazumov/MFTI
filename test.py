from functools import reduce
from sys import getsizeof

variables = []     # массив для оценки памяти

n = int(input('Введите количество элементов ряда чисел: '))

lst = [1]
number = 1

for i in range(1, n + 1):

    number = number / 2

    if i % 2 == 0:
        lst.append(number)
    else:
        lst.append(-number)

answer = reduce(lambda x, y: x+y, lst)
print(f'Ответ вариант 3: {answer}')

def show_lst_float_int(object, mem_size = 0):

    if isinstance(object, int) or isinstance(object, float):
        return getsizeof(object)

    mem_size += getsizeof(object)

    if isinstance(object, list):
        for item in object:
            mem_size += getsizeof(item)
        return mem_size

def append_to_lst(*args):
    variables = []
    for item in args:
        variables.append(item)
    return variables

variables = append_to_lst(lst, answer, i, n, number)

memory_size = int()
for i in variables:
    memory_size += show_lst_float_int(i)
print(f'Вариант 3 занял в памяти: {memory_size} байт.')