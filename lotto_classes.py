from random import randint

"""
Описание объектов для игры в Лото
"""

def yes_or_no():
    """
    функция добивается ответа пользователя либо да, либо нет.
    :return: True, если 'да';  False, если 'нет'
    """
    answer = 'waiting for an answer'

    while answer != 'да' and answer != 'нет':
        answer = input('\'да\' или \'нет\'? ').lower().strip()

    yes_answer = True if answer == 'да' else False

    return yes_answer


class Cards:
    """
    Карточки для игры в лото
    """

    def __init__(self):
        #  создание карточки
        rows = 3           # количество строк в карточке
        dig_in_row = 5     # количество цифр в строке
        places_in_row = 9  # количество позиций в строке
        min_int = 1        # самое маленькое число
        max_int = 90       # самое большое число
        row_digs = []      # это все цифры в строках карточки
        row_masks = []     # это все места для печати чисел или пустых значений в строках карточки

        for i in range(rows):

            # создаем маску одной строки r_m
            r_m = [0 for k in range(places_in_row)]
            # генерируем места ==1 для dig_in_row цифр, остальные места будут пустыми ==0
            while sum(r_m) < dig_in_row:
                r_m[randint(0, places_in_row - 1)] = 1

            # собираем двумерный список масок
            row_masks.append(r_m)
            # пример результата:
            # [[1, 0, 0, 0, 1, 1, 0, 1, 1], [0, 1, 0, 1, 1, 0, 1, 1, 0], [0, 1, 1, 1, 0, 1, 1, 0, 0]]

            # создаем список из dig_in_row уникальных чисел по возрастанию для каждой строки
            r_d = []

            while len(r_d) < dig_in_row:
                # собираем множество всех уже использованных чисел all_digs
                #     все числа в двумерном списке разворачиваем в одномерный
                #     и преобразуем в множество
                all_digs = set([a for b in row_digs for a in b])
                #     все цифры в формируемой строке
                new_digs = set(r_d)
                all_digs = all_digs | new_digs
                #     новое число
                dig = randint(min_int, max_int)
                if dig not in all_digs:
                    r_d.append(dig)

            # собираем двумерный список чисел
            r_d.sort()
            row_digs.append(r_d)
            # пример результата:
            # [[15, 27, 45, 77, 84], [9, 39, 43, 62, 65], [10, 26, 28, 64, 90]]

        # соберем итоговое множество чисел
        all_digs = set([a for b in row_digs for a in b])
        # пример результата:
        # {64, 65, 90, 39, 9, 10, 43, 77, 45, 15, 84, 26, 27, 28, 62}

        # заменим в маске row_masks единицы на числа из row_digs

        for i in range(len(row_masks)):
            j = 0  # индекс списка row_digs
            for k in range(len(row_masks[i])):
                if row_masks[i][k] != 0:
                    row_masks[i][k] = row_digs[i][j]
                    j += 1
        # пример результата row_masks:
        # [[15, 0, 0, 0, 27, 45, 0, 77, 84], [0, 9, 0, 39, 43, 0, 62, 65, 0], [0, 10, 26, 28, 0, 64, 90, 0, 0]]

        self.id = None                     # id карты
        self.player_id = 0                 # id игрока, которому сдана карточка
        self.all_digs = all_digs           # множество всех чисел на карточке
        self.lines_to_print = row_masks    # список строк с нулями и цифрами на карточке

    def card_as_txt(self):
        """
        Функция формирует текст, который потом можно напечатать
        :return: txt_prn - текстовая строка для печати
        """
        places_in_row = 9
        txt_prn = '-' * (places_in_row*5 + 1) + '\n'    # верхняя линия

        for line in self.lines_to_print:
            txt_prn = txt_prn + chr(124)
            for dig in line:
                if dig == 0:
                    txt_prn = txt_prn + '  .. '
                elif dig == -1:
                    txt_prn = txt_prn + ' --- '
                else:
                    txt_prn = txt_prn + str(dig).rjust(4) + ' '

            txt_prn = txt_prn + chr(124) + '\n'
            txt_prn = txt_prn + '-' * (places_in_row*5 + 1) + '\n'   # нижняя линия

        return txt_prn

    def cross_out(self, number):
        """
        'зачеркивает' выбывающее число number.
        Если успешно, то возвращает True,
            исключает число number из множества self.all_digs
            и записывает в self.lines_to_print на место числа '-1',
               теперь при печати на месте выбывающего числа будет стоять прочерк
        Если такого числа не было, возвращает False
        :param number: целое число, которое, предположительно, выбывает
        :return:  True, если такое число было, иначе False
        """

        correct_number = (number in self.all_digs)

        if correct_number:
            for line in self.lines_to_print:
                try:
                    i = line.index(number)
                    # заменяем выбывающее число в таблице для печати на '-1'
                    line[i] = -1
                    # исключаем выбывающее число из множества цифр
                    self.all_digs = self.all_digs - {number}
                except ValueError:
                    pass   # если число не нашлось в этой строке, найдется в другой

        return correct_number


class Player:
    """
    игроки
    """

    def __init__(self):
        self.id = None            # id игрока
        self.name = None          # имя игрока
        self.status = 'in_game'   # 'in_game' - в игре
                                  # 'win' - выиграл
                                  # 'lost' - проиграл
        self.card = Cards()       # генерируется карта class Cards, которая сдана игроку
        self.brain = None         # 'HI' == человек, 'AI' == компьютер

    def txt_info(self):
        """
        Функция возвращает текстовую информацию об игроке и состоянии его карточки
        :return: txt
        """

        txt_status = ''
        if self.status == 'in_game':
            txt_status = ' - в игре'
        elif self.status == 'win':
            txt_status = ' Это победитель. Поздравляем!!!'
        elif self.status == 'lost':
            txt_status = ' Проиграл. Не унывайте. Удача придёт.'
        else:
            txt_status = ' Что он здесь делает? - Не определено'

        txt = '*'*64 + '\n'
        txt = txt + 'Игрок id: ' + str(self.id) + ', Статус: ' + txt_status + '\n'

        txt = txt + 'Имя: ' + str(self.name) + '\n'

        txt_brain = ''
        if self.brain == 'HI':
            txt_brain = 'это человек'
        elif self.brain == 'AI':
            txt_brain = 'это компьютер'
        else:
            txt_brain = 'Кто это? - Не определено'

        txt = txt + 'Тип игрока: ' + txt_brain + '\n\n'

        txt = txt + self.card.card_as_txt()

        return txt



class HumanPlayer(Player):
    """
    игрок - человек
    """

    # def __init__(self):
    #     self.brain = 'HI'  # 'HI' == Human Intelegence

    def move(self, boch):
        """
        ход человека в ответ на вновь открытое число
        :return: True, если игрок не ошибся
        """

        print('Ход игрока', self.name, '       Состояние карточки:')
        print(self.card.card_as_txt())
        print('Выпал номер', boch.id)

        yes_answer = yes_or_no()

        # правильный ли номер у боченка (есть ли такой на карте)
        included = boch.id in self.card.all_digs

        # игрок сделал правильный выбор, если его ответ совпадает
        #     с вхождением числа на бочонке в карточку
        correct_answer = True if yes_answer == included else False

        # вычеркнуть открывшееся число
        if correct_answer and included:
            self.card.cross_out(boch.id)
            self.card.all_digs = self.card.all_digs - {boch.id}


        if not correct_answer:
            self.status = 'lost'
            print('Вы ошиблись и выбываете из игры \n')

        return correct_answer


class ComputerPlayer(Player):
    """
    игрок - компьютер
    """

    def move(self, boch):
        """
        ход компьютера в ответ на вновь открытое число
        :return: True, компьютер всегда выдает верный ответ
        """
        print('Ход игрока', self.name)
        print(self.card.card_as_txt())
        print('Выпал номер', boch.id)
        included = boch.id in self.card.all_digs
        # имитируем ответ игрока
        txt_answer = 'да' if included else 'нет'
        print('\'да\' или \'нет\'? ', txt_answer)

        # зачеркнуть
        if included:
            self.card.cross_out(boch.id)

        return True


class Chips:
    """
    бочонки
    """

    def __init__(self):
        self.id = None         # допустимо от 1 до 90 включительно
        self.status = 'wait'   # 'wait' == лежит в мешке;
                               # 'on_board' == на столе;
                               # 'out' == отыгран



