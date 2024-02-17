# Функция для вывода поля
def print_field(field):
    for j in range(3):
        print(field[j])


# Функция для проверки вводимого места для x или o
def proverka_vvoda(a):
    if len(a) == 2 and 0 <= a[0] < 3 and 0 <= a[1] < 3:
        return True
    else:
        return False


def pobeda(field, s):
    # Проверка горизонтальной победы
    for i in range(3):
        flag = True
        for j in range(3):
            if (field[i][j] == s):
                flag = True
            else:
                flag = False
                break
        if flag == True:
            return True

    # Проверка вертикальной победы
    for i in range(3):
        flag = True
        for j in range(3):
            if (field[j][i] == s):
                flag = True
            else:
                flag = False
                break
        if flag == True:
            return True

    # Проверка диагональной победы
    if (field[0][0] == s and field[1][1] == s and field[2][2] == s):
        return True
    elif (field[0][2] == s and field[1][1] == s and field[2][0] == s):
        return True


# Функция для игры с другом
def chel_vs_chel(field):
    print("Первым всегда ходит крестик")
    count = 0
    print_field(field)
    while count < 9:
        print("Куда ставим крестик? (вводите в формате 'a b' два натуральных числа [0, 3])")
        a = [int(i) for i in input().split() if i.isdigit()]
        if proverka_vvoda(a):
            stroka = a[0]
            stolbec = a[1]
            if field[stroka][stolbec] == "-":
                field[stroka][stolbec] = "x"
                count += 1
            else:
                print("Место занято :(")
                break
            if pobeda(field, "x"):
                print("Поздравляем, крестики победили!")
                print_field(field)
                break
        else:
            print("Неверные координаты :(")
            break

        print_field(field)
        print("Куда ставим нолик? (вводите в формате 'a b' два натуральных числа 0<= a,b <=3)")
        a = [int(i) for i in input().split()]
        if proverka_vvoda(a):
            stroka = a[0]
            stolbec = a[1]
            if field[stroka][stolbec] == "-":
                field[stroka][stolbec] = "o"
                count += 1
            else:
                print("Место занято :(")
                break
            print_field(field)
            if pobeda(field, "o"):
                print("Поздравляем, нолики победили!")
                break
        else:
            print("Неверные координаты :(")
            break
        if count == 9:
            print("У вас ничья)")
            break

    print("Игра окончена...")
    # если поле уже x или o - нельзя менять
    # расписать 8 вариантов выигрыша для x и o


def bot_move(field, symbol):
    weights = [
        [2, 1, 2],
        [1, 3, 1],
        [2, 1, 2]
    ]
    best_score = 0
    best_move = None

    if symbol == "x":
        sopernik = "o"
    else:
        sopernik = "x"

    for i in range(3):
        for j in range(3):
            if field[i][j] == "-":
                score = weights[i][j]
                field[i][j] = symbol
                # Проверяем, победит ли бот на следующем ходу
                if pobeda(field, symbol):
                    field[i][j] = "-"
                    return i, j
                field[i][j] = "-"
                # Проверяем, победит ли игрок на следующем ходу
                field[i][j] = sopernik
                if pobeda(field, sopernik):
                    field[i][j] = "-"
                    return i, j
                field[i][j] = "-"
                if score > best_score:
                    best_score = score
                    best_move = (i, j)

    if best_move is not None:
        row, col = best_move
        return row, col
    else:
        # Если нет доступных ходов, бот возвращает None
        return None



def chel_vs_bot(field):
    print("Выберите один из двух вариантов: ")
    print("1) Играть за крестик")
    print("2) Играть за нолик")
    flag = True
    while flag:
        u = input()
        if u.isdigit():
            symbol = int(u)
        else:
            symbol = 3
        if symbol == 1:
            # Игра за крестик
            flag = False
        elif symbol == 2:
            # Игра за нолик
            flag = False
        else:
            print("Выберите 1 или 2!")

    print_field(field)

    count = 0
    while count < 9:

        if symbol == 1:
            print("Ваш ход. Введите координаты в формате 'строка столбец': ")
            a = [int(i) for i in input().split() if i.isdigit()]
            if proverka_vvoda(a):
                stroka = a[0]
                stolbec = a[1]
                if field[stroka][stolbec] == "-":
                    field[stroka][stolbec] = "x"
                    count += 1
                else:
                    print("Место занято :(")
                    continue
                if pobeda(field, "x"):
                    print("Поздравляем, вы победили!")
                    print_field(field)
                    break
            else:
                print("Неверные координаты :(")
                continue
            if count == 9:
                break
            # Ход бота
            print_field(field)
            bot_row, bot_col = bot_move(field, "o")
            field[bot_row][bot_col] = "o"
            count += 1
            print("Ход бота:", bot_row, bot_col)
            print_field(field)
            if pobeda(field, "o"):
                print("К сожалению, бот победил. Попробуйте еще раз!")
                print_field(field)
                break
        else:
            # Ход бота
            bot_row, bot_col = bot_move(field, "x")
            field[bot_row][bot_col] = "x"
            count += 1
            print("Ход бота:", bot_row, bot_col)
            print_field(field)
            if count == 9:
                break
            if pobeda(field, "x"):
                print("К сожалению, бот победил. Попробуйте еще раз!")
                break


            print("Ваш ход. Введите координаты в формате 'строка столбец': ")
            a = [int(i) for i in input().split() if i.isdigit()]
            if proverka_vvoda(a):
                stroka = a[0]
                stolbec = a[1]
                if field[stroka][stolbec] == "-":
                    field[stroka][stolbec] = "o"
                    count += 1
                else:
                    print("Место занято :(")
                    continue
                if pobeda(field, "o"):
                    print("Поздравляем, вы победили!")
                    print_field(field)
                    break
            else:
                print("Неверные координаты :(")
                continue
    if count == 9:
        print("Ничья!")


# Создание поля 3x3, заполненного -
field = [0] * 3
for i in range(3):
    field[i] = ["-"] * 3

print("Выберите один из двух вариантов: ")
print("1) Игра с другом")
print("2) Игра с ботом")

flag = True
while flag:
    f = input()
    if f.isdigit():
        choice = int(f)
    else:
        choice = 3
    if choice == 1:
        chel_vs_chel(field)
        flag = False
    elif choice == 2:
        chel_vs_bot(field)
        flag = False
    else:
        print("Выберите 1 или 2!")
