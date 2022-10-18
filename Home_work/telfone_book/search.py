
# Функция поиска абонента в справочнике
def search_name(phonebook):
    name = input('Введите имя или номер абонента: ')
    for key, volume in phonebook.items():
        if name in key:
            print(key, volume)
