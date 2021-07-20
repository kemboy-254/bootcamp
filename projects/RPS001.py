print()

import random

input("Welcome to Rock, Paper, Scissors! Press enter to start.")

my_score=0
comp_score=0

while True:
	print()

	my_choice=input("Rock, Paper, or Scissors?: ").lower()

	while my_choice != "rock" and my_choice != "paper" and my_choice != "scissors":

		my_choice = input("Invalid Choice! Please try again: ").lower()

	random_num=random.randint(0,2)

	if random_num == 0:
		comp_choice="rock"
	elif random_num == 1:
		comp_choice="paper"
	elif random_num == 2:
		comp_choice="scissors"

	print()
	print("You chose: ",my_choice)
	print("The computer chose: ",comp_choice)
	print()

	if my_choice=="rock":
		if comp_choice=="rock":
			print("It's a tie")
		elif comp_choice=="paper":
			print("You Lost! Paper covers the Rock")
			comp_score += 1
		elif comp_choice=="scissors":
			print("You Won!! The Rock smashes Scissors")
			my_score += 1

	elif my_choice=="paper":
		if comp_choice=="paper":
			print("It's a tie")
		elif comp_choice=="scissors":
			print("You Lost! Scissors cut the Paper")
			comp_score += 1
		elif comp_choice=="rock":
			print("You Won!! Paper covers the Rock")
			my_score += 1

	elif my_choice=="scissors":
		if comp_choice=="scissors":
			print("It's a tie")
		elif comp_choice=="rock":
			print("You Lost! Rock smashes the Scissors")
			comp_score += 1
		elif comp_choice=="paper":
			print("You Won!! Scissors cut the Paper")
			my_score += 1

	print()
	print("You have",my_score,"wins")
	print("The computer has",comp_score,"wins")
	print()

	repeat = input("Do you want to continue? (Y/N)  ").lower()
	while repeat != "y" and repeat != "n":
		repeat = input("Invalid Choice! Please try again:  ").lower()


	if repeat == "n":
		print()
		print("Thanks for the game! Come back soon")
		print()
		break
		
	print("\n--------------------\n")

