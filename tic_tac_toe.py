import random
import time

# -----------------------------ФУНКЦИИ-----------------------------

# Интерфейс стартового меню
def start_menu():
    print(f"1. Начать игру") # Начать игру
    print(f"0. Выход") # Выйти из игры
    print(f"------------------") # Пунктирная линия для UI

# Визуализация поля игры
def display_field(game_field):
    
    row_num = 0 # Счётчик строк
    
    for row in game_field:
        row_num += 1
        print(f"{row_num}.", end=' ')
        print(*row)
    print('----------------------------------------')

# Обработка выбранного поля игроком/ботом
def hero_choice(game_field, move, hero, is_bot_move=False):
    find_move = 0 # Номер найденного поля (по умолчанию 0)

    if is_win_check(game_field):
        for i in range(0, len(game_field)):
            for j in range(0, len(game_field)):
                find_move += 1
                
                if find_move == move and game_field[i][j] == '-':
                    game_field[i][j] = hero
                    return True
                elif find_move == move and game_field[i][j] != '-' and is_bot_move:
                    # print("Бот сделал ход на занятое поле!")
                    # time.sleep(1)
                    # print("Бот переставляет ход...")
                    return False
                elif find_move == move and game_field[i][j] != '-':
                    print("Игрок, ты выбрал занятое поле!")
                    return False
            
            if find_move == move:
                break
    else:
        return True

def display_winner(game_field, hero):
    print('-------------------WIN------------------')
    time.sleep(0.5)
    print(f'🏆 Победил {hero}')
    time.sleep(0.5)
    
    display_field(game_field)

# Функция сканирования поля
def is_win_check(game_field):
    
    n = len(game_field)

    # Счётчик пустых полей
    total_line = [1 for i in range(0, n) if '-' in game_field[i]]
    total_x = [game_field[i].count('X') for i in range(0, n)]
    total_o = [game_field[i].count('O') for i in range(0, n)]

    if 3 in total_x or 3 in total_o:
        if 3 in total_o:
            display_winner(game_field, 'Нолик')
            
            return False
        elif 3 in total_x:
            display_winner(game_field, 'Крестик')

            return False
    else:
        total_x = []
        total_o = []

        # Парсинг элементов столбцов (Вертикальные победные комбинации)
        for i in range(0, n):
            for j in range(0, n):
                if game_field[j][i] == 'X':
                    total_x.append(1)
                elif game_field[j][i] == 'O':
                    total_o.append(1)

            if sum(total_x) == 3:
                display_winner(game_field, 'Крестик')

                return False
            elif sum(total_o) == 3:
                display_winner(game_field, 'Нолик')

                return False
            
            else:
                total_x = []
                total_o = []

        # Парсинг элементов по диагонали (Главной и Побочной)
        
    # Если пустых полей нет, то конец игры
    if sum(total_line) == 0:
        display_field(game_field)
        print('Игра кончилась.')
        return False
    # Иначе игра продолжается
    else:
        return True
    
# ---------------------------------------------------------------------------------------
         
# --------------------------------------НАЧАЛО ИГРЫ--------------------------------------

start_menu() # Стартовое меню
main_menu = int(input(": ")) # Номер Пункта меню
while main_menu != 0:

    field = [
                ['-', '-', '-',],
                ['-', '-', '-',],
                ['-', '-', '-',],
        ]

    if main_menu == 1:
        breakpoent = 0
        print("1. За крестик")
        print("2. За нолик")

        hero_num = int(input("За кого хочешь играть?: "))

        if hero_num == 1:
            print("Ты выбрал Крестик (Х)")
            print("Игра началась.")
            print("----------------------")

            while is_win_check(field):
        
                display_field(field)
                
                player_move = int(input("Выбери позицию куда сделать ход (от 1 до 9): "))
                bot_move = random.randint(1, 9)

                if player_move > 9 or player_move < 1:
                    print("Введите число в диапазоне от 1 до 9!")
                else:
                    while hero_choice(field, player_move, 'X') == False:
                        player_move = int(input("Выбери позицию куда сделать ход (от 1 до 9): "))
                        # hero_choice(field, player_move, 'X')

                    breakpoent += 1

                    if breakpoent == 8:
                        pass

                    while hero_choice(field, bot_move, 'O', True) == False:
                        bot_move = random.randint(1, 9)
                        # hero_choice(field, bot_move, 'O', True)

        elif hero_num == 2:
            print("Ты выбрал Нолик (O)")
            print("Игра началась.")
            print("----------------------")

            while is_win_check(field):
        
                display_field(field)
                
                player_move = int(input("Выбери позицию куда сделать ход (от 1 до 9): "))
                bot_move = random.randint(1, 9)

                if player_move > 9 or player_move < 1:
                    print("Введите число в диапазоне от 1 до 9!")
                else:
                    while hero_choice(field, player_move, 'O') == False:
                        player_move = int(input("Выбери позицию куда сделать ход (от 1 до 9): "))
                        # hero_choice(field, player_move, 'O')

                    while hero_choice(field, bot_move, 'X', True) == False:
                        bot_move = random.randint(1, 9)
                        # hero_choice(field, bot_move, 'X', True)
        else:
            print("Введи цифру 1 или 2")

    start_menu()
    main_menu = int(input(": "))

# =========Задачи==========
# 1. Считать ход Нолика (О)
#       ✅ Получить число из библиотеки random, и присвоить его Нолику
#       ✅ Найти это число на поле игры, и поставить Нолик (O) на СВОБОДНОЕ поле
# 2. Отслеживать кто победил
#   o Надо сканировать поле на наличие победных комбинаций
#       o Сделать проверку комбинаций
#           ✅ Вертикальных
#           ✅ Горизонтальных
#           o Главной диагонали
#           o Побочной диагонали
#       ✅ Надо добавить счётчик символов крестика (X) и нолика (О) одновременно

# =========Доработки==========
# 1. Предупреждать о том, что ход на указанном поле сделан (если кншн он сделан)
#   o Не давать ставить боту ход на занятую клетку
#       o Написать для бота отдельную функцию по проверке хода