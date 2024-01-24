# Write a Python program to find the positions of all uppercase vowels (not counting Y) in even indices of a given string.
# Input: w3rEsOUrcE
# Output:
# [6]
# Input: AEIOUYW
# Output:
# [0, 2, 4]

def test(word):
  return [i for i, c in enumerate(word) if i % 2 == 0 and c in "AEIOU"]
print(test(['w3rEsOUrcE']))