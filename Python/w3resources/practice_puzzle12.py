# Write a Python program to check whether the given strings are palindromes or not. Return True otherwise False.
# Input:
# ['palindrome', 'madamimadam', '', 'foo', 'eyes']
# Output:
# [False, True, True, False, False]

def test(str):
  return [s == s[::-1] for s in str]
print(test(['palindrome', 'madamimadam', '', 'foo', 'eyes']))
