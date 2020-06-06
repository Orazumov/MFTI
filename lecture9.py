# рекурентные сортировки: Тони Хоара и сортировка слиянием.

# сортировка слиянием.

# слияние отсортированных массивов.

def merge(A:list, B:list):
    C = [0]*(len(A) + len(B)) # зарезервировали нужное количество памяти под фин. массив.
    i = k = n = 0
    while i < len(A) and k < len(B):
        if A[i] <= B[k]:
            C[n] = A[i]; i += 1; n += 1 # мы берем из А, чтобы сорт была устойчивой, т.е. чтобы не менять порядок равных элементов.
        else:
            C[n] = B[k]; k += 1; n += 1
    while i < len(A):   # заливаем оставшиеся элементы, если B закончился.
        C[n] = A[i]; i += 1; n += 1
    while k < len(B):  # заливаем оставшиеся элементы, если А закончился.
        C[n] = B[k]; k += 1; n += 1
    return C

# тут мы передали 2 массива в ф., а можно сделать так, чтобы в ф. отдавался 1 массив, 2 части которого отсортированы.
# при этом будут указатели middle, а также left и right - начало и конец массивов.

# Рекурентная ф. для сортировки слиянием:

def merge_sort(A):
    if len(A) <= 1:
        return
    middle = len(A)//2
    L = [A[i] for i in range(0, middle)]
    R = [A[i] for i in range(middle, len(A))]
    merge_sort(L)
    merge_sort(R)
    C = merge(L, R)
    for i in range(len(A)): # перелили в А. Можно сделать срезами.
        A[i] = C[i] # просто А=С нельзя, т.к. просто поменяем ссылку.
    return A

print(merge_sort([5,4,12,6,7,8,0,0,1,5,7]))

# сотировка Тони Хоара.

# барьерный элемент == A[0]

def hoar_sort(A):
    if len(A) <= 1:
        return # None
    L = []; R = []; M = []
    barrier = A[0]
    for x in A:
        if x < barrier:
            L.append(x)
        elif x == barrier:
            M.append(x)
        else:
            R.append(x)
    hoar_sort(L)
    hoar_sort(R)
    k = 0
    for x in L+M+R: #! склеили массив!
        A[k] = x
        k += 1

# проверка упорядоченности массива за O(n):

def check_sorted(A, ascending=True):
    '''проверка отсортированности за О(длинны А)'''

    flag = True
    s = 2*int(ascending)-1

# int(True) = 1, int(False) = 0, нам нужно чтобы: в случае True => +1, в случае False => -1.
# поэтому вводим функцию s. Все это нужно для поворота знака < > чтобы проверять массив как на
# возростание, так и на убывание.

    for i in range(0, N-1):
        if s*A[i] > s*A[i+1]:
            flag = False
            break
    return flag

