from lotto_classes import *
from random import randint

"""
Игра Лото
"""

# ******************    инициализация объектов    ******************


# инициализируем все бочонки
min_chip_int = 1        # самое маленькое число на бочонке
max_chip_int = 90       # самое большое число на бочонке 'chip'

# список всех бочонков, которые еще не достали из мешка
chips_wait = []
# список отыгранных бочонков
chips_used =[]

for chips_counter in range(min_chip_int, max_chip_int + 1):
    chip = Chips(chips_counter)
    chips_wait.append(chip)


# инициализируем всех игроков
players_counter = 0

# список всех игроков
game_players = []

print(' *******  Вводим участников игры:   *******')

player_name = input('Введите имя игрока: ')

while player_name:

    print('Это человек?')
    yes_answer = yes_or_no()

    # инициализируем игрока - человека
    if yes_answer:
        g_p = HumanPlayer()
        g_p.brain = 'HI'
    # инициалищзируем игрока - компьюетер
    else:
        g_p = ComputerPlayer()
        g_p.brain = 'AI'

    g_p.id = players_counter
    players_counter += 1
    g_p.name = player_name

    game_players.append(g_p)

    player_name = input('Введите имя следующего игрока или нажмите ENTER для окончания ввода игроков: ')

print('Всего игроков:', len(game_players))

for player in game_players:
    print(player.txt_info())

print('*'*64)
print(' *******  Начинаем игру:   *******')

# остановка игры, если кто-то закрыл всю карточку
game_stop = False

# подсчет оставшихся игроков в игре:
players_in_game_count = 0
for player in game_players:
    if player.status == 'in_game':
        players_in_game_count += 1

# достаем бочонки по одному
while len(chips_wait) and not game_stop and players_in_game_count:
    # достаем бочонок из мешка:
    chip_index = randint(0, len(chips_wait)-1)
    chip_on_board = chips_wait.pop(chip_index)
    chip_on_board.status = 'on_board'

    print('В игре', players_in_game_count, 'игроков')
    print('*'*64)

    # каждый игрок делает ход
    for player in game_players:
        if player.status == 'in_game':
            # игрок делает ход
            player.move(chip_on_board)
            # если закрыта последняя цифра на карточке игрока
            if len(player.card.all_digs) == 0:
                player.status = 'win'
                game_stop = True
            print('Обновленное состояние:')
            print(player.txt_info())

    # переложим бочонок в использованные
    chip_on_board.status = 'used'
    chips_used.append(chip_on_board)

    # вновь подсчет оставшихся игроков в игре:
    players_in_game_count = 0
    for player in game_players:
        if player.status == 'in_game':
            players_in_game_count += 1

# печатаем список победителей
print('*'*32, ' Поздравляем победителей! ', '*'*32,)

for player in game_players:
    if player.status == 'win':
        print(player.id, ':', player.name)

print('*'*32, '      Игра завершена      ', '*'*32,)

