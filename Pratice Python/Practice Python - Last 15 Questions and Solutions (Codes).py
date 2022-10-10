#!/usr/bin/env python
# coding: utf-8

# #Practice Python Exercises
# *Ref: https://www.practicepython.org/*
# 

# #### Q25. User will have in your head a number between 0 and 100. The program will guess a number, and you, the user, will say whether it is too high, too low, or your number.
# 
# #### At the end of this exchange, your program should print out how many guesses it took to get your number.
# 
# #### Note: The program needs an optimal guessing strategy. An alternate strategy might be to guess 50 (right in the middle of the range), and then increase / decrease by 1 as needed. After you’ve written the program, try to find the optimal strategy! (We’ll talk about what is the optimal one next week with the solution.)

# In[ ]:


# binary search to check how many guesses is required by the computer to find the number
def binary_search():
  user_num = int(input("Choose a num between 0 to 100:"))
  num_list = [i for i in range(0,101)]
  
  lower_index, upper_index = 0, len(num_list)-1
  guess_count = 0
  while lower_index <= upper_index:

    mid_index = (lower_index + upper_index) // 2
    mid_value = num_list[mid_index]

    guess_count += 1

    if user_num == mid_value:
      return user_num, guess_count
    elif user_num < mid_value:
      upper_index = mid_index - 1
    else:
      lower_index = mid_index + 1
    

print("The computer took", binary_search()[1], "guesses to find your number")


# #### Q26. If a game of Tic Tac Toe is represented as a list of lists, like so:
# #### game = [[1, 2, 0],
# ####        [2, 1, 0],
# ####	      [2, 1, 1]]
# #### where a 0 = empty square, a 1 = player 1 put their token in that space, and a 2 = player 2 put their token in that space.
# 
# #### Given a 3 by 3 list of lists, tell me whether anyone has won, and tell me which player won, if any. A Tic Tac Toe win is 3 in a row - either in a row, a column, or a diagonal. Assume that in every board there will only be one winner.

# In[ ]:


# checking rows
def row_match(game):
  for rows in game:
    if len(set(rows)) == 1:
      return rows[0]
  else:
    return None

# checking columns
def col_match(game):
  rows, cols = 0,0
  while cols <= 2:
    if game[rows][cols] == game[rows+1][cols] == game[rows+2][cols]:
      return game[rows][cols]
    cols += 1
  else:
    return None

# checking diagonals
def diag_match(game):
  if len(set([game[i][i] for i in range(len(game))])) == 1:
        return game[0][0]
  elif len(set([game[i][len(game)-i-1] for i in range(len(game))])) == 1:
        return game[0][len(game)-1]
  else:
    return None


# winning games
winner_1 = [[1, 2, 0],
	          [2, 1, 0],
	          [2, 1, 1]]

winner_2 = [[2, 2, 0],
	          [2, 1, 0],
	          [2, 1, 1]]

winner_1_also = [[0, 1, 0],
	               [2, 1, 0],
	               [2, 1, 1]]

# drawing games
draw = [[1, 1, 0],
	      [0, 2, 1],
	      [1, 1, 2]]

also_draw = [[1, 2, 0],
	           [2, 1, 0],
	           [2, 1, 0]]

also2_draw = [[1, 2, 0],
	            [2, 1, 0],
	            [2, 1, 2]]

def check_game(game):
  if col_match(game) != None and col_match(game) != 0:
    print("Player {} is the winner !".format(col_match(game)))
  elif row_match(game) != None and row_match(game) != 0:
    print("Player {} is the winner !".format(row_match(game)))
  elif diag_match(game) != None:
    print("Player {} is the winner !".format(diag_match(game)))
  else:
    print("Its a draw ! There is no winner :(")

check_game(winner_1)


# #### Q27 & Q29. Tic-tac-toe
# 
# - For this exercise, assume that player 1 (the first player to move) will always be X and player 2 (the second player) will always be O.
# 
# - Coordinates starting from (1, 1) instead of (0, 0).
# 
# - Ask the user to enter coordinates in the form “row,col” - a number, then a comma, then a number. 
# 
# - Don’t worry about checking whether someone won the game, but if a player tries to put a piece in a game position where there already is another piece, do not allow the piece to go there.
# 
# - Keep track of how many squares are full and automatically stop asking for moves when there are no more valid moves.

# In[ ]:


game = [[0, 0, 0],
	      [0, 0, 0],
	      [0, 0, 0]]

# checking rows
def row_match(game):
  for rows in game:
    if len(set(rows)) == 1:
      return rows[0]
  else:
    return None

# checking columns
def col_match(game):
  rows, cols = 0,0
  while cols <= 2:
    if game[rows][cols] == game[rows+1][cols] == game[rows+2][cols]:
      return game[rows][cols]
    cols += 1
  else:
    return None

# checking diagonals
def diag_match(game):
  if len(set([game[i][i] for i in range(len(game))])) == 1:
        return game[0][0]
  elif len(set([game[i][len(game)-i-1] for i in range(len(game))])) == 1:
        return game[0][len(game)-1]
  else:
    return None

# checking for a winner on the board
def check_game(game):
  if col_match(game) != None and col_match(game) != 0:
    return col_match(game)
  elif row_match(game) != None and row_match(game) != 0:
    return row_match(game)
  elif diag_match(game) != None:
    return diag_match(game)
  else:
    return False

def player_move(player_mark, game):
  x_coord, y_coord = [int(i) for i in input("Enter the coordinates: ").split(",")]
  x_index, y_index = x_coord-1, y_coord-1
  if game[x_index][y_index] == 0:
    game[x_index][y_index] = player_mark
  else:
    print("This square is occupied :( Try another square")
    player_move(player_mark, game)

print("Welcome to Tic-Tac-Toe !!! ")
print("Player 1 starts first and plays with X while Player 2 plays with O")

spaces = 9
player_number = 1
continue_game = 'y'
player1_count = 0
player2_count = 0

while continue_game == 'y':

  while spaces >= 0:
    
    if check_game(game) == False:
      
      if player_number == 1:
        print("Player {}'s turn".format(player_number))
        player_move('X', game)
        player_number += 1
      elif player_number == 2:
        print("Player {}'s turn".format(player_number))
        player_move('O', game)
        player_number -= 1
      else:
        player_number = player_number
      
      spaces = sum([rows.count(0) for rows in game])
      #print("There are {} spaces left".format(spaces))
      spaces -= 1
      
      for row in game:
        print('| ' + ' '.join(str(place).replace("0", " ") + ' |' for place in row))
        print(" --- --- --- ")

    elif check_game(game) == 'X':
      print("Player 1 is the winner !")
      player1_count += 1
      break

    elif check_game(game) == 'O':
      print("Player 2 is the winner !")
      player2_count += 2
      break

  print("There are no moves left !")
  continue_game = input("Do you wish to continue? y/n")
  if continue_game == 'n':
    print("Player 1 won {} games and Player 2 won {} games".format(player1_count, player2_count))
    break


# #### Q28. Implement a function that takes as input three variables, and returns the largest of the three. Do this without using the Python max() function!

# In[ ]:


def max_num(num1, num2, num3):
  if num1 > num2 and num1 > num3:
    return num1
  elif num2 > num1 and num2 > num3:
    return num2
  elif num3 > num1 and num3 > num2:
    return num3
  elif num1 == num2 == num3:
    return num1
  else:
    num_list = [num1, num2, num3]
    for num in num_list:
      if num_list.count(num) == 2:
        return num
    
max_num(2,1,2)


# #### Q30. Hangman (part 1/3): Pick a random word from a list of words from the SOWPODS dictionary i.e. hangman_words.txt file

# In[ ]:


import random
with open('hangman_words.txt', 'r') as open_file:
    raw_words = open_file.readlines()

all_words = [words.replace('\n','') for words in raw_words]
random_word = random.choice(all_words)


# #### Q31. Hangman (part 2/3): Write the logic that asks a player to guess a letter and displays letters in the clue word that were guessed correctly. For now, let the player guess an infinite number of times until they get the entire word. As a bonus, keep track of the letters the player guessed and display a different message if the player tries to guess that letter again. Stop the game when all the letters have been guessed correctly.

# In[ ]:


guessed_letters = []
correct_letters = []

def guess_word(word):
  spaces = '_'*len(word)

  while spaces != word:
    guess = input("Guess your letter: ").upper()

    if guess in guessed_letters:
      print("This letter has already been guessed ! Try a different one ")
    
    elif guess in word:
      correct_letters.append(guess)

      for i in range(len(word)):
        if word[i] in correct_letters:
          spaces = spaces[:i] + word[i] + spaces[i+1:]

    else:
      print("Incorrect letter :( Please try again !")
    
    guessed_letters.append(guess)
    print(" ".join(spaces))

  print("Congrats, you've guessed it correctly !")
  print("Number of Guesses: ", len(guessed_letters))
  print("Your guesses: ", guessed_letters)


random_word = random.choice(all_words)
print("Welcome to HANGMAN")
print('_ '*len(random_word))
print(random_word)
guess_word(random_word)


# #### Q32. Hangman (part 3/3): Real Hangman game:
# 
# - Only let the user guess 6 times, and tell the user how many guesses they have left.
# 
# - Keep track of the letters the user guessed. If the user guesses a letter they already guessed, don’t penalize them - let them guess again
# 
# - When the player wins or loses, let them start a new game.

# In[ ]:


import random
with open('hangman_words.txt', 'r') as open_file:
    raw_words = open_file.readlines()

all_words = [words.replace('\n','') for words in raw_words]

# function for guessing the word
def guess_word(word):
  guessed_letters = []
  correct_letters = []

  spaces = '_'*len(word)
  incorrect_count = 6

  while incorrect_count >= 1:
    
    guess = input("\nGuess your letter: ").upper()

    if guess in guessed_letters:
      print("This letter has already been guessed ! Try a different one ")
    
    elif guess in word:
      correct_letters.append(guess)

      for i in range(len(word)):
        if word[i] in correct_letters:
          spaces = spaces[:i] + word[i] + spaces[i+1:]
      
      if spaces == word:
        break

    else:
      incorrect_count -= 1
      print("Incorrect letter :( Please try again !")
  
    guessed_letters.append(guess)
    if incorrect_count == 0:
      break
    print("\nYou have {} incorrect guesses left !".format(incorrect_count))
  
    print(" ".join(spaces))
  return spaces

quit = 'n'

while quit == 'n':
  random_word = random.choice(all_words)

  print("\nWelcome to HANGMAN")
  print('_ '*len(random_word))
  print(random_word)

  if guess_word(random_word) == random_word:
    print("Congrats you guessed the word {} !".format(random_word))
  else:
    print("Whoops :( You've exhausted your attempts !")
    print("The word was: ", random_word)
  
  quit = input("\nDo you want to quit Hangman ? (y/n): \n")
  if quit == 'y':
    break


# In[ ]:


# # side project: Takes a word, and returns the index values of the characters in the string
# word = 'ABBCA'
# guess_list = ['A', 'B', 'C', 'D']
# # create a dictionary to store the correct letters and their index value(s) in the word
# guess_dict = {} # {'character': [index]}

# for guess in guess_list:
#   guess_dict[guess] = [index for index in range(len(word)) if word.startswith(guess, index)]

# print(guess_dict)


# #### Q33: Birthday Data (part 1/4): Create a dictionary of names and birthdays. Print the names in the dictionary first and then ask the user to enter a name; then return the birthday of that person back to them

# In[24]:


bday_dict = {
    "A": '01/07/1987',
    "B": '04/08/2007',
    "C": '23/02/1970',
    "D": '19/11/2023',
    "E": '30/01/1990'
}

print("We know the birthdays of :")
for name in bday_dict:
    print(name, end=' ')

bday_name = input("\nWho's birthday do you want to look up?\n")
print("{}'s birthday is {}".format(bday_name.upper(), bday_dict[bday_name.upper()]))


# #### Q34. Birthday Data (part 2/4): Load the birthday dictionary from a JSON file on disk. Ask the user for another scientist’s name and birthday to add to the dictionary, and update the JSON file you have on disk with the scientist’s name. If you run the program multiple times and keep adding new names, your JSON file should keep getting bigger and bigger.

# In[ ]:


import json

def save_as_json(json_name, dict_name):
  # specify file name to be saved as...
  with open(json_name, "w") as f:
    json.dump(dict_name, f)

# Note: JSON won’t remember the name of the variable you saved your dictionary in

def load_json(json_name):
  with open(json_name, "r") as f:
    info = json.load(f)
  return info

# json file
json_name = "bday_database.json"

add_name = 'y'

while add_name == 'y':
  
  print("Birthday Database: ")
  print(json.dumps(load_json(json_name), indent=2))

  add_name = input("Do you wish to add a new name (y/n)?")
  if add_name == 'n':
    break
  
  bday_dict = load_json(json_name) # returns the dict

  new_name = input("Enter a name: \n")
  bday = input("Enter age in the form dd/mm/yyyy (with slashes): \n")
  bday_dict[new_name] = bday

  save_as_json(json_name,bday_dict)


# #### Q35: Birthday Data (part 3/4): Load that JSON file from disk, extract the months of all the birthdays, and count how many scientists have a birthday in each month (Hint: Import counter module from collections library)

# In[ ]:


from collections import Counter

# json file
json_name = "bday_database.json"

# month names
months = ['Jan', 'Feb', 'March', 'April', 'May', 'June', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# store the dict
bday_dict = load_json(json_name)

def get_months(dict_name):
  # gets the birthdates from the dictionary
  date_list = [dict_name[name] for name in dict_name]

  # gets the month numbers from the dates
  month_num_list = [int(date.split('/')[1]) for date in date_list]

  # converts month numbers to month names
  month_name_list = [months[month_num-1] for month_num in month_num_list]

  return month_name_list

num_of_bdays_per_month = dict(Counter(get_months(bday_dict)))
print(num_of_bdays_per_month)


# #### Q36. Birthday Data (part 4/4): Use the bokeh Python library to plot a histogram of which months the scientists have birthdays in 

# In[ ]:


import bokeh.io
from bokeh.plotting import figure, show, output_file

# Enable viewing Bokeh plots in the notebook
bokeh.io.output_notebook()

def bokeh_hist_plot(data_dict):
  html_file = input("Output Filename: \n") + ".html"

  # specify an output file
  output_file(html_file)

  # load our x (keys in the dict) and y (corresponding values in the dict) data
  x = [month for month in data_dict]
  y = [data_dict[month] for month in data_dict]

  # create a figure
  months = ['Jan', 'Feb', 'March', 'April', 'May', 'June', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
  p = figure(x_range=months)

  # create a histogram
  p.vbar(x=x, top=y, width=0.5)

  # render (show) the plot
  show(p)

bokeh_hist_plot(num_of_bdays_per_month)


# #### Q37. Refactor the following print pattern using functions where generating an 8x8 or a 19x19 grid is a single change to a function call!

# In[ ]:


# print(" --- --- ---")
# print("|   |   |   |")
# print(" --- --- ---")
# print("|   |   |   |")
# print(" --- --- ---")
# print("|   |   |   |")
# print(" --- --- ---")

def draw_pattern(rows):
    pattern = ""
    for i in range(2*rows+1):
        # switch between printing vertical and horizontal bars
        if i % 2 == 0:
            pattern += " ---" * (rows)
        else:
            pattern += "|   " * (rows+1)
        pattern += "\n"

    print(pattern)

draw_pattern(3)


# #### Q38. Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old ----> except use f-strings instead of the + operator to print the resulting output message

# In[ ]:


from datetime import date

current_year = date.today().year

name = input("Enter your name:\n")
age = int(input("Enter your age:\n"))

print(f"{name} you will turn 100 years old in {current_year + (100-age)} !")





# In[ ]:




