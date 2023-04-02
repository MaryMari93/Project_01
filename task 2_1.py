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
