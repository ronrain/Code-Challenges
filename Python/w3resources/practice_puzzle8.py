#  Write a Python program to split a string of words separated by commas and spaces into two lists, words and separators.
# Input: W3resource Python, Exercises.
# Output:
# [['W3resource', 'Python', 'Exercises.'], [' ', ', ']]
# Input: The dance, held in the school gym, ended at midnight.
# Output:
# [['The', 'dance', 'held', 'in', 'the', 'school', 'gym', 'ended', 'at', 'midnight.'], [' ', ', ', ' ', ' ', ' ', ' ', ', ', ' ', ' ']]
# Input: The colors in my studyroom are blue, green, and yellow.
# Output:
# [['The', 'colors', 'in', 'my', 'studyroom', 'are', 'blue', 'green', 'and', 'yellow.'], [' ', ' ', ' ', ' ', ' ', ' ', ', ', ', ', ' ']]

def test(string):
    import re #used for working with regular expressions
    merged = re.split(r"([ ,]+)", string) #method to split a string based on a specifc regex pattern
    #[ ,]+ matches one or more patterns with a space or comma
    #([ ,]+) enclosed in parentheses to create a capturing group
    #this makes the string when split include spaces and commas
    return [merged[::2], merged[1::2]]
  #[::2] contains every second element on the list starting at index 0
#[1::2] contains all the elements that start at the second element and skips every other element
print(test("The dance, held in the school gym, ended at midnight."
))