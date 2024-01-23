# Write a Python program to find the largest number where commas or periods are decimal points.
# Input:
# ['100', '102,1', '101.1']
# Output:
# 102.1

def test(nums):
    return max(float(num.replace(',', '.')) for num in nums)
    #float returns a floating point number from a string or number

print(test(['100', '102,1', '101.1']))