import random
import logging

# Добавление Лог файла
logging.basicConfig(level=logging.INFO, filename="Bo4onki_log.log",filemode="w")

# Ввод и проверка на валидность числа N.
while True:
    try:
        N = int(input("Введите число бочек N: "))
        logging.info(f" Number of Bo4ki == {N}")
        if N < 1:
            logging.error(" Error. Invalid 'N'", exc_info=True)
            raise ValueError
        break
    except ValueError as err:
         print("Ошибка, введите целое положительное число.")
         logging.error(" Error. Invalid 'N'", exc_info=True)

# Создание 2х списков: "Мешка" и "Стола". Заполнение Мешка бочонками.
Bag = []
Table = []
for i in range(1, N+1):
    Bag.append(i)
print(f"В Мешке: {Bag}")
logging.info(f" In the Bag: {Bag}")


# Выбираем случайный бочонок из Мешка и кладем его на Cтол.
while Bag != []:
    while True:
        try:
            Button = int(input("Введите 1, чтобы вытащить один бочонок из мешка or Введите 2, чтобы завершить программу: "))
            if Button not in range(1, 3):
                logging.error(" Error. Invalid 'N'", exc_info=True)
                raise ValueError
            break
        except ValueError:
            print("Ошибка")
            logging.error(" Error. Invalid 'N'", exc_info=True)
    if Button == 1:
        logging.info(f" Button pressed: {Button}")
        x = random.choice(Bag)
        Bag.remove(x)
        logging.info(f" Bo4ka #{x} removed from Bag")
        Table.append(x)
        print(f"{Bag} Мешок")
        logging.info(f" {Bag} left in Bag")
        print(f"{Table} бочонки на столе")
        logging.info(f" {Table} on Table")
    else:
        logging.info(f" Button pressed: {Button}. Program ended.")
        exit()
else:
    print("Мешочек пуст :(")
    logging.info(" Bag is empty :(")
