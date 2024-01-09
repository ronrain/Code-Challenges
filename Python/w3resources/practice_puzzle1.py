# Write a Python program to find a list of integers with exactly two occurrences of nineteen and at least three occurrences of five. Return True otherwise False.
# Input:
# [19, 19, 15, 5, 3, 5, 5, 2]
# Output:
# True
# Input: 
# [19, 15, 15, 5, 3, 3, 5, 2]
# Output:
# False
# Input:
# [19, 19, 5, 5, 5, 5, 5]
# Output:
# True

def prac_puzz(nums):
  return nums.count(19) == 2 and nums.count(5) == 3
print(prac_puzz([19,19,15,5,3,5,5,2])) #True
print(prac_puzz([19,15,15,5,3,3,5,2])) #false