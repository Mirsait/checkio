'''
returns the difference between the maximum and minimum numbers
'''

def get_most_numbers(arg):
    pass

if __name__ == '__main__':
    get_most_numbers(1, 2, 3) == 2
    get_most_numbers(5, -5) == 10
    get_most_numbers(10.2, -2.2, 0, 1.1, 0.5) == 12.4
    get_most_numbers() == 0
