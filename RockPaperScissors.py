import random

game_options = ("rock", "paper", "scissors")
players_list = ["AI"]
choices_list = []

num_ai_wins = 0
num_human_wins = 0

username = input("Enter your name: ")
players_list.append(username)
num_rounds = int(input("Enter the number of rounds: "))

def determine_winner(index1, index2):
  winning_hand = index1
  losing_hand = index2

  #Identify winner by using the input choices and searching for its postion in the choice_list, then using the returned position to find the corresponding player ID in the players list
  winner = players_list[choices_list.index(index1)]
  loser = players_list[choices_list.index(index2)]
  
  print("The winner is {} who played {}.\nThe loser is {} who played {}.\n".format(winner, winning_hand, loser, losing_hand).replace("\'", ""))

#Winner is set as index1 and loser as index2
for i in range(0, num_rounds):
  ai_choice = random.choice(game_options)
  choices_list.append(ai_choice)
  
  user_choice = input("\nEnter \"rock\", \"paper\", or \"scissors\": ").lower()
  choices_list.append(user_choice)
  
  if ai_choice == user_choice:
    print("Draw! Both players played {}.\n".format(ai_choice).replace("\'", ""))
  elif "rock" and "paper" in choices_list:
    index1 = "paper"
    index2 = "rock"
    determine_winner(index1, index2)
  elif "rock" and "scissors" in choices_list:
    index1 = "rock"
    index2 = "scissors"
    determine_winner(index1, index2)
  elif "paper" and "scissors" in choices_list:
    index1 = "scissors"
    index2 = "paper"
    determine_winner(index1, index2)
  else:
    print("Nani?!")

  choices_list.clear()
