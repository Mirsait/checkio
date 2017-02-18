#Cipher map

def recall_password(grille, password):
    new_pass = ''
    for fourth_i in range(4):#rotate
        for row_index in range(4):#rows
            fourth = ''
            for i, item in enumerate(grille[row_index]):#items
                if item=='X':
                    fourth += password[row_index][i]
            new_pass += fourth
        grille = rotate(grille)
    return new_pass

def rotate(matrix):
    rmatr = []
    for index in range(4):
        new_row = [row[index] for row in matrix]
        new_row.reverse()
        rmatr.append(new_row)
        rmatr[index] = ''.join(rmatr[index])
    return rmatr

if __name__ == '__main__':
    print(recall_password(
        ('X...',
        '..X.',
        'X..X',
        '....'),
        ('itdf',
        'gdce',
        'aton',
        'qrdi')))
    print(recall_password(
        ('X...',
        '..X.',
        'X..X',
        '....'),
        ('itdf',
        'gdce',
        'aton',
        'qrdi')) == 'icantforgetiddqd')

    print(recall_password(
        ('....',
        'X..X',
        '.X..',
        '...X'),
        ('xhwc',
        'rsqx',
        'xqzz',
        'fyzr')) == 'rxqrwsfzxqxzhczy')
