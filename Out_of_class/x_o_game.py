import random

# Приветствуем игроков
name_one_player = input("Введите ваше имя: ")
print(f'Приветствую тебя, {name_one_player}!')
name_two_player = input("Введите имя второго игрока: ")
print(f'Приветствую тебя, {name_two_player}!')
print()


# Гемплей
def game_play(player_name, char, mat_game):
    print(f'Ход игрока {player_name}')
    mui_player_one = (input('Ваш ход, введите цифру позиции: '))
    for i in range(len(mat_game)):
        for j in range(len(mat_game)):
            if mui_player_one == mat_game[i][j] and mat_game[i][j] != 'X' and mat_game[i][j] != 'O':
                mat_game[i][j] = char

    for i in range(len(mat_game)):
        print(mat_game[i])

    return mat_game


# Проверка есть ли победитель
def count_games(mat_game):
    if mat_game[0][0] == mat_game[0][1] == mat_game[0][2]:
        return True
    elif mat_game[1][0] == mat_game[1][1] == mat_game[1][2]:
        return True
    elif mat_game[2][0] == mat_game[2][1] == mat_game[2][2]:
        return True
    elif mat_game[0][0] == mat_game[1][0] == mat_game[2][0]:
        return True
    elif mat_game[0][1] == mat_game[1][1] == mat_game[2][1]:
        return True
    elif mat_game[0][2] == mat_game[1][2] == mat_game[2][2]:
        return True
    elif mat_game[0][0] == mat_game[1][1] == mat_game[2][2]:
        return True
    elif mat_game[2][0] == mat_game[1][1] == mat_game[0][2]:
        return True
    else:
        return False


# Случайный выбор первого хода
random_move = random.randint(1, 2)

# Создание игрового поля
matrix_game = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
for i in range(len(matrix_game)):
    print(matrix_game[i])

# Запуск игры
count = False
count_len = 9
while count == False:
    if random_move == 1:
        game_play(name_one_player, 'O', matrix_game)
        count = count_games(matrix_game)
        random_move = 2
        count_len -= 1
    elif random_move == 2:
        game_play(name_two_player, 'X', matrix_game)
        count = count_games(matrix_game)
        random_move = 1
        count_len -= 1
    if count_len == 0:
        count = None

# Вывод победителя
if count == True and random_move == 2:
    print(f'Победил игрок {name_one_player}!!!')
elif count == True and random_move == 1:
    print(f'Победил игрок {name_two_player}!!!')
elif count == None:
    print('НИЧЬЯ!!!')
