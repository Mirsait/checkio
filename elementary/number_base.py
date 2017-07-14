def convert_to_ten(str_number, radix):
    if (radix < 2 or radix > 36):
        return -1
    dist = {k:v for v, k in enumerate('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', start=1)}
    str_number_len = len(str_number) - 1
    sum = 0
    for index, item in enumerate(str_number):
        int_number = dist.get(item)-1
        if  int_number >= radix:
            return -1
        exp = str_number_len - index
        sum += (radix**exp * int_number)
    return sum


def test():
    print(convert_to_ten("AF", 16) == 175) #"Hex"
    print(convert_to_ten("101", 2) == 5) #"Bin"
    print(convert_to_ten("101", 5) == 26) #"5 base"
    print(convert_to_ten("Z", 36) == 35) #"Z base"
    print(convert_to_ten("AB", 10) == -1) #"B > A > 10"

if __name__ == '__main__':
    test()
