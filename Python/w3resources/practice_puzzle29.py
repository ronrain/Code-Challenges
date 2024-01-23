# Write a Python program to find the indices of two numbers that sum to 0 in a given list of numbers.
# Input:
# [1, -4, 6, 7, 4]
# Output:
# [4, 1]
# Input:
# [1232, -20352, 12547, 12440, 741, 341, 525, 20352, 91, 20]
# Output:
# [1, 7]

def test(nums):
  numbers = set(nums)
  for num in numbers:
    if -num in numbers:
      return [nums.index(num), nums.index(-num)]

print(test([1232, -20352, 12547, 12440, 741, 341, 525, 20352, 91, 20]))
