from random import choice


def create(mines):
    global FIELD, OPEN
    FIELD = [[0 for _ in range(mines)] for _ in range(mines)]
    OPEN = [[False for _ in range(num)] for _ in range(num)]


def append_flag(x, y):
    FLAG.append((y, x))


def inside(x, y):
    return 0 <= x < num and 0 <= y < num


def mine(x, y):
    if inside(x, y):
        if FIELD[y][x] == -1:
            return True
    return False


def end():
    if not state:
        openmines()
        print_field()
        print('вы проиграли')
    else:
        print_field()
        print('вы выиграли')


def openmines():
    for y in range(num):
        for x in range(num):
            if FIELD[y][x] == -1:
                OPEN[y][x] = True


def check(answer):
    if len(answer) == 3:
        if answer[-1] in '!?.':
            if answer[0].isdigit() and answer[1].isdigit():
                if not OPEN[answer[1]][answer[0]]:
                    return True
    return False


def empty(x, y):
    if inside(x, y):
        if FIELD[y][x] == 0:
            return True
    return False


def print_field():
    for y in range(num):
        for x in range(num):
            if OPEN[y][x]:
                if FIELD[x][y] == -1:
                    print('[*]', end='')
                elif FIELD[y][x] == 0:
                    print('[.]', end='')
                else:
                    print(FIELD[y][x], end='')
            else:
                if (y, x) in FLAG:
                    print('[?]', end='')
                else:
                    print('[]', end='')
        print()
    print()


def clear(x, y):
    if inside(x, y):
        OPEN[y][x] = True
        if FIELD[y][x] == 0:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if (y + i, x + j) != (y, x):
                        clear(i + y, j + x)
#        else:
#            for i in range(-1, 2):
#                for j in range(-1, 2):
#                    if (y + i, i + j) != (y, x):
#                        if empty(i + y, j + x):
#                            clear(y + i, x + j)


def pole(coords):
    for i in range(num):
        mina = (choice(range(num)), choice(range(num)))
        while mina == coords:
            mina = (choice(range(num)), choice(range(num)))
        FIELD[mina[1]][mina[0]] = -1
    for y in range(num):
        for x in range(num):
            if FIELD[y][x] != -1:
                k = 0
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if (y + i, x + j) != (y, x):
                            if mine(i + y, x + j):
                                k += 1
                FIELD[y][x] = k


def checkwin_flags():
    for i in FLAG:
        y, x = i
        if FIELD[y][x] != -1:
            return False
    return True


def checkwin_blanks():
    for y in range(num):
        for x in range(num):
            if FIELD[y][x] != -1 and not OPEN[y][x]:
                return False
    return True


notification = 'Введите строку в формате X Y -, где -:\n\t! - отметить клетку,' \
               '\n\t? - поставить флажок,\n\t. - убрать флажок\n:'
state = True
OPEN = []
FIELD = []
FLAG = []
print('С А П Ё Р')
num = input('Введите количество мин:\t')
while not num.isdigit():
    num = input('Введите кореектное значение:\t')
num = int(num)
create(num)
print()
print_field()
move = input('Введите клетку в формате X Y:\t')
move_split = move.split(' ')
while len(move_split) != 2 or not move_split[0].isdigit() or not move_split[1].isdigit():
    print('введите корректные данные')
    move = input('Введите клетку в формате X Y:\t')
    move_split = move.split(' ')
pole(tuple([int(i) for i in move_split]))
clear(*[int(i) for i in move_split])
while state:
    print_field()
    move = input(notification).split(' ')
    while not check:
        print('введите корректные данные')
        move = input(notification).split(' ')
    x, y, operation = move
    if operation == '!':
        if mine(y, x):
            state = False
            end()
        else:
            clear(y, x)
            if checkwin_blanks():
                end()
                break
    elif operation == '?':
        if (y, x) not in FLAG:
            if len(FLAG) == num:
                print('Слишком много флагов. Уберите уже имеющийся.')
            else:
                append_flag(x, y)
                if checkwin_flags():
                    end()
                    break
        else:
            print('введите корректные данные')
    elif operation == '.':
        if (y, x) not in FLAG:
            print('Такого флага не существует.')
        else:
            FLAG.remove((y, x))
