# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

# Стратегия игры: Если мой ход первый то забрать 6 конфет и после каждого хода противника брать количество конфет
# 28 - ход противника.
# Если хожу вторым, то после каждого хода противника брать количество конфет
# 28 - ход противника.
import random


# Приветствие и выбор противника
def choice_user():
    print('Приветствую вас, игроки! Меня зовут Антон!')
    choice_user = input \
        ('Если вы хотите играть со мной в эту игру,\n'
         'введите: Y'
         '\nЕсли вы хотите играть вдвоем, введите: N\n')
    if choice_user.lower() == 'y':
        return 'auto'
    elif choice_user.lower() == 'n':
        return 'hand'
    else:
        print('Не корректный ввод')
        return choice_user()


# Ввод имени игрока
def hand_play():
    name = input('Введите имя игрока: ')
    return name


# Чей следущий ход
def play_label(number_label, name_one=1, name_two=2):
    if number_label == 0:
        print(f'Ход игрока {name_two}:')
        number_label = 1
    elif number_label == 1:
        print(f'Ход игрока {name_one}:')
        number_label = 0
    else:
        return
    return number_label


# Поговори с Антоном
def voice_anton():
    voice_list = \
        ['Не тормози, это простая игра!', 'Мне кажется я уже выиграл!',
         'Эту цифру я видел во сне', 'Твой ход дружище!', 'А у тебя конфеты с какой начинкой?']
    print(random.choice(voice_list))


# Ход бота Антон
def auto_player():
    move = random.randint(1, 28)
    print(f'Я возьму {move} конфет(ы)')
    voice_anton()
    return move


# Ход игрока
def play():
    players_move_in = int(input())
    return players_move_in


# Метод подсчета оставшихся конфет
def players_move(user_numbers, volume):
    if user_numbers <= 28:
        volume = volume - user_numbers
        return volume
    else:
        print('Число не может превышать 28! Вы проиграли!')
        return game(choice_user())


# Кто победил
def winner(number_label, name_p_one, name_p_two):
    if number_label == 0:
        print(f'Все конфеты достаются победителю - {name_p_two}!!!')
    else:
        print(f'Все конфеты достаются победителю - {name_p_one}!!!')


# Игра с конфетами
def game(choice):
    max_of_one_step = 28
    candy_bank = 2021
    flag = random.randint(0, 1)
    names = hand_play()
    if choice == 'hand':
        names_two = hand_play()
    elif choice == 'auto':
        names_two = 'Anton'
    while candy_bank > max_of_one_step:
        if flag == 1:
            flag = play_label(flag, names, names_two)
            candy_bank = players_move(play(), candy_bank)
        else:
            if choice == 'auto':
                flag = play_label(flag, names, names_two)
                candy_bank = players_move(auto_player(), candy_bank)
            elif choice == 'hand':
                flag = play_label(flag, names, names_two)
                candy_bank = players_move(play(), candy_bank)

        print(f'Число конфет на столе: {candy_bank}')
    winner(flag, names, names_two)


# Запуск игры
game(choice_user())
