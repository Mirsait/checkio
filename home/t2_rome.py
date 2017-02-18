'''
Римские цифры пришли к нам из древней римской системы счета.
Они основаны на особых буквах алфавита, которые в азличных сочетаниях,
путем суммирования (а иногда и разницы) описывают различные числа.
Первые 10 римских чисел это: I, II, III, IV, V, VI, VII, VIII, IX, and X.

Римская система счета имеет десятичное основание, но она непозиционная и
не включает в себя 0 (ноль). Римские числа образуются путем комбинации
следующих семи символов:
Символ - Значение
I 1 (unus)
V 5 (quinque)
X 10 (decem)
L 50 (quinquaginta)
C 100 (centum)
D 500 (quingenti)
M 1,000 (mille)

В этой задаче, вам необходимо преобразовать данное целое число (от 1 до 3999)
в римскую систему счета.

Вх. данные: Число, как целочисленное (int).

Вых. данные: Римское число, как строка (str).
'''


def get_rome (number):
    rome_dist = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
    rome_number = ''

    tousends = number // 1000
    rome_number += (tousends * rome_dist[1000])
    rest = number % 1000 #<1000

    for i in (100,10,1):
        fives = rest // (5*i)
        rest = rest % (5*i)
        tens =  rest // (1*i)
        if fives:
            if tens == 4:
                rome_number += rome_dist[1*i] + rome_dist[10*i]
            else:
                rome_number += rome_dist[5*i] + tens*rome_dist[1*i]
        else:
            rome_number += (fives * rome_dist[5*i])
            if tens==4:
                rome_number += (rome_dist[1*i]+rome_dist[5*i])
            else:
                rome_number += (tens * rome_dist[1*i])
        rest = rest % (1*i)
    return rome_number

if __name__=='__main__' :
    print(get_rome(6) == 'VI')
    print(get_rome(76) == 'LXXVI')
    print(get_rome(13) == 'XIII')
    print(get_rome(44) == 'XLIV')
    print(get_rome(3999) == 'MMMCMXCIX')
    print(get_rome(2222))
