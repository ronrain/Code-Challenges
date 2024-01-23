# Write a Python program to find the XOR of two given strings interpreted as binary numbers.
# Input:
# ['0001', '1011']
# Output:
# 0b1010
# Input:
# ['100011101100001', '100101100101110']
# Output:
# 0b110001001111

def test(num):
  return bin(int(num[0], 2) ^ int(num[1], 2))

print(test(['0001', '1011']))