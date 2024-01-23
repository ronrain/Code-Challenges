# Write a Python program to find x that minimizes the mean squared deviation from a given list of numbers.
# Input:
# [4, -5, 17, -9, 14, 108, -9]
# Output:
# 17.142857142857142
# Input:
# [12, -2, 14, 3, -15, 10, -45, 3, 30]
# Output:
# 1.1111111111111112


def test(nums):
  return sum(nums)/len(nums)

print(test([12, -2, 14, 3, -15, 10, -45, 3, 30]))