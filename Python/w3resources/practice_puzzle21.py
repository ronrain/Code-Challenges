# Write a Python program to check, for each string in a given list, whether the last character is an isolated letter or not. Return True otherwise False.
# Input:
# ['cat', 'car', 'fear', 'center']
# Output:
# [False, False, False, False]
# Input:
# ['ca t', 'car', 'fea r', 'cente r']
# Output:
# [True, False, True, True]

def test(words):
  return [len(word.split(" ")[-1]) == 1 for word in words]
    #removes the last letter where the space is and measures to see of its 1.
    # if no space then has to be false
print(test(['cat', 'car', 'fear', 'center']))