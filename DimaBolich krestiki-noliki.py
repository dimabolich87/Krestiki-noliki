field = [["."] * 3 for k in range(3)]


def show():
    """ функция, которая выводит визуально
        поле игры на экран.
    """

    print("  | 0 | 1 | 2 |")
    print("-" * 15)
    for k in range(3):
        print(f"{k} | {field[k][0]} | {field[k][1]} | {field[k][2]} |")
        print("-" * 15)


# show()
def take_input():
    """функция, которая позволяет ввести координаты
           и сделать необходимые минимальные проверки.
        """
    while True:
        cords = input('введите координаты от 0 до 2х через пробел: ').split()

        if len(cords) != 2:
            print("ведите 2 координаты! ")
            continue

        x, y = cords
        x, y = int(x), int(y)

        if x < 0 or x > 2 or y < 0 or y > 2:
            print("!! координаты находятся вне диапазона игры ")
            continue

        if field[x][y] != ".":
            print("!!! клетка занята,")
            continue

        return x, y


winn_comb = [((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)),
             ((2, 0), (2, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
             ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)),
             ((0, 0), (1, 1), (2, 2)), ((2, 0), (1, 1), (0, 2))]


def chek_win():
    """функция, проверяющая выигрышные комбинации"""

    for win in winn_comb:
        symbols = []

        for c in win:
            symbols.append(field[c[0]][c[1]])
            if symbols == ['X', 'X', 'X']:
                print('Мистер X победил')
                return True
            if symbols == ['O', 'O', 'O']:
                print('Мистер O победил')
                return True

    return False


def main_game():
    """главная игровая функция"""

    count = 0
    while True:
        show()
        count += 1
        if count % 2 == 1:
            print("Мистер X! Ваш ход")
        else:
            print("Мистер O! Ваш ход")

        x, y = take_input()

        if count % 2 == 1:
            field[x][y] = "X"
        else:
            field[x][y] = "O"

        if chek_win():
            break

        if count == 9:
            print('ничья')
            break


main_game()
