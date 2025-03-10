#Ask the user to make a choice
# If choice is not valid
#   print an error
# Let the computer to make a choice 
# Print choices 
#Determine the winner 
#Ask the user if they want to continue 

import random

ROCK = 'r'
SCISSOR = 's'
PAPER = 'p'

emojis = { SCISSOR: '✂️',  PAPER: '📰', ROCK: '🪨'}
choices = tuple(emojis.keys())

def get_user_choice():
  while True:
    user_ch= input("What do you choices (Paper, Rock, Scissors): ").lower()
    if user_ch in choices:
      return user_ch
    else:
      print  ("Invalid choice")

def display_choice(user_ch):
  print (f"you chose: {emojis [user_ch]}"),
  print (f"computer chose: {emojis[computer_ch]}")

def Determine_the_winner(user_ch):
  if user_ch == computer_ch:
    print ('Tie')
  elif (
    (user_ch == ROCK and computer_ch == SCISSOR) or 
    (user_ch == SCISSOR and computer_ch == PAPER) or
    (user_ch == PAPER and computer_ch == ROCK) ):
    print ("you win 👏")
  else: 
    print ("You lose 😔")

while True:
  user_choice = get_user_choice()
  computer_ch= random.choice(choices)
  
  display_choice(user_choice)
  
  Determine_the_winner(user_choice)
  
  Question = input("Do you wan Continue (Y/N): ").upper()
  if Question == 'N':
    print ("Thanks for visit our game 💐")
    break
