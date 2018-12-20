import random



def printBoard(board):
    print(board[6]+'  |  '+board[7]+'  |  '+board[8])
    print('---------------')
    print(board[3]+'  |  '+board[4]+'  |  '+board[5])
    print('---------------')
    print(board[0]+'  |  '+board[1]+'  |  '+board[2])

def checkifwon(board, choice):
    if(
        (board[0]==choice and board[1]==choice and board[2]==choice)or
        (board[3]==choice and board[4]==choice and board[5]==choice)or
        (board[6]==choice and board[7]==choice and board[8]==choice)or
        (board[0]==choice and board[3]==choice and board[6]==choice)or
        (board[1]==choice and board[4]==choice and board[7]==choice)or
        (board[2]==choice and board[5]==choice and board[8]==choice)or
        (board[2]==choice and board[4]==choice and board[6]==choice)or
        (board[0]==choice and board[4]==choice and board[8]==choice)
      ):
      return True
def checkiflost(board, choice):
    if(
        (board[0]==choice and board[1]==choice and board[2]==choice)or
        (board[3]==choice and board[4]==choice and board[5]==choice)or
        (board[6]==choice and board[7]==choice and board[8]==choice)or
        (board[0]==choice and board[3]==choice and board[6]==choice)or
        (board[1]==choice and board[4]==choice and board[7]==choice)or
        (board[2]==choice and board[5]==choice and board[8]==choice)or
        (board[2]==choice and board[4]==choice and board[6]==choice)or
        (board[0]==choice and board[4]==choice and board[8]==choice)
      ):
      return True

def checkIfTableFull(board):
    for i in range(len(board)):
        if(board[i] == ' '):
            return False
        else:
            return True


num_list = '1 2 3 4 5 6 7 8 9'.split()
print('Welcome to Tic-Tac-Toe')
print('would you like to be X or O?')
choice = input()
while(choice != 'X' and choice != 'O'):
    print('pick either "X" or "O"')
    choice = input()

gamewon = False
gamelost = False
tablefull = False

gamechoice = ''
if(choice == 'X'):
    gamechoice = 'O'
else:
    gamechoice = 'X'
board = list(' '*9)
gameIsPlaying = True
print('The table looks as follows')
print('7 '+' | '+' 8 '+' | '+' 9')
print('---------------')
print('4 '+' | '+' 5 '+' | '+' 6')
print('---------------')
print('1 '+' | '+' 2 '+' | '+' 3')
print('')
print('You can pick a number to fill in the corresponding block.')
print('////////////////////////////////////////////////////')

while gameIsPlaying:
    print('Pick a number and enter here: ',end=' ')
    num = input()
    while(num not in num_list):
        print('Pick a valid number.')
        for i in range(len(num_list)):
            print(num_list[i],end=' ')
        num = input()
    num_list.remove(num)
    board[int(num)-1] = choice
    printBoard(board)
    gamewon = checkifwon(board, choice)
    gamelost = checkiflost(board, gamechoice)
    if gamewon == False and gamelost == False:
        tablefull = checkIfTableFull(board)
    if gamewon or gamelost or tablefull:
        gameIsPlaying = False

    if gamewon == True:
        print('You won.')
    elif gamelost == True:
        print('Suck on that. I won.')
    elif tablefull == True:
        print('We tied.')
    if gameIsPlaying == False:
        break
    randomNumber = num_list[random.randint(0, len(num_list)-1)]
    num_list.remove(randomNumber)
    board[int(randomNumber)-1] = gamechoice

    print('My turn:')
    printBoard(board)
    gamewon = checkifwon(board, choice)
    gamelost = checkiflost(board, gamechoice)
    if gamewon == False and gamelost == False:
        tablefull = checkIfTableFull(board)
    if gamewon == True:
        print('You won.')
    elif gamelost == True:
        print('Suck on that. I won.')
    elif tablefull == True:
        print('We tied.')
    if gamewon or gamelost or tablefull:
        gameIsPlaying = False
    if gameIsPlaying == False:
        break
