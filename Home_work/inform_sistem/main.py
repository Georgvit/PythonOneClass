# Создать информационную систему позволяющую работать
# с сотрудниками некой компании \ студентами вуза \ учениками школы
from typing import TextIO


#
# def write_csv(employees: list):
#     with open(Path.cwd() / 'database.csv', 'w', encoding='utf-8') as fout:
#         csv_writer = csv.writer(fout)
#
#     for employee in employees:
#         csv_writer.writerow(employee.values())
#
#
# def write_json(employees: list):
#     with open(Path.cwd() / 'database02.json', 'w', encoding='utf-8') as fout:
#         for employee in employees:
#         fout.write(json.dumps(employee) + '\n')
#
# for employee in employees:
#     if employee['id'] == id:
#         return employee
#
# def find_employees_by_salary_range(employees: list) -> list:
#     result = []
#     lo, hi = get_salary_range()
#     for employee in employees:
#         if lo <= employee["salary"] <= hi:
#             result.append(employee)
#     return result

# Запуск программы
import view as vid
import controller as con

con.step(vid.show_menu())