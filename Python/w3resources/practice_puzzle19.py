# Write a Python program to split a given string (s) into strings if there is a space in s, otherwise split on commas if there is a comma, otherwise return the list of lowercase letters in odd order (order of a = 0, b = 1, etc.).
# Input:
# a b c d
# Split the said string into strings if there is a space in the string,
# otherwise split on commas if there is a comma,
# Output:
# ['a', 'b', 'c', 'd']
# Input:
# a,b,c,d
# Split the said string into strings if there is a space in the string,
# otherwise split on commas if there is a comma,
# Output:
# ['a', 'b', 'c', 'd']
# Input:
# abcd
# Split the said string into strings if there is a space in the string,
# otherwise split on commas if there is a comma,
# Output:
# ['b', 'd']



def test(s):
  if " " in s: #if theres a space in the string
    return s.split(" ") #seperate the string based on space
  elif "," in s: # if theres a comma in the string
    return s.split(",") #seperate the string based on comma
  else:
    return [c for c in s if c.islower() and ord(c) % 2 == 0]
      #c is the variable that represnets eacg character in s
      #for c in s iterates through each character in s
      #c.islower() checks if the character is lowercase
      #ord(c) % 2 == 0 checks if the unicode at c is even


print(test('a b c d'))