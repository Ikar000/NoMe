def privi():
    print('         Дратути в игре      ')
    print()
    print('   Ксрестоносцы (X) и Zero (O)')
    print()
    print('Правiлы:')
    print('будем играть через координаты x и y ')
    print(' x - номер строки  ')
    print(' y - номер столбца ')
    print('Первыми ходят крестоносцы!')


def hi_pi():
    print()
    print('      0   1   2  ')

    for i, row in enumerate(field):
        row_str = f'  {i} | {" | ".join(row)} | '
        print(row_str)

    print()


def coo():
    while True:
        cord = input('      Ваш ход: ').split()

        if len(cord) != 2:
            print(' Введите 2 координаты! ')
            continue

        x, y = cord

        if not(x.isdigit()) or not(y.isdigit()):
            print(' Числа не числа! ')
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Координаты не координаты! ")
            continue

        if field[x][y] != ' ':
            print(' Клетка не клетка! ')
            continue

        return x, y


def win_win():
    w_coo = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
             ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
             ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in w_coo:
        symb = []
        for c in cord:
            symb.append(field[c[0]][c[1]])
        if symb == ['X', 'X', 'X']:
            print(' Крестоносцы победили! ')
            return True
        if symb == ['O', 'O', 'O']:
            print(' Zero победили! ')
            return True
    return False


privi()

field = [[' '] * 3 for _ in range(3)]

num_num = 0

while True:
    num_num += 1

    hi_pi()

    if num_num % 2 == 1:
        print(' Ход крестоносца ')
    else:
        print(' Ход очконавта ')

    x, y = coo()

    if num_num % 2 == 1:
        field[x][y] = 'X'
    else:
        field[x][y] = 'O'

    if win_win():
        break

    if num_num == 9:
        print(' Ничича ')
        break
