#  Write a Python program to check the nth-1 string is a proper substring of the nth string in a given list of strings.
# Input:
# ['a', 'abb', 'sfs', 'oo', 'de', 'sfde']
# Output:
# True
# Input:
# ['a', 'abb', 'sfs', 'oo', 'ee', 'sfde']
# Output:
# False
# Input:
# ['a', 'abb', 'sad', 'ooaaesdfe', 'sfsdfde', 'sfsd', 'sfsdf', 'qwrew']
# Output:
# False
# Input:
# ['a', 'abb', 'sad', 'ooaaesdfe', 'sfsdfde', 'sfsd', 'sfsdf', 'qwsfsdfrew']
# Output:
# True

def test(str1):
  return str1[len(str1) - 2] in str1[len(str1) - 1] and str1[len(str1) - 2] != str1[len(str1) - 1]
print(test(['a', 'abb', 'sfs', 'oo', 'de', 'sfde']))