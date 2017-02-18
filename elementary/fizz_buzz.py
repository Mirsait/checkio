# Вы должны написать функцию, которая принимает положительное целое число и возвращает:
# "Fizz Buzz", если число делится на 3 и 5;
# "Fizz", если число делится на 3;
# "Buzz", если число делится на 5;
# Число, как строку для остальных случаев.

def fizzbuzz(number):
    if number%3==0 and number%5==0:
        return "Fizz Buzz"
    if number%3==0:
        return "Fizz"
    if number%5==0:
        return "Buzz"
    return str(number)


if __name__=='__main__':
    print(fizzbuzz(3)=='Fizz')
    print(fizzbuzz(5)=='Buzz')
    print(fizzbuzz(45)=='Fizz Buzz')
    print(fizzbuzz(46)=='46')
    print(fizzbuzz(101)=='101')
