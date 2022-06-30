""" Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
(т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести
наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль
ниже среднего.
"""

import collections

company = collections.namedtuple('company', ['name', 'q1', 'q2', 'q3', 'q4', 'y'])

company_collection = []

lot_company = int(input("Введите количество компаний: "))

total_profit = 0

for i in range(lot_company):
    name = input(f"Введите название {i+1}-ого предприятия: ")
    q1 = int(input("Прибыль за 1 квартал: "))
    q2 = int(input("Прибыль за 2 квартал: "))
    q3 = int(input("Прибыль за 3 квартал: "))
    q4 = int(input("Прибыль за 4 квартал: "))
    year_profit = q1 + q2 + q3 + q4
    total_profit += year_profit
    company_collection.append(company(name=name, q1=q1, q2=q2, q3=q3, q4=q4, y=year_profit))

total_avg = total_profit / lot_company

print(f"Предприятия с прибылью выше средней годовой прибыли: {total_avg}: ")
for company in company_collection:
    if company.y >= total_avg:
        print(f" Предприятие {company.name} с прибылью {company.y}")

print(f"Предприятия с прибылью ниже средней годовой прибыли: {total_avg}: ")
for company in company_collection:
    if company.y < total_avg:
        print(f" Предприятие {company.name} с прибылью {company.y}")

