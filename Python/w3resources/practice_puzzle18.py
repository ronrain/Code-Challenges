# An irregular/uneven matrix, or ragged matrix, is a matrix that has a different number of elements in each row. Ragged matrices are not used in linear algebra, since standard matrix transformations cannot be performed on them, but they are useful as arrays in computing.
# Write a Python program to find the indices of all occurrences of target in the uneven matrix.
# Input:
# [([1, 3, 2, 32, 19], [19, 2, 48, 19], [], [9, 35, 4], [3, 19]),19]
# Output:
# [[0, 4], [1, 0], [1, 3], [4, 1]]
# Input:
# [([1, 2, 3, 2], [], [7, 9, 2, 1, 4]),2]
# Output:
# [[0, 1], [0, 3], [2, 2]]

def test(M, T):
  occurences = []
  for i, row in enumerate(M): #enumerate iterates over a list tuple or string, keeps track of the index and the corresponding element
    for j, n in enumerate(row):
      if n == T:
        occurences.append([i,j])
  return occurences

def test_list_comprehension(M, T):
  return [[i,j] for i, row in enumerate(M) for j, n in enumerate(row) if n == T]


print(test(([1, 3, 2, 32, 19], [19, 2, 48, 19], [], [9, 35, 4], [3, 19]),19))
print(test_list_comprehension(([1, 2, 3, 2], [], [7, 9, 2, 1, 4]),2))