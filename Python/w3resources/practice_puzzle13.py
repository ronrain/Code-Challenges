# Write a Python program to find strings in a given list starting with a given prefix.
# Input:
# [( ca,('cat', 'car', 'fear', 'center'))]
# Output:
# ['cat', 'car']
# Input:
# [(do,('cat', 'dog', 'shatter', 'donut', 'at', 'todo'))]
# Output:
# ['dog', 'donut']

def test(pre, strg):
  return [pre == s[:2] for s in strg]
def test1(strg, prefix):
  return [s for s in strg if s.startswith(prefix)]
pre = 'do'
strg = ['cat', 'dog', 'shatter', 'donut', 'at', 'todo']
print(test(pre, strg))
print(test1(strg, pre))