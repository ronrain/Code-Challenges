# Write a Python program to create a string consisting of non-negative integers up to n inclusive.
# Input:
# 4
# Output:
# 0 1 2 3 4
# Input:
# 15
# Output:
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15

def test(num):
  return [n for n in range(num +1)]
print(test(15))
