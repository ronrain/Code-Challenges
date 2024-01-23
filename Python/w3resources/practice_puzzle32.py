# Write a Python program to rescale and shift numbers in a given list, so that they cover the range [0, 1].
# Input:
# [18.5, 17.0, 18.0, 19.0, 18.0]
# Output:
# [0.75, 0.0, 0.5, 1.0, 0.5]
# Input:
# [13.0, 17.0, 17.0, 15.5, 2.94]
# Output:
# [0.7155049786628734, 1.0, 1.0, 0.8933143669985776, 0.0]

def test(nums):
  #find min and max of values
  maxi = max(nums)
  mini = min(nums)
  #checks if the min and ax values are )
  #if the range is zero, return a list w 0.0 as the first element and a 1.0 for the remaining elements
  # if maxi - mini == 0:
  #   return [0.0] + [1.0] * (len(nums)-1)
  #iterate over the indices of the list
  for n in range(len(nums)):
    #rescale and shift each element in the list to cover the range[0,1]
    nums[n] = (nums[n] - mini)/(maxi-mini)
  return nums
print(test([18.5, 17.0, 18.0, 19.0, 18.0]))