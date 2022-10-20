# Добавления абонента в справочник
def add_subscriber(book):
    subscriber = input('Введите имя обонента: ') + ' '
    numbers = input('Введите имя обонента: ')
    book[subscriber] = numbers
    for key, volume in book.items():
        print(key, volume)
    return book

