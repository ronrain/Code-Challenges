#  Write a Python program to find the length of a given list of non-empty strings.
# Input:
# ['cat', 'car', 'fear', 'center']
# Output:
# [3, 3, 4, 6]
# Input:
# ['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']
# Output:
# [3, 3, 7, 5, 2, 4, 0]

def test(str):
  return[len(s) for s in str]
print(test(['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']
))
