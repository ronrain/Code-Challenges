# Given a string consisting of whitespace and groups of matched parentheses, write a Python program to split it into groups of perfectly matched parentheses without any whitespace.
# Input:
# ( ()) ((()()())) (()) ()
# Output:
# ['(())', '((()()()))', '(())', '()']
# Input:
# () (( ( )() ( )) ) ( ())
# Output:
# ['()', '((()()()))', '(())']

def test(combined):
  ls=[]#will contain the extracted substring
  str=""#used to accumulate characters from the combined list
  for s in combined.replace(" ",""): #iterates through the characters in    the combined list
    #removes any spaces from the combined list
    str += s  # Append the current character to the accumulating string s2.
    if str.count("(") == str.count(")"):
      ls.append(str)  # If the counts of '(' and ')' are equal, add s2 to the list ls.
      str = ""  # Reset s2 to an empty string for the next substring.
  return ls


print(test('() (( ( )() ( )) ) ( ())'))