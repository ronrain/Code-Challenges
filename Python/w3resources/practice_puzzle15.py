# Write a Python program to find the longest string in a given list of strings.
# Input:
# ['cat', 'car', 'fear', 'center']
# Output:
# center
# Input:
# ['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']
# Output:
# shatter

def test(strg):
  return max(strg, key=len)
print(test(['cat', 'car', 'fear', 'center']))
