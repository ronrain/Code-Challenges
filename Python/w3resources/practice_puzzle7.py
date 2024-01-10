# Write a Python program to check a given list of integers where the sum of the first i integers is i.
# Input:
# [0, 1, 2, 3, 4, 5]
# Output:
# False
# Input:
# [1, 1, 1, 1, 1, 1]
# Output:
# True
# Input:
# [2, 2, 2, 2, 2]
# Output:
# False

def test(li, i):
  return sum(li[:i]) == i
print(test([2, 2, 2, 2, 2],2))