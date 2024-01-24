# Write a Python program to compute the product of the odd digits in a given number, or 0 if there aren't any.
# Input: 123456789
# Output:
# 945
# Input: 2468
# Output:
# 0
# Input: 13579
# Output:
# 945

def test(num):
  if any(int(n) % 2 for n in str(num)):
    numbers = 1
    for n in str(num):
      if int(n) % 2 != 0:
        numbers *= int(n)
    return numbers
  return 0
print(test(2468))