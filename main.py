import csv
from controls import jess_card,pete_card,last_statement_min,credit_column_name,debit_column_name,card_number_column_name, recent_sheet

def truncate(n):
  return int(n * 100) / 100

def get_credit_line():
  with open('./sheets/{}'.format(recent_sheet), newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    credit_line = 0
    for row in reader:
      if row[credit_column_name] != '' and float(row[credit_column_name]) > last_statement_min:
        return reader.line_num


def find_total(card_number):
  with open('./sheets/{}'.format(recent_sheet), newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    total = 0
    for row in reader:
      if row[card_number_column_name] == card_number and row[debit_column_name] != '' and reader.line_num < get_credit_line():
        total += float(row[debit_column_name])
      if row[card_number_column_name] == card_number and row[credit_column_name] != '' and reader.line_num < get_credit_line():
        total -= float(row[credit_column_name])

    return truncate(total)


pete_balance = find_total(pete_card)
jess_balance = find_total(jess_card)
total_balance = truncate(pete_balance + jess_balance)


print('''
Pete's Total: {}
Jess's Total: {}
Total Balance: {} 
'''.format(pete_balance,jess_balance, total_balance )
)



