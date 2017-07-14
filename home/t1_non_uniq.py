# Дан непустой массив целых чисел (X). В этой задаче вам нужно вернуть массив,
# состоящий только из неуникальных элементов данного массива. Для этого
# необходимо удалить все уникальные элементы (которые присутствуют в данном
# массиве только один раз). Для решения этой задачи не меняйте оригинальный
# порядок элементов. Пример: [1, 2, 3, 1, 3], где 1 и 3 неуникальные элементы и
# результат будет [1, 3, 1, 3]

arrs1 = [1, 2, 3, 1, 2, 3, 4, 5]
arrs2 = [1, 2, 3, 1, 2, 3, 5]
arrs3 = [5, 5, 5, 5]
arrs4 = [1,2,3,4]
arrs5 = []

def get_non_unique (data):
    backup = data[:]
    for a in data:
        if data.count(a) < 2:
            backup.remove(a)
    return backup


if __name__ == '__main__':
    print(get_non_unique(arrs1))
    print(get_non_unique(arrs2))
    print(get_non_unique(arrs3))
    print(get_non_unique(arrs4))
    print(get_non_unique(arrs5))


