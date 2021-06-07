def add(num1, num2):
  return num1 + num2

def add5(num):
  return add(num, 5)

user_num = int(input('What number would you like to add 5 to? '))

print(add5(user_num))