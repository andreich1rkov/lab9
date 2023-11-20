import random
import logging

# Добавление Лог файла
logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="w")

# Ввод и проверка на валидность числа N.
while True:
    try:
        N = int(input("Введите целое положительное число N: "))
        if N < 1:
            raise ValueError
        break
    except ValueError:
         print("Ошибка")

# Создание 2х списков: "Мешка" и "Стола". Заполнение Мешка бочонками.
Bag = []
Table = []
for i in range(1, N+1):
    Bag.append(i)
print(Bag)

# Выбираем случайный бочонок из Мешка и кладем его на Cтол.
while Bag != []:
    while True:
        try:
            Button = int(input("Введите 1, чтобы вытащить один бочонок из мешка or Введите 2, чтобы завершить программу: "))
            if Button not in range(1, 3):
                raise ValueError
            break
        except ValueError:
            print("Ошибка")
    if Button == 1:
        x = random.choice(Bag)
        Bag.remove(x)
        Table.append(x)
        print(f"{Bag} Мешок")
        print(f"{Table} бочонки на столе")
    else:
        exit()
else:
    print("Мешочек пуст :(")
