# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа)
# для каждого предприятия.. Программа должна определить среднюю прибыль (за год для всех предприятий) и
# вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий,
# чья прибыль ниже среднего.

from collections import defaultdict, namedtuple
import random


def mean(data):
    if data.__len__() > 0:
        return sum(data) / data.__len__()


# Для тестирования
# names_company = ['Company1', 'Company2', 'Company3']
# Microsoft Google Apple
names_company = input("Введите наименования предприятий через пробел\n").split(' ')

print(f'Вы ввели {names_company.__len__()} предприятия\n')
Company = namedtuple('Company', 'profit_for_quarters, profit_mean')
companies = defaultdict(Company)
for n in names_company:
    # Для тестирования
    # fin_data = list(random.randint(1, 100) for _ in range(0, 4))
    fin_data = list(int(v) for v in input(f'Введите для предприятия {n} прибыль за 4е квартала через пробел\n').split(' '))

    companies[n] = Company(fin_data, mean(fin_data))

profit_mean_all = mean(list(companies[name].profit_mean for name in companies))
print(f'Средняя прибыль всех предприятий = {profit_mean_all}\n')

# Вывод на основе генераторов
down_profit_mean = list(name for name in companies if companies[name].profit_mean < profit_mean_all)
up_profit_mean = list(name for name in companies if companies[name].profit_mean > profit_mean_all)

print(f'Список предприятий с прибылью ниже среднего {down_profit_mean}')
print(f'Список предприятий с прибылью выше среднего {up_profit_mean}')

# Детальный вывод для каждого предприятия
# for name in companies:
#     if companies[name].profit_mean > profit_mean_all:
#         print(f'Предприятие {name} имеет среднюю прибыль {companies[name].profit_mean} и она выше среднего\n')
#
#     if companies[name].profit_mean < profit_mean_all:
#         print(f'Предприятие {name} имеет среднюю прибыль {companies[name].profit_mean} и она ниже среднего\n')

# Введите наименования предприятий через пробел
# Microsoft Google Apple
# Вы ввели 3 предприятия
#
# Введите для предприятия Microsoft прибыль за 4е квартала через пробел
# 10 11 12 10
# Введите для предприятия Google прибыль за 4е квартала через пробел
# 20 21 23 20
# Введите для предприятия Apple прибыль за 4е квартала через пробел
# 5 8 12 7
# Средняя прибыль всех предприятий = 13.25
#
# Список предприятий с прибылью ниже среднего ['Microsoft', 'Apple']
# Список предприятий с прибылью выше среднего ['Google']

