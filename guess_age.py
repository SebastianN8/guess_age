#
# guess_age.py
# 
# Created by: Sebastian N
# Created on: April 6
#
# This program challeges the user to guess an age

# Guess from user
guess_user = 0

# While loop
while (guess_user is not 19):
	guess_user = int(input('What do you think is my age: '))
	if guess_user == 19:
		print('You got it!')
	elif guess_user > 19:
		print('You guessed too big. Try again!')
	elif guess_user < 19:
		print('You guessed too small. Try again!')
	else:
		print('Invalid answer!')

input()
