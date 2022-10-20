# Функция открытия файла
# def open_file():
#     openen = input('Введите адрес файла: ')
#     with open(openen, 'r', encoding='utf=8') as file:
#         text = file.readlines()
#
#     if openen[-3:] == 'txt':
#         return text
#     elif openen[-3:] == 'csv':
#         return text
#     elif openen[-3:] == 'son':
#         return text
#     else:
#         print('Неверный формат файла!')

import csv
import json
from pathlib import Path


def open_file() -> list:
    employee = []

    with open(Path.cwd() / 'database.csv', 'r', encoding='utf-8') as fin:
        csv_reader = csv.reader(fin)
        for row in csv_reader:
            temp = {}
            temp["id"] = int(row[0])
            temp["last_name"] = row[1]
            temp["first_name"] = row[2]
            temp["position"] = row[3]
            temp["phone_number"] = row[4]
            temp["salary"] = float(row[5])
        employee.append(temp)
        print(employee)
        return employee

# def open_file() -> list:
#     employee = []
#     with open(Path.cwd() / 'database02.json', 'r', encoding='utf-8') as fin:
#         for line in fin:
#             temp = json.loads(line.strip())
#     employee.append(temp)
#     print(employee)
#     return employee