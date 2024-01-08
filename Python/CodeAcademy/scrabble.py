letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_point = dict(zip(letters, points))
letter_to_point[" "] = 0
print(letter_to_point)

def score_word(word):
  point_total = 0
  for letter in word:
    point_total += letter_to_point[letter]
    if letter not in letter_to_point:
      point_total += 0
  return point_total

print(score_word("BROWNIE"))

player_to_word = {"Player 1": ["BLUE", "TENNIS", "EXIT"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}
