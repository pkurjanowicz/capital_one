import os
import platform
from os import listdir
from os.path import isfile, join

#these functions find the most recent file name in the directory sheets
def find_recent_file_name():
  list_of_dicts = []
  onlyfiles = [f for f in listdir('./sheets') if isfile(join('./sheets', f))]
  for i in range(len(onlyfiles)):
    if onlyfiles[i] != '.DS_Store':
      date = creation_date('./sheets/'+ onlyfiles[i])
      list_of_dicts.append({'name': onlyfiles[i], 'date': date})
  return sorted(list_of_dicts, key = lambda i: i['date'],reverse=True)[0]['name']

def creation_date(path_to_file):
    if platform.system() == 'Windows':
        return os.path.getctime(path_to_file)
    else:
        stat = os.stat(path_to_file)
        try:
            return stat.st_birthtime
        except AttributeError:
            return stat.st_mtime

jess_card = '0717'
pete_card = '9246'
last_statement_min = 2000 
credit_column_name = 'Credit'
debit_column_name = 'Debit'
card_number_column_name = 'Card No.'
recent_sheet = find_recent_file_name()