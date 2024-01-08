letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letters += [ #allows there to be lowercase letters in words
  letter.lower()
  for letter
  in letters
]
points *= 2 #applies the point system to the lowercase letters
letter_to_points = { #joins the 2 lists into a dictionary using a for loop
  key:value
  for key, value
  in zip(letters, points) #zip is used to combine dictionaries
}

letter_to_points[" "] = 0 #adds a space value that equals 0 if inputted
# print(letter_to_point)

def score_word(word): #adds the value of the word based on the point system. 
  point_total = 0
  for letter in word:
    point_total += letter_to_points[letter] #adds the point based on the letter used
    if letter not in letter_to_points:
      point_total += 0
  return point_total

# print(score_word("BROWNIE"))

player_to_words = {"Player 1": ["BLUE", "TENNIS", "EXIT"], "Word Nerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}

player_to_points = {}
def update_points_totals():
  for player, words in player_to_words.items():#creates a tuple of th player, words (key:value)
    player_points = 0
    for word in words:
      player_points += score_word(word)#declares the function score_word with the word that's inputted and translates the points from that word
    player_to_points[player] = player_points #finds the player that said the word and matches the points to the player {key:value}
update_points_totals()


def play_word(player, word):
  player_to_words[player].append(word)#adds the word a player in player_to_word inputs
  update_points_totals()#inititates the function to add the points based on that word

play_word("Player 1", "BROWN")
print(player_to_words)