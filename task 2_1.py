# Задача 2.1. 

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# функции max и min использовать нельзя!


list = [8, 5, 88, 12, 33, 96, 987, -388, 22, 77, 64, 15, 20, -33]

def minimum(arr):
    min(list, key= lambda: int(i))
    return min
print('min =', list[-1])


def maximum(arr):
    max = arr[0]
    for ele in arr:
        if ele > max:
            max = ele
    return max
list.sort()
print('max =', list[-1])

# не совсем понял что вы хотели сделать таким решением(
# В max да, суть верна
# Вариант 1
# сортировка выбором
def minimum(arr):
    min_num = arr[0]
    for i in range(len(arr)):
        if arr[i] < min_num:
            min_num = arr[i]
    return min_num


def maximum(arr):
    max_num = arr[0]
    for i in range(len(arr)):
        if arr[i] > max_num:
            max_num = arr[i]
    return max_num

print('\nСортировка выбором')
print('min =', minimum([4,6,2,1,9,63,-134,566]))
print('max =', maximum([4,6,2,1,9,63,-134,566]))


# Вариант 2
# используем сортировку пузырьком
def bubblesort(l):
    for i in range(len(l)-1):
        for j in range(len(l)-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    return l

# Максимум - это последний элемент отсортированного списка
def maximum(arr):
    return bubblesort(arr)[-1]

 # Минимум - это первый элемент отсортированного списка
def minimum(arr):
    return bubblesort(arr)[0]

print('\nСортировка пузырьком')
print('min =', minimum([4,6,2,1,9,63,-134,566]))
print('max =', maximum([4,6,2,1,9,63,-134,566]))
