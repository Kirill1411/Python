#Создайте программу для игры в ""Крестики-нолики"".

from random import randint


def print_board(board: list):
    for i in range(3):
        print(
            '|', board[0 + i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|'
        )


def add_board(board: list, sign: str):
    print_board(board)
    x = int(input(f'Выберите номер клетки для {sign}: '))
    if x > 0 or x < 10:
        if (str(board[x - 1]) not in "XO"):
            board[x - 1] = sign
            return
        else:
            print('Данная клетка уже занята')
    else:
        x = input(f'Некоректный ввод, попробуйте снова:  ')


def winner(board: list):
    coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for i in coord:
        if board[i[0]] == board[i[1]] == board[i[2]]:
            return True
    return False


def game():
    board = [i for i in range(1, 10)]
    count = 0
    check = False
    print('Начинаем!')
    while check == False:
        if count % 2 == 0:
            add_board(board, 'X')
        else:
            add_board(board, 'O')
        count += 1
        if count > 3:
            check = winner(board)
            if check:
                print('Победа!!!')
                print_board(board)
                return
        if count == 9:
            print('Ничья.')
            print_board(board)
            return


print('Приветствуем вас в игре Крестики-нолики!')
player1 = input('Введите имя игрока: ')
player2 = input('Введите имя игрока: ')
print('Очередность первого хода будет определяться случайно'
      '...')
r = randint(0, 2)
if r == 0:
    print(f'Первым ходит {player1}')
else:
    print(f'Первым ходит {player2}')
game()