def convert_to_ten(str_number, radix):
    return -1


def test():
    print(convert_to_ten("AF", 16) == 175) #"Hex"
    print(convert_to_ten("101", 2) == 5) #"Bin"
    print(convert_to_ten("101", 5) == 26) #"5 base"
    print(convert_to_ten("Z", 36) == 35) #"Z base"
    print(convert_to_ten("AB", 10) == -1) #"B > A > 10"

if __name__ == '__main__':
    test()
