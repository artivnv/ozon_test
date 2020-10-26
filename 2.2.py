import csv

dic = []
costs = []
with open ('product.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f, delimiter = ',')
    for row in reader:
        name_quantity_list = {row['good_name']: int(row['quantity'])}
        dic.append(name_quantity_list)
        costs_list = {row['good_name']: int(row['cost'])}
        costs.append(costs_list)

resultdic = {}                                 # результирующий словарь
for dictionary in dic:                         # пробегаем по списку словарей
  for key in dictionary:                       # пробегаем по ключам словаря
        try:
            resultdic[key] += dictionary[key]  # складываем значения
        except KeyError:                       # если ключа еще нет - создаем
            resultdic[key] = dictionary[key]

resultcosts = {}
for dictionary in costs:
    for key in dictionary:
        resultcosts[key] = dictionary[key]

count = {k: resultdic[k]*resultcosts[k] for k in resultdic}

for k, v in resultdic.items():
    print(k, v, count[k])

