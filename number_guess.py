# Author: Anthony Rodriguez
# Version: 1.0
# Since: 2019-05-25
import random, math, time
from utilities import *
from player import *

def get_name():
	""" Returns the player's name. """
	clear_screen()
	print("Hello! What is your name?")
	name = input()
	return name

def play_game(player, number, upperBound):
	""" Gets each guess from the player.

	name -- The player
	number -- the secret number
	upperBound -- The secret number can range from 1 to upperBound

	"""
	clear_screen()
	max_guesses = (int) (math.log(upperBound, 2))
	print("Well, " + player.get_name() + ", I am thinking of a number " \
	 "between 1 and " + str(upperBound) + ".")
	print("You will have " + str(max_guesses) + " guesses.")

	for guess_num in range(max_guesses):
		flush_input()
		print('Enter your guess:')
		guess = input()
		guess = int(guess)
		guesses_taken = guess_num + 1

		if guess < number:
			clear_screen()
			print('Your guess is too low.')
			time.sleep(2)
			clear_screen()

		if guess > number:
			clear_screen()
			print('Your guess is too high')
			time.sleep(2)
			clear_screen()

		if guess == number:
			print('\nGood job, ' + player.get_name() + \
				'! You guessed my number in ' + str(guesses_taken) + \
				" guesses!" if guesses_taken > 1 else " guess!")
			player.increase_score(max_guesses - guess_num)
			print("\nSCORE: " + str(player.get_score()))
			time.sleep(4)
			return True

	print('\nYou are out of guess attempts. The number I was thinking of was ' + str(number) + '.')
	print('\nSCORE: ' + str(player.get_score()))	
	time.sleep(4)
	return False

def showTitle(top_player, highest_score):
	""" Shows the opening title of the game. """
	clear_screen()
	title = \
	"""
    ***************************************************************************************************
    *                                                                                                 *
    *  NN     N  U    U  M     M  BBBBBB   EEEEEE  RRRRR      GGGGGG  U    U  EEEEEE  SSSSSS  SSSSSS  *
    *  N N    N  U    U  M M M M  B     B  E       R    R     G    G  U    U  E       S       S       *
    *  N  N   N  U    U  M  M  M  BBBBBB   E       R    R     G       U    U  E       S       S       *
    *  N   N  N  U    U  M     M  B     B  EEEEEE  RRRRR      G   GGG U    U  EEEEEE  SSSSSS  SSSSSS  *
    *  N    N N  U    U  M     M  B     B  E       R    R     G    G  U    U  E            S       S  *
    *  N     NN  UUUUUU  M     M  BBBBBB   EEEEEE  R    R     GGGGGG  UUUUUU  EEEEEE  SSSSSS  SSSSSS  *
    *                                                                                                 *
    ***************************************************************************************************
    """
	print(title)
	print('\n\n\t\t\t\t\tPress Enter to start game')
	print('\n\n\t\t\t\tHighest Score: ' + str(highest_score) +\
		  ' | Top Player Name: ' + str(top_player))
	input()

def playAgain():
	""" Checks to see if the player wants to play again. """
	clear_screen()
	flush_input()
	print("Would you like to play the game again?")
	print("Enter yes or no:")
	answer = input()
	answer = answer.lower()
	# Error checking input
	while answer != "yes" and answer != "no":
		clear_screen()
		print("You must only enter yes or no.")
		time.sleep(3)
		clear_screen()
		flush_input()
		print("Would you like to play the game again?")
		print("Enter yes or no:")
		answer = input()
		answer = answer.lower()

	if answer == "yes":
		return True
	return False

def main():
	# Open file with top player and highest score
	f_highest_score = open("highest_score.txt", "r")
	top_player = f_highest_score.readline().strip()
	highest_score = f_highest_score.readline().strip()
	highest_score = int(highest_score)
	f_highest_score.close()
	# Show the title
	showTitle(top_player, highest_score)
	play = True
	upperBound = 10
	name = get_name()
	player = Player(name)
	# Begin the game loop
	while play:
		number = random.randint(1, upperBound)
		correct_guess = play_game(player, number, upperBound)
		if correct_guess:
			clear_screen()
			upperBound += 10
		else:
			play = playAgain()
			upperBound = 10
	# Check to see if there is a new top player
	if (player.get_score() > highest_score):
		print("Congratulations " + player.get_name() + "!")
		print("You scored "+ str(player.get_score()) + "!")
		print("You have the new highest score!")
		print("You are the new top player of Number Guess!")
		file = open("highest_score.txt", "w")
		file.write(player.get_name())
		file.write("\n")
		file.write(str(player.get_score()))
		file.close()

if __name__=='__main__':
	main()
