# Write a Python program to select a string from a given list of strings with the most unique characters.
# Input:
# ['cat', 'catatatatctsa', 'abcdefhijklmnop', '124259239185125', '', 'foo', 'unique']
# Output:
# abcdefhijklmnop
# Input:
# ['Green', 'Red', 'Orange', 'Yellow', '', 'White']
# Output:
# Orange

from collections import Counter

def test(words): 
  return max(words, key=lambda x: len(set(x)))
  #lambda function is a smaller fucntion, the x is the argument and the len(set(x)) is the expression
  #set() removes all duplicate characters
  #len() measures the length of the string
  #max() then finds the max element based on the key function

print(test(['Green', 'Red', 'Orange', 'Yellow', '', 'White']))
