#Дан массив целых чисел.
#Нужно найти сумму элементов с четными индексами (0-й, 2-й, 4-й итд),
# затем перемножить эту сумму и последний элемент исходного массива.
#Не забудьте, что первый элемент массива имеет индекс 0.
#Для пустого массива результат всегда 0 (ноль).

def evenlast(array):
    result = 0
    if len(array)>0:
        for value in array[::2]:
            result += value
        result *= array[-1]
    return result

if __name__ == '__main__':
    evenlast([0, 1, 2, 3, 4, 5]) == 30
    evenlast([1, 3, 5]) == 30
    evenlast([6]) == 36
    evenlast([]) == 0
