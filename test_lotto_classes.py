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

    def test_str(self):

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
        result_txt = str(self.crd)

        self.assertEqual(tst_crd_to_print, result_txt, 'текст карточки формируется некорректно')

    def test_eq(self):
        crd1 = Cards()
        crd2 = Cards()
        crd_other = Cards()
        crd1.all_digs = {64, 65, 90, 39, 9, 10, 43, 77, 45, 15, 84, 26, 27, 28, 62}
        crd2.all_digs = {90, 65, 64, 62, 39, 9, 10, 43, 77, 45, 15, 84, 26, 27, 28}   # те же, но в другом порядуке
        crd_other.all_digs = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}      # совсем другое множество
        assert crd1 == crd2
        assert not (crd1 == crd_other)

    def test_ne(self):
        crd1 = Cards()
        crd2 = Cards()
        crd_other = Cards()
        crd1.all_digs = {64, 65, 90, 39, 9, 10, 43, 77, 45, 15, 84, 26, 27, 28, 62}
        crd2.all_digs = {90, 65, 64, 62, 39, 9, 10, 43, 77, 45, 15, 84, 26, 27, 28}  # те же, но в другом порядуке
        crd_other.all_digs = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}  # совсем другое множество
        assert not (crd1 != crd2)
        assert crd1 != crd_other


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

    def test_str(self):

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
        # txt_exp = txt_exp + '\n\n'

        assert str(plr) == txt_exp, 'неверное формирование карты игрока'

    def test_eq(self):
        plr1 = HumanPlayer()              # plr1 и plr2 предполагаются одинаковыми
        plr2 = Player()
        plr1.brain = 'HI'
        plr2.brain = 'HI'
        plr_other = ComputerPlayer()      # plr_other - отличается
        plr_other.brain = 'AI'

        plr1.id = 77
        plr2.id = 77
        plr_other.id = 13

        plr1.name = 'Pedro'
        plr2.name = 'Pedro'
        plr_other.id = 'IBM'

        # *.status им присвоится одинаковый при инициализации

        crd12 = Cards()
        plr1.card = crd12
        plr2.card = crd12

        crd_other = Cards()
        while crd12 == crd_other:    # на всякий случай, чтобы crd_other точно отличалась от crd12
            crd_other = Cards()
        plr_other.card = crd_other

        assert (plr1 == plr2)
        assert not (plr1 == plr_other)

    def test_ne(self):

        plr1 = HumanPlayer()              # plr1 и plr2 предполагаются одинаковыми
        plr2 = Player()
        plr1.brain = 'HI'
        plr2.brain = 'HI'
        plr_other = ComputerPlayer()      # plr_other - отличается
        plr_other.brain = 'AI'

        plr1.id = 77
        plr2.id = 77
        plr_other.id = 13

        plr1.name = 'Pedro'
        plr2.name = 'Pedro'
        plr_other.id = 'IBM'

        # *.status им присвоится одинаковый при инициализации

        crd12 = Cards()
        plr1.card = crd12
        plr2.card = crd12

        crd_other = Cards()
        while crd12 == crd_other:    # на всякий случай, чтобы crd_other точно отличалась от crd12
            crd_other = Cards()
        plr_other.card = crd_other

        assert not (plr1 != plr2)
        assert (plr1 != plr_other)


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

    def test_create_chips(self):
        chip_lst = Chips.create_chips(1,3)
        # создается ли список нужной длины
        assert len(chip_lst) == 3
        # являются ли элементы списка представителями класса Chips
        assert isinstance(chip_lst[0], Chips)

    def test_eq(self):
        bochka1 = Chips(77)      # bochka1 и bochka2 предполагаются одинаковыми
        bochka2 = Chips(77)
        bochka_other = Chips(13)        # bochka_other - намеренно другая
        # статус при инициализации у всех одинаковый

        assert bochka1 == bochka2
        assert not (bochka1 == bochka_other)


        def test_ne(self):
            bochka1 = Chips(77)  # bochka1 и bochka2 предполагаются одинаковыми
            bochka2 = Chips(77)
            bochka_other = Chips(13)  # bochka_other - намеренно другая
            # статус при инициализации у всех одинаковый

            assert not (bochka1 != bochka2)
            assert bochka1 != bochka_other




