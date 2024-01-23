# Write a Python program to find a list of strings that have fewer total characters (including repetitions).
# Input:
# [['this', 'list', 'is', 'narrow'], ['I', 'am', 'shorter but wider']]
# Output:
# ['this', 'list', 'is', 'narrow']
# Input:
# [['Red', 'Black', 'Pink'], ['Green', 'Red', 'White']]
# Output:
# ['Red', 'Black', 'Pink']


def test(words):
  return min(words, key=lambda x: sum(len(i) for i in x))
  
print(test([['this', 'list', 'is', 'narrow'], ['I', 'am', 'shorter but wider']]))