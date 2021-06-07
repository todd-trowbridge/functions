list_of_numbers = [0,1,2,3,4,5,6,7,8,9,1000,-1000]
list_of_strings = ['1','22','333','4444','55555','666666']

# 1

def smallest(list):
  smallest_num = list.pop()
  for num in list:
    if num < smallest_num:
      smallest_num = num
  return smallest_num

# print(smallest(list_of_numbers))

# 2

def largest(list):
  largest_num = list.pop()
  for num in list:
    if num > largest_num:
      largest_num = num
  return largest_num
  
# print(largest(list_of_numbers))

# 3

def shortest_string(list):
  shortest_string = list.pop()
  for string in list:
    if len(string) < len(shortest_string):
      shortest_string = string
  return shortest_string

# print(shortest_string(list_of_strings))

def longest_string(list):
  longest_string = list.pop()
  for string in list:
    if len(string) > len(longest_string):
      longest_string = string
  return longest_string

# print(longest_string(list_of_strings))