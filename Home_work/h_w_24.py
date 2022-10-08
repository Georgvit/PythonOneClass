# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах

def encrypted(text):
    # Создаем и открываем файлы для записи оригинального текста
    o_text = open('original_text.txt', 'w+')

    # Записываем данные в файл и закрываем их
    o_text.write(text)
    o_text.close()

    # Открываем файлы для чтения данных
    with open('original_text.txt', 'r') as file:
        list_text = str(file.readlines()).strip("['']")

    # Шифруем текст
    new_text = ''
    count = 1
    list_text += ' '

    for i in range(len(list_text) - 1):

        if list_text[i] == list_text[i + 1]:
            count += 1
        else:
            new_text += str(count) + list_text[i]
            count = 1

    # Записываем результат в файл
    e_text = open('encrypted_text.txt', 'w+')
    e_text.write(new_text)
    e_text.close()
    with open('encrypted_text.txt', 'r') as file:
        print(file.readlines())


def decoding():
    # Открываем файлы для чтения данных
    with open('encrypted_text.txt', 'r') as file:
        list_text = str(file.readlines()).strip("['']")

    # Расшифровка текста
    new_text = ''
    for i in range(0, len(list_text) - 1, 2):
        new_text += list_text[i + 1] * int(list_text[i])

    # Записываем результат в файл
    e_text = open('decoding_text.txt', 'w+')
    e_text.write(new_text)
    e_text.close()
    with open('decoding_text.txt', 'r') as file:
        print(file.readlines())


encrypted('AAAAANNNNDRRTYYEUUUUUUCCC')
decoding()
