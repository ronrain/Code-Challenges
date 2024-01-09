# Write a Python program that accepts an integer and determines whether it is greater than 4^4 and which is 4 mod 34.
# Input:
# 922
# Output:
# True
# Input:
# 914
# Output:
# False
# Input:
# 854
# Output:
# True
# Input:
# 854
# Output:
# True

def pra_puz(nums):
  return nums > 4**4 and nums % 34 == 4
print(pra_puz(854))