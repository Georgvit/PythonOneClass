# Функция сохранения телефонного справочника в формате на выбор пользователя
def save_file(book_list):
    save_book = input('Введите имя сохраняемого файла: ')
    with open(save_book, 'w+', encoding='utf=8') as file:
        for key, volume in book_list.items():
            text_book = key + volume + '\n'
            file.write(text_book)
