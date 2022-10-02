def binary_seach(list, item):
    # Границы части списка где ведется поиск
    low = 0
    high = len(list) - 1

    while low <= high:
        # Проверяем средний элемент
        mid = int((low + high) / 2)
        guess = list[mid]

        # Проверка найденного значения
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = [1, 2, 4, 5, 7, 8, 10, 11, 13, 45]

print(f'Индекс искомого элемента: {binary_seach(my_list, 10)}')
