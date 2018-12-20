import random

print('\tHANGMAN')
images =['''
	         +---+
	           |
	           |
	           |
                ========
						''','''
			 +----+
		      0 |
			    |
			    |
			 ========
			 			''', '''
			 +----+
   		      0 |
   			  | |
   			    |
   			 ========
			 			''','''
			 +----+
   		      0 |
   			 /| |
   			    |
   			 ========
			 			''','''
			 +----+
   		      0 |
   			 /|\\|
   			    |
   			 ========
			 			''','''
			 +----+
   		       0  |
   			  /|\\|
   			  /
   			 ========
			 			''','''
			 +----+
    		  0 |
    		 /|\\|
    		 /\\
    	    ========
				 			''']


def getRandomWord():
	words = ['word','cat','dog','rat','animal','computer','python']
	randomword = words[random.randint(1, len(words)-1)]
	return randomword

endofgame = False
while endofgame == False:
	imageindex = 0
	wordfound = False
	randomword = 'animal'
	#randomword = getRandomWord()
	length = len(randomword)
	b = '-'*length
	blanks = list(b)

	print('I have a random word. Try and guess\na letter in a word:')
	while(imageindex != len(images)-1 and wordfound == False):

		for i in range(len(blanks)):
			print(blanks[i],end='')
		print('')
		print(images[imageindex])
		print('input letter: ',end='')
		guessedletter = input()
		guessedletter = guessedletter.lower()
		while(len(guessedletter)!=1):
			print('Guess a one letter word please.')
			guessedletter = input()
		if(guessedletter in randomword):
			indices = [i for i, x in enumerate(list(randomword)) if x == guessedletter]
			for z in range(len(indices)):
				blanks[indices[z]] = guessedletter
			#blanks = blanks[:i] + list(guessedletter) + blanks[i+1:]
		else:
			imageindex = imageindex +1
			print('Wrong. ',end=' ')

		if('-' not in blanks):
			print('==================')
			print('Word:',end=' ')
			print(randomword)
			print('You have found the word!')
			print('')
			print('Would you like to try again? "Y" or "N"')
			playagain = input()
			wordfound = True
	if(imageindex == len(images)-1):
		print('You have guessed ' + str(imageindex +1) + ' times.')
		print('You have run out of guesses.\n Would you like to try again? "Y" or "N"')
		playagain = input()


	if(playagain.lower() == 'y'):
		endofgame = False
	elif(playagain.lower() == 'n'):
		endofgame = True
		print('Goodbye!')
