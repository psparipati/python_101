# -*- coding: utf-8 -*-
"""Number Ranking.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ILTq-rLcYg6M1IY87IDUHCqyHA5U8BiF
"""

def get_bin_name(input_price):
  A = 0.949
  B = 1.232
  C = 1.63
  D = 2.821
  E = 4.165
  bin_name = ['Very Low', 'Low', 'High', 'Very High']
  if (input_price <= B):
    return bin_name[0]
  elif ((input_price > B) and (input_price <= C)):
    return bin_name[1]
  elif ((input_price > C) and (input_price <= D)):
    return bin_name[2]
  elif (input_price > D):
    return bin_name[3]

# Test Cases 1 to 4
# Very Low, Low, High or Very High?
print(get_bin_name(2.45))
print(get_bin_name(1.2))
print(get_bin_name(5.0))
print(get_bin_name(0.8))