
# Avito тестовое задание

[![N|Solid](https://www.freepngimg.com/thumb/tree/35945-9-fir-tree-thumb.png)](https://nodesource.com/products/nsolid)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

# Задание 2

Автомат принимает накопительные скидочные карты и при своем расчете учитывает количество баллов, по которому начисляет процент скидки: От 0 до 100 баллов - скидка 1% От 100 до 200 баллов - скидка 3 % От 200 до 500 баллов - скидка 5% От 500 баллов - скидка 10% Задание: Составить такой набор тестовых данных для автомата, при котором мы гарантированно будем знать, что в соответствии со своими накопленными баллами покупатель получит верную скидку.
(Мне кажется неправильно заданы баллы, т. к. с 0 баллов не дают скидку:))

Допустим мы хотим купить на сумму 456$
Ожидаемая сумма скидок такова (с правильными баллами):
- от 1 до 99 = скидка 1% = 4,56$
- от 100 до 199 = скидка 3% = 13,68$
- от 200 до 499 = скидка 5% = 22,8$
- от 500 = скидка 10% = 45,6$

Тестовые данные (баллы):
- 0(не должна давать скидку)
- Для проверки 1% скидки = 1, 2, 98, 99 - ожидаемый результат = скидка 4,56$
- Для проверки 3% скидки = 100, 101, 198, 199 - ожидаемый результат = скидка 13,68$
- Для проверки 5% скидки = 200, 201, 498, 499 - ожидаемый результат = скидка 22,8$
- Для проверки 10% скидки = 500, 501, 700, 1000, 5000, 10000 - ожидаемый результат = скидка 45,6$

# Комментарий к первой задаче

Программа находится в файле test.py