"""Игра угадай число
Компьютер сам загадывает и сам угадывает число менее чем за 20 попыток
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    array = [i for i in range(1, 101)] # создаем список возможных вариантов
    while True:
        predict_number = array[round(len(array)/2)] # угадываем число из середины списка возможных вариантов
        count += 1 # счетчик количества попыток
        
        if number == predict_number:
            break # выход из цикла если угадали
        elif number > predict_number:
            array = array[round(len(array)/2):] # если загаданное число больше, то оставляем правую часть списка возможных вариантов
        else:
            array = array[:round(len(array)/2)] # если загаданное число меньше, то оставляем левую часть списка возможных вариантов
            
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
