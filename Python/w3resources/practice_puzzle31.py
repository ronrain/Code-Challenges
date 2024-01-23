# Write a Python program to find the coordinates of a triangle with given side lengths.
# Input:
# [3, 4, 5]
# Output:
# [[0.0, 0.0], [3, 0.0], [3.0, 4.0]]
# Input:
# [5, 6, 7]
# Output:
# [[0.0, 0.0], [5, 0.0], [3.8, 5.878775382679628]]


def test(sides):
  #sort the sides in ascending ordeer and assign them a b c
  a,b,c = sorted(sides)
  #calculate the semi-perimeter of the triangle
  s = sum(sides)/2
  #use heron's formula to calculate the area if the triangle
  area = (s * (s-a) * (s-b) * (s-c)) **0.5
  #calculate the hight of the triangle
  y = 2 * area / a
  #calculate the x-coordinate of the third vertex using the Pythagorean theorem
  x = (c**2-y**2)**0.5
  return [[0.0,0.0],[a,0.0],[x,y]]

print(test([5, 6, 7]))