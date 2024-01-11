# Write a Python program to find strings in a given list containing a given substring.
# Input:
# [(ca,('cat', 'car', 'fear', 'center'))]
# Output:
# ['cat', 'car']
# Input:
# [(o,('cat', 'dog', 'shatter', 'donut', 'at', 'todo', ''))]
# Output:
# ['dog', 'donut', 'todo']
# Input:
# [(oe,('cat', 'dog', 'shatter', 'donut', 'at', 'todo', ''))]
# Output:
# []

def test(strg, let):
  return [s for s in strg if let in s]
let = 'o'
strg = ('cat', 'dog', 'shatter', 'donut', 'at', 'todo', '')
print(test(strg, let))