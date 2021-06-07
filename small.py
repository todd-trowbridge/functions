# 1
def madlib(name, subject):
  return f"{name}'s favorite subject in school is {subject}."

# print(madlib('Todd','Python'))

# 2
def c_to_f(user_temp):
  return int(user_temp * 9 / 5) + 32

# print(c_to_f(0))

# 3
def f_to_c(user_temp):
  return int((user_temp -32) * 5 / 9)

# print(f_to_c(100))

# 4
def is_even(num):
  if num % 2 == 0: return True
  else: return False

# print(is_even(11))

# 5
def is_odd(num):
  if num % 2 == 1: return True
  else: return False

# print(is_odd(11))

list_of_numbers = [0,1,2,3,4,5,6,7,8,9,1001,1002]

# 6
def only_evens(list):
  list_of_even_numbers = []
  for num in list:
    if num % 2 == 0 and num != 0: list_of_even_numbers.append(num)
  return list_of_even_numbers

# print(only_evens(list_of_numbers))

# 7
def only_odds(list):
  list_of_even_numbers = []
  for num in list:
    if num % 2 == 1 and num != 0: list_of_even_numbers.append(num)
  return list_of_even_numbers

# print(only_odds(list_of_numbers))