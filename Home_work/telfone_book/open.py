# Функция открытия файла
def open_file():
    openen = input('Введите адрес файла: ')
    with open(openen, 'r', encoding='utf=8') as file:
        text = file.readlines()

    if openen[-3:] == 'txt':
        return text
    elif openen[-3:] == 'csv':
        return text
    else:
        print('Неверный формат файла!')
