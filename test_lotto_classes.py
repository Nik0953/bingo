import unittest

from lotto_classes import *

"""
модуль для тестирование классов и функций из модуля lotto_classes
"""


def test_yes_or_no():
    # частичное тестирование грязной функции с консольным вводом-выводом
    assert yes_or_no('да')
    assert not yes_or_no('нет')


class TestCards(unittest.TestCase):

    def setUp(self):
        self.crd = Cards()

    def tearDown(self):
        del self.crd

    def test_init(self):

        self.assertEqual(len(self.crd.lines_to_print), 3, 'должно быть 3 строки')

        for line in self.crd.lines_to_print:
            self.assertEqual(len(line), 9, 'должно быть 9 позиций в строке')

            # в кажджой строке новой карты
            #     должно быть 5 положительных чисел от 1 до 90, также может быть 0
            positive_digs_count = 0  # счетчик положительных чисел

            for dig in line:
                if dig > 0 and dig < 91:
                    positive_digs_count += 1
                elif dig != 0:
                    self.assertFalse(True, 'не подходящее число' + str(dig))

            self.assertEqual(positive_digs_count, 5, ' должно быть 5 положительных чисел в строке')

        digs_lst = []
        # все положительные числа должны быть уникальными
        for line in self.crd.lines_to_print:
            for dig in line:
                if dig > 0:
                    digs_lst.append(dig)
        self.assertEqual(len(digs_lst), len(set(digs_lst)), 'повторяющиеся числа')

    def test_card_as_txt(self):

        # тестовый список
        tst_lst = [[15, 0, 0, 0, 27, 45, 0, 77, 84], [0, 9, 0, 39, 43, 0, 62, 65, 0], [0, 10, 26, 28, 0, 64, 90, 0, 0]]
        self.crd.lines_to_print = tst_lst

        # ожидаемый результат
        tst_crd_to_print = '----------------------------------------------\n'
        tst_crd_to_print = tst_crd_to_print + '|  15   ..   ..   ..   27   45   ..   77   84 |\n'
        tst_crd_to_print = tst_crd_to_print + '----------------------------------------------\n'
        tst_crd_to_print = tst_crd_to_print + '|  ..    9   ..   39   43   ..   62   65   .. |\n'
        tst_crd_to_print = tst_crd_to_print + '----------------------------------------------\n'
        tst_crd_to_print = tst_crd_to_print + '|  ..   10   26   28   ..   64   90   ..   .. |\n'
        tst_crd_to_print = tst_crd_to_print + '----------------------------------------------\n'
        # рассчитанный результат
        result_txt = self.crd.card_as_txt()

        self.assertEqual(tst_crd_to_print, result_txt, 'текст карточки формируется некорректно')

    def test_cross_out(self):

        # тест для числа 15, входящего в список
        # тестовый список
        tst_lst = [[15, 0, 0, 0, 27, 45, 0, 77, 84], [0, 9, 0, 39, 43, 0, 62, 65, 0], [0, 10, 26, 28, 0, 64, 90, 0, 0]]
        self.crd.lines_to_print = tst_lst
        self.crd.all_digs = set([a for b in tst_lst for a in b])

        # число 15 должно быть опознано, как входящее в карточку
        result_bool = self.crd.cross_out(15)
        self.assertEqual(result_bool, True, 'число, входящее в картокчку, не опознано')

        # число 15 должно быть заменено на -1
        self.assertEqual(self.crd.lines_to_print[0][0], -1, 'число 15 не заменено на -1')

        # число 15 должно быть удалено из множества чисел после его 'вычеркивания'
        self.assertEqual((not ({15} in self.crd.all_digs)), True, 'удаляемое число осталось во множестве')

        # тест для числа 7, не входящего в список
        # тестовый список
        tst_lst = [[15, 0, 0, 0, 27, 45, 0, 77, 84], [0, 9, 0, 39, 43, 0, 62, 65, 0], [0, 10, 26, 28, 0, 64, 90, 0, 0]]
        self.crd.lines_to_print = tst_lst
        self.crd.all_digs = set([a for b in tst_lst for a in b])

        # число 7 НЕ должно быть опознано, как входящее в карточку
        result_bool = self.crd.cross_out(7)
        self.assertFalse(result_bool, True)


class TestPlayer:

    def test_init(self):
        plr = Player()
        crd = Cards
        assert isinstance(plr.card, Cards), 'не создана надлежащая игровая карточка'
        assert plr.status == 'in_game'

    def txt_info(self):

        plr = Player()
        plr.name = 'Nick'
        plr.id = 7
        plr.brain = 'AI'
        plr.status = 'win'
        plr.card.lines_to_print = [[15, 0, 0, 0, 27, 45, 0, 77, 84], [0, 9, 0, 39, 43, 0, 62, 65, 0], [0, 10, 26, 28, 0, 64, 90, 0, 0]]

        txt_exp = '****************************************************************\n'
        txt_exp = txt_exp + 'Игрок id: 7, Статус:  Это победитель. Поздравляем!!!\n'
        txt_exp = txt_exp + 'Имя: Nick\nТип игрока: это компьютер\n\n'
        txt_exp = txt_exp + '----------------------------------------------\n'
        txt_exp = txt_exp + '|  15   ..   ..   ..   27   45   ..   77   84 |\n'
        txt_exp = txt_exp + '----------------------------------------------\n'
        txt_exp = txt_exp + '|  ..    9   ..   39   43   ..   62   65   .. |\n'
        txt_exp = txt_exp + '----------------------------------------------\n'
        txt_exp = txt_exp + '|  ..   10   26   28   ..   64   90   ..   .. |\n'
        txt_exp = txt_exp + '----------------------------------------------\n'
        txt_exp = txt_exp + '\n\n'

        assert plr.txt_info() == txt_exp, 'неверное формирование карты игрока'


class TestComputerPlayer:

    # проверяем распознавание вхождения заведомо принадлежащего карточке числа
    plr = ComputerPlayer()
    all_digs = plr.card.all_digs

    # выбираем число b, заведомо присутствующее в карточке
    b = int(list(all_digs)[0])
    boch = Chips(b)
    included_expected = plr.move(boch)
    assert included_expected, 'ошибка 1 ComputerPlayer.move()'

class TestChips:

    def test_init(self):
        b = 77     # любое значение для инициализации id
        bochka = Chips(b)
        assert b == bochka.id
        assert bochka.status == 'wait'
