# Write a Python program to find the largest k numbers from a given list of numbers.
# Input: [1, 2, 3, 4, 5, 5, 3, 6, 2]
# Output:
# [6]
# Input: [1, 2, 3, 4, 5, 5, 3, 6, 2]
# Output:
# [6, 5]
# Input: [1, 2, 3, 4, 5, 5, 3, 6, 2]
# Output:
# [6, 5, 5]
# Input: [1, 2, 3, 4, 5, 5, 3, 6, 2]
# Output:
# [6, 5, 5, 4]
# Input: [1, 2, 3, 4, 5, 5, 3, 6, 2]
# Output:
# [6, 5, 5, 4, 3]

def test(nums):
  nums.sort()


print(test([1, 2, 3, 4, 5, 5, 3, 6, 2]))