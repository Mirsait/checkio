'''
returns the difference between the maximum and minimum numbers
'''

def get_most_numbers(*args):
    print(args)
    return  (max(args)-min(args)) if len(args)>0 else 0


def test():
    print(get_most_numbers(1, 2, 3) == 2)
    print(get_most_numbers(5, -5) == 10)
    print(get_most_numbers(10.2, -2.2, 0, 1.1, 0.5) == 12.4)
    print(get_most_numbers() == 0)


if __name__ == '__main__':
    test()
