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
    min_num = 1 # минимальное возможное загаданное число
    max_num = 100 # максимально возможное загаданное число
    while True:
        count += 1
        predict_number = np.random.randint(min_num, max_num + 1)  # предполагаемое число
        
        if count > 20:
            break # выход из цикла в случае перебора попыток
        
        if number == predict_number:
            break  # выход из цикла если угадали
        elif number > predict_number:
            min_num = predict_number + 1 # если загаданное число больше, то обновляем минимально возможный вариант
        else:
            max_num = predict_number - 1 # если загаданное число меньше, то обновляем максимально возможный вариант
            
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
