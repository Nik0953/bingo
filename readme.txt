
Домашнее задание к уроку 11:
ООП. Магические методы, утиная типизация, статические методы

    0. В проекте "Игра Лото" перейти на новую ветку для добавления нового функционала;
    (Для развития мышления можно попробовать сначала написать тест, а потом уже написать метод)
    1. Для каждого класса в программе добавить магический метод __str__;
           - да
    2. Для каждого класса сделать возможность сравнения 2-х объектов этого класса (a == b, a != b);
           - да
    3. Использовать любые подходящие магические методы для того чтобы сделать код более читаемым
       и удобным для переиспользования;
           - добавлен метод для генерации списка бочонков
           lotto_classes.py -строка 342:
                   @staticmethod
                   def create_chips(n1, n2):
           метод использован при создании бочонков:
           lotto_main.py -строка 16

    4. Покрыть новый код тестами;
           - да
    5. Создать pull request на объединение веток master и новой ветки с тестами,
       прислать ссылку на pull request как решение дз.


               Результаты тестирования:
=================
Testing started at 20:15 ...
Launching pytest with arguments /Users/nikolayagafonov/Desktop/Python progs/bingo/test_lotto_classes.py --no-header --no-summary -q in /Users/nikolayagafonov/Desktop/Python progs/bingo

============================= test session starts ==============================
collecting ... collected 13 items

test_lotto_classes.py::test_yes_or_no PASSED                             [  7%]
test_lotto_classes.py::TestCards::test_cross_out PASSED                  [ 15%]
test_lotto_classes.py::TestCards::test_eq PASSED                         [ 23%]
test_lotto_classes.py::TestCards::test_init PASSED                       [ 30%]
test_lotto_classes.py::TestCards::test_ne PASSED                         [ 38%]
test_lotto_classes.py::TestCards::test_str PASSED                        [ 46%]
test_lotto_classes.py::TestPlayer::test_init PASSED                      [ 53%]
test_lotto_classes.py::TestPlayer::test_str PASSED                       [ 61%]
test_lotto_classes.py::TestPlayer::test_eq PASSED                        [ 69%]
test_lotto_classes.py::TestPlayer::test_ne PASSED                        [ 76%]
test_lotto_classes.py::TestChips::test_init PASSED                       [ 84%]
test_lotto_classes.py::TestChips::test_create_chips PASSED               [ 92%]
test_lotto_classes.py::TestChips::test_eq PASSED                         [100%]

============================== 13 passed in 0.14s ==============================

Process finished with exit code 0


                 Тестирование в терминале:
====================
platform darwin -- Python 3.8.0, pytest-7.1.2, pluggy-1.0.0
rootdir: /Users/nikolayagafonov/Desktop/Python progs/bingo
plugins: cov-3.0.0
collected 13 items

test_lotto_classes.py .............                                                                                                                      [100%]

---------- coverage: platform darwin, python 3.8.0-final-0 -----------
Name                    Stmts   Miss  Cover
-------------------------------------------
lotto_classes.py          179     34    81%
test_lotto_classes.py     167      8    95%
-------------------------------------------
TOTAL                     346     42    88%


====================================================================== 13 passed in 0.17s ======================================================================
MacBook-Pro-Nikolay:bingo nikolayagafonov$




