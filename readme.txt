
Домашнее задание к уроку 10:
Тестирование классов с unittest, pytest

Сделал тесты и с unittest и с pytest
не тестировал только метод HumanPlayer.move,
    так как там сплошь консольный ввод-вывод.
=================================================
Результаты тестирования:


Testing started at 00:15 ...
Launching pytest with arguments /Users/nikolayagafonov/Desktop/Python progs/bingo/test_lotto_classes.py --no-header --no-summary -q in /Users/nikolayagafonov/Desktop/Python progs/bingo

============================= test session starts ==============================
collecting ... collected 6 items

test_lotto_classes.py::test_yes_or_no PASSED                             [ 16%]
test_lotto_classes.py::TestCards::test_card_as_txt PASSED                [ 33%]
test_lotto_classes.py::TestCards::test_cross_out PASSED                  [ 50%]
test_lotto_classes.py::TestCards::test_init PASSED                       [ 66%]
test_lotto_classes.py::TestPlayer::test_init PASSED                      [ 83%]
test_lotto_classes.py::TestChips::test_init PASSED                       [100%]

============================== 6 passed in 0.05s ===============================



MacBook-Pro-Nikolay:bingo nikolayagafonov$ pytest --cov
===================================================================== test session starts ======================================================================
platform darwin -- Python 3.8.0, pytest-7.1.2, pluggy-1.0.0
rootdir: /Users/nikolayagafonov/Desktop/Python progs/bingo
plugins: cov-3.0.0
collected 6 items

test_lotto_classes.py ......                                                                                                                             [100%]

---------- coverage: platform darwin, python 3.8.0-final-0 -----------
Name                    Stmts   Miss  Cover
-------------------------------------------
lotto_classes.py          127     36    72%
test_lotto_classes.py      90     19    79%
-------------------------------------------
TOTAL                     217     55    75%


====================================================================== 6 passed in 0.14s =======================================================================
MacBook-Pro-Nikolay:bingo nikolayagafonov$




