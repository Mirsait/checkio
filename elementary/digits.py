from functools import reduce
def checkio(number):
    str_number = [int(num) for num in str(number) if num != '0']
    return reduce(lambda multy, n: multy * n, str_number, 1)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
