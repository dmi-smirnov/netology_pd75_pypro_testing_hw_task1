from pprint import pprint

import input_data


def task1(geo_logs: list):
  ru_geo_logs = []
  for d in geo_logs:
    if list(d.values())[0][1] == 'Россия':
      ru_geo_logs.append(d)

  return ru_geo_logs

def task2(ids: dict):
  ids_uniq = set()
  for ids_list in ids.values():
    ids_uniq |= set(ids_list)

  return list(ids_uniq)

def task3(queries: list):
  queries_word_amounts = []

  for q in queries:
    queries_word_amounts.append(len(q.split()))

  queries_amount = len(queries)

  queries_word_amounts_percents = dict()

  for querie_word_amount in set(queries_word_amounts):
    count = queries_word_amounts.count(querie_word_amount)
    percent = round(count * 100 / queries_amount)
    queries_word_amounts_percents[querie_word_amount] = percent
  
  return queries_word_amounts_percents

def main():
  # task1
  print('task1:')
  pprint(task1(input_data.task1))
  print()

  # task2
  print(f'task2:\n{task2(input_data.task2)}\n')

  # task3
  print('task3:')
  print('\n'.join(f'слов {amount}: {percent}%'
    for amount, percent in task3(input_data.task3).items()))

main()