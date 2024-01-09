# . Write a Python program that accepts a list of integers and calculates the length and the fifth element. Return true if the length of the list is 8 and the fifth element occurs thrice in the said list.
# Input:
# [19, 19, 15, 5, 5, 5, 1, 2]
# Output:
# True
# Input:
# [19, 15, 5, 7, 5, 5, 2]
# Output:
# False
# Input:
# [11, 12, 14, 13, 14, 13, 15, 14]
# Output:
# True
# Input:
# [19, 15, 11, 7, 5, 6, 2]
# Output:
# False

def prac_puzz(nums):
  return len(nums) == 8 and nums.count(nums[4]) == 3
print(prac_puzz([19, 19, 15, 5, 5, 5, 1, 2]))#True
print(prac_puzz([19, 15, 5, 7, 5, 5, 2]))#False
print(prac_puzz([11, 12, 10, 13, 14, 13, 15, 14]))#False
