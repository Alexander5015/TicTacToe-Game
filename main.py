#Tic Tac Toe Game with AI

def insertLetter(board, letter, pos):
    board[pos] = letter

def spaceIsFree(board, pos):
    return board[pos] == ' '

def printBoard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

def isWinner(board, letter):
    # Given a board and a player’s letter, this function returns True if that player has won
    # by scanning every win condition
    return ((board[7] == letter and board[8] == letter and board[9] == letter) or # across the top
    (board[4] == letter and board[5] == letter and board[6] == letter) or # across the middle
    (board[1] == letter and board[2] == letter and board[3] == letter) or # across the bottom
    (board[7] == letter and board[4] == letter and board[1] == letter) or # down the left side
    (board[8] == letter and board[5] == letter and board[2] == letter) or # down the middle
    (board[9] == letter and board[6] == letter and board[3] == letter) or # down the right side
    (board[7] == letter and board[5] == letter and board[3] == letter) or # diagonal
    (board[9] == letter and board[5] == letter and board[1] == letter)) # diagonal

def playerMove(board):
    run = True
    while run:
        move = input('Please select a position to place an \'X\' (1-9): ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(board, move):
                    run = False;
                    insertLetter(board, 'X', move)
                else:
                    print('Sorry, this space is occupied!')
            else:
                print("Please type a number within the range!")
        except:
            print('Please type a number!')


def compMove(board):
    #get moves
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    #set default move
    move = 0

    #Simple 5 step algorithm
    #Check if either player can win on a move and move there
    for letter in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = letter
            if isWinner(boardCopy, letter):
                move = i
                return move
    #Pick Corner
    cornersOpen = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            cornersOpen.append(i)
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    #Pick Center
    if 5 in possibleMoves:
        move = 5;
        return move

    #Any Open Edge
    #Pick Corner
    edgesOpen = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgesOpen.append(i)
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        return move

    return move

def selectRandom(board):
    import random
    rand = random.choice(board)
    return rand

def isBoardFull(board):
    return board.count(' ') == 1

def clearBoard(board):
    board = [' ' for x in range(10)]
    return board

def main():
    board = [' ' for x in range(10)]
    playing = True
    print("Welcome to Tic Tac Toe!")
    while playing:
        printBoard(board)
        while not(isBoardFull(board)):
            if not(isWinner(board, 'O')):
                playerMove(board)
                printBoard(board)

            else:
                print('Sorry, O won this time!')
                break;

            if not(isWinner(board, 'X')):
                move = compMove(board)
                if move != 0:
                    insertLetter(board, 'O', move)
                    print('Computer placed an \'O\' in position', move, ":")
                    printBoard(board)

            else:
                print('X won this time! Good Job!')
                break;

        if isBoardFull(board):
            print("Tie Game!")

        run = True
        while run:
            playAgain = input('Play again? (y/n)')
            if playAgain.lower() == 'y':
                run = False
                board = clearBoard(board)
            elif playAgain.lower() == 'n':
                run = False
                playing = False
            else:
                print("\'" + playAgain + "\'" + " is invalid")
main()
