'''
returns the difference between the maximum and minimum numbers
'''

def get_most_numbers(*args):
    return max(args)-min(args) if args else 0


def test_method():
    print(get_most_numbers(1, 2, 3) == 2)#true
    print(get_most_numbers(5, -5) == 10)#true
    print(get_most_numbers(10.2, -2.2, 0, 1.1, 0.5) == 12.4)#true
    print(get_most_numbers() == 0)#true


if __name__ == '__main__':
    test_method()
