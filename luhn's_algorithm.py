# -*- coding: utf-8 -*-
"""Luhn's Algorithm.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1dZeSTlKzMHRonR86rXHqDcpZ0VdRURjq
"""

#@title Luhn's Algorithm Version 1

def is_credit_card(credit):
  #Step 1
  credit = str(credit)
  credit_evaluator = []
  for j in credit:
    j = int(j)
    credit_evaluator.append(j)
  #Step 2
  c = 0
  for i in range(len(credit_evaluator)):
    if (c % 2):
      credit_evaluator[i] = credit_evaluator[i] * 2
    c = c + 1
  #Step 3
  d = 0
  for y in range(len(credit_evaluator)):
    if ((d % 2) and (credit_evaluator[y] >= 10)):
      credit_evaluator[y] = credit_evaluator[y] - 10
      credit_evaluator[y] = credit_evaluator[y] + 1
    d = d + 1
  #Step 4
  sum = 0
  for g in range(len(credit_evaluator)):
    a = credit_evaluator[g]
    sum = sum + a
  #Extra Security
  if ((sum % 10) == 0):
    help = credit + ' is a valid credit card number, but how did you get this credit card? ...'
  elif ((sum % 10) != 0):
    help = 'Draining money from bank account because '+ credit +' is not valid...'
  return help

print(is_credit_card(4685135647))
print()
print(is_credit_card(468513564))

#@title Luhn's Algorithm Version 2

def is_credit_card(credit):
  #Step 1
  credit = str(credit)
  credit_evaluator = []
  for j in credit:
    j = int(j)
    credit_evaluator.append(j)
  #Step 2
  c = 0
  for i in range(len(credit_evaluator)):
    if (c % 2):
      credit_evaluator[i] = credit_evaluator[i] * 2
    c = c + 1
  #Step 3
  d = 0
  for y in range(len(credit_evaluator)):
    if (credit_evaluator[y] >= 10):
      credit_evaluator[y] = credit_evaluator[y] - 9
    d = d + 1
  #Step 4 + Extra Stuff
  if ((sum(credit_evaluator) % 10) == 0):
    return credit +' is a valid credit card number.'
  else:
    return credit +' is not valid...'

def is_visa_or_master(credit):
  credit = str(credit)
  credit_evaluator = []
  for j in credit:
    j = int(j)
    credit_evaluator.append(j)
  if (is_credit_card(credit) == credit +' is a valid credit card number.'):
    if (((len(credit) == 16) or (len(credit) == 13)) and (credit_evaluator[0] == 4)):
      return credit+' is a valid Visa number.'
    elif ((len(credit) == 16) and (credit_evaluator[0] == 5)):
      return credit+' is a valid Mastercard number'
    else:
      return credit+' is not a valid number for any parameter...'
  else:
    return credit+' is not valid at all...'

print(is_visa_or_master(4685135647))
print()
print(is_credit_card(468513564))

#@title Luhn's Algorithm Version 3

def is_credit(card_number):
  card_number = str(card_number)
  credit_evaluator = [int(j) for j in card_number]
  c = 0
  for i in range(len(credit_evaluator)):
    if (c % 2 != 0):
      credit_evaluator[i] = credit_evaluator[i] * 2
    c = c + 1
  for y in range(len(credit_evaluator)):
    if (credit_evaluator[y] >= 10):
      credit_evaluator[y] = credit_evaluator[y] - 9
  if ((sum(credit_evaluator) % 10) == 0):
    return True
  else:
    return False

def is_visa(card_number):
  card_number = str(card_number)
  credit_evaluator = [int(j) for j in card_number]
  if ((len(card_number) == 16) or (len(card_number) == 13) and (credit_evaluator[0] == 4)):
    if (is_credit(card_number) == True):
      return True
    else:
      return False
  else:
    return False

def is_mastercard(card_number):
  card_number = str(card_number)
  credit_evaluator = [int(j) for j in card_number]
  if ((len(card_number) == 16) and (credit_evaluator[0] == 5) and (credit_evaluator[1] == range(6))):
    if (is_credit(card_number) == True):
      return True
    else:
      return False
  else:
    return False

def answer():
  print("is_credit('6011000000000004'):", is_credit("6011000000000004"))
  print("is_credit('79927398713'):", is_credit("79927398713"))
  print("is_credit('30000000000004'):" ,is_credit("30000000000004"))
  print("is_credit('6911600873502604'):"  ,is_credit("6911600873502604"))
  print("is_credit('1234567890'):",  is_credit("1234567890"))

  print("is_visa('6011000000000004'):",is_visa("6011000000000004"))
  print("is_visa('79927398713'):", is_visa("79927398713"))
  print("is_visa('30000000000004'):" ,is_visa("30000000000004"))
  print("is_visa('6911600873502604'):"  ,is_visa("6911600873502604"))
  print("is_visa('1234567890'):",  is_visa("1234567890"))

  print("is_mastercard('6011000000000004'):",is_mastercard("6011000000000004"))
  print("is_mastercard('79927398713'):", is_mastercard("79927398713"))
  print("is_mastercard('30000000000004'):" ,is_mastercard("30000000000004"))
  print("is_mastercard('6911600873502604'):"  ,is_mastercard("6911600873502604"))
  print("is_mastercard('1234567890'):",  is_mastercard("1234567890"))

answer()

#@title Luhn's Algorithm Version 4

def is_credit(card_number):
  card_number = str(card_number)
  credit_evaluator = [int(j) for j in card_number]
  c = 0
  sum = 0
  for i in range(len(credit_evaluator)):
    if c % 2 == 0:
        sum += i
    elif i >= 5:
        sum += i * 2 - 9
    else:
        sum += i * 2
  if ((sum % 10) == 0):
    return True
  else:
    return False

def is_visa(card_number):
  card_number = str(card_number)
  credit_evaluator = [int(j) for j in card_number]
  if ((len(card_number) == 16) or (len(card_number) == 13) and (credit_evaluator[0] == 4)):
    if (is_credit(card_number) == True):
      return True
    else:
      return False
  else:
    return False

def is_mastercard(card_number):
  card_number = str(card_number)
  credit_evaluator = [int(j) for j in card_number]
  if ((len(card_number) == 16) and (credit_evaluator[0] == 5) and (credit_evaluator[1] == range(6))):
    if (is_credit(card_number) == True):
      return True
    else:
      return False
  else:
    return False

def answer():
  print("is_credit('6011000000000004'):", is_credit("6011000000000004"))
  print("is_credit('79927398713'):", is_credit("79927398713"))
  print("is_credit('30000000000004'):" ,is_credit("30000000000004"))
  print("is_credit('6911600873502604'):"  ,is_credit("6911600873502604"))
  print("is_credit('1234567890'):",  is_credit("1234567890"))

  print("is_visa('6011000000000004'):",is_visa("6011000000000004"))
  print("is_visa('79927398713'):", is_visa("79927398713"))
  print("is_visa('30000000000004'):" ,is_visa("30000000000004"))
  print("is_visa('6911600873502604'):"  ,is_visa("6911600873502604"))
  print("is_visa('1234567890'):",  is_visa("1234567890"))

  print("is_mastercard('6011000000000004'):",is_mastercard("6011000000000004"))
  print("is_mastercard('79927398713'):", is_mastercard("79927398713"))
  print("is_mastercard('30000000000004'):" ,is_mastercard("30000000000004"))
  print("is_mastercard('6911600873502604'):"  ,is_mastercard("6911600873502604"))
  print("is_mastercard('1234567890'):",  is_mastercard("1234567890"))

answer()

#@title Luhn's Algorithm Version 5

def is_credit(card_number):
  card_number = str(card_number)
  credit_evaluator = [int(j) for j in card_number]
  sum = 0
  credit_evaluator.reverse()
  for i in range(len(credit_evaluator)):
    c = credit_evaluator[i]
    if i % 2 == 0:
        sum += c
    elif c >= 5:
        sum += c * 2 - 9
    else:
        sum += c * 2
  credit_evaluator.reverse()
  if ((sum % 10) == 0):
    return True
  else:
    return False

def is_visa(card_number):
  card_number = str(card_number)
  credit_evaluator = [int(j) for j in card_number]
  if ((len(card_number) == 16) or (len(card_number) == 13) and (credit_evaluator[0] == 4)):
    if (is_credit(card_number) == True):
      return True
    else:
      return False
  else:
    return False

def is_mastercard(card_number):
  card_number = str(card_number)
  credit_evaluator = [int(j) for j in card_number]
  if ((len(card_number) == 16) and (credit_evaluator[0] == 5) and (credit_evaluator[1] == range(6))):
    if (is_credit(card_number) == True):
      return True
    else:
      return False
  else:
    return False

def answer():
  print("is_credit('6011000000000004'):", is_credit("6011000000000004"))
  print("is_credit('79927398713'):", is_credit("79927398713"))
  print("is_credit('30000000000004'):" ,is_credit("30000000000004"))
  print("is_credit('6911600873502604'):"  ,is_credit("6911600873502604"))
  print("is_credit('1234567890'):",  is_credit("1234567890"))

  print("is_visa('6011000000000004'):",is_visa("6011000000000004"))
  print("is_visa('79927398713'):", is_visa("79927398713"))
  print("is_visa('30000000000004'):" ,is_visa("30000000000004"))
  print("is_visa('6911600873502604'):"  ,is_visa("6911600873502604"))
  print("is_visa('1234567890'):",  is_visa("1234567890"))

  print("is_mastercard('6011000000000004'):",is_mastercard("6011000000000004"))
  print("is_mastercard('79927398713'):", is_mastercard("79927398713"))
  print("is_mastercard('30000000000004'):" ,is_mastercard("30000000000004"))
  print("is_mastercard('6911600873502604'):"  ,is_mastercard("6911600873502604"))
  print("is_mastercard('1234567890'):",  is_mastercard("1234567890"))

#answer()
a = '''
is_credit('6011000000000004') True
is_credit('79927398713') True
is_credit('30000000000004') True
is_credit('6911600873502604') False
is_credit('1234567890') False
is_visa('6011000000000004') False
is_visa('79927398713') False
is_visa('30000000000004') False
is_visa('6911600873502604') False
is_visa('1234567890') False
is_mastercard('6011000000000004') False
is_mastercard('79927398713') False
is_mastercard('30000000000004') False
is_mastercard('6911600873502604') False
is_mastercard('1234567890') False
'''

if ((answer()) != a):
  print(False)
else:
  print(True)

#@title Luhn's Algorithm Version 6

def is_credit(card_number):
  if (card_number.isnumeric() == True):
    card_number = str(card_number)
    credit_evaluator = [int(j) for j in card_number]
    sum = 0
    credit_evaluator.reverse()
    for i in range(len(credit_evaluator)):
      c = credit_evaluator[i]
      if i % 2 == 0:
        sum += c
      elif c >= 5:
        sum += c * 2 - 9
      else:
        sum += c * 2
    credit_evaluator.reverse()
    if ((sum % 10) == 0):
      return True
    else:
      return False
  else:
    return False

def is_visa(card_number):
  card_number = str(card_number)
  credit_evaluator = [int(j) for j in card_number]
  if ((len(card_number) == 16) or (len(card_number) == 13) and (credit_evaluator[0] == 4)):
    if (is_credit(card_number) == True):
      return True
    else:
      return False
  else:
    return False

def is_mastercard(card_number):
  card_number = str(card_number)
  credit_evaluator = [int(j) for j in card_number]
  if ((len(card_number) == 16) and (credit_evaluator[0] == 5) and (credit_evaluator[1] == range(1, 6))):
    if (is_credit(card_number) == True):
      return True
    else:
      return False
  else:
    return False

def main():
  print('\n==>1. Basic test cases (positive)')
  print("is_credit('6011000000000004')", is_credit("6011000000000004"))
  print("is_credit('79927398713')", is_credit("79927398713"))
  print("is_credit('30000000000004')" ,is_credit("30000000000004"))
  print("is_credit('6911600873502604')"  ,is_credit("6911600873502604"))
  print("is_credit('1234567890')",  is_credit("1234567890"))

  print('\n==>2. Negative Test Case')
  print(("is_credit('abcdefg')"), is_credit("abcdefg"))

  print('\n==>3. Checking whether a card is valid visa card or not')
  print("is_visa('6011000000000004')",is_visa("6011000000000004"))
  print("is_visa('79927398713')", is_visa("79927398713"))
  print("is_visa('4012888888881881')" ,is_visa("4012888888881881"))
  print("is_visa('4111111111111111')",  is_visa("4111111111111111"))

  print('\n==>4. Checking whether a card is valid Master card or not')
  print("is_mastercard('5555555555554444')",is_mastercard("5555555555554444"))
  print("is_mastercard('79927398713')", is_mastercard("79927398713"))
  print("is_mastercard('5105105105105100')" ,is_mastercard("5105105105105100"))
  print("is_mastercard('6911600873502604')"  ,is_mastercard("6911600873502604"))

main()