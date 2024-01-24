# Write a Python program to find the sum of the numbers in a given list among the first k with more than 2 digits.
# Input: [4, 5, 17, 9, 14, 108, -9, 12, 76]
# Value of K: 4
# Output:
# 0
# Input: [4, 5, 17, 9, 14, 108, -9, 12, 76]
# Value of K: 6
# Output:
# 108
# Input: [114, 215, -117, 119, 14, 108, -9, 12, 76]
# Value of K: 5
# Output:
# 331
# Input: [114, 215, -117, 119, 14, 108, -9, 12, 76]
# Value of K: 1
# Output:
# 114

def test(nums, k):
  numbers = []
  for num in nums[:k]:
    if num >= 100 or num <= -100:
      numbers.append(num)
  return sum(numbers)

print(test([4, 5, 17, 9, 14, 108, -9, 12, 76], 6))