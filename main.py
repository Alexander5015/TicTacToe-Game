#Tic Tac Toe Game with AI

board = [' ' for x in range(10)]

def insertLetter(letter, pos):
    board[pos] = letter

def spaceIsFree(pos):
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

def playerMove():
    run = True
    while run:
        move = input('Please select a position to place an \'X\' (1-9): ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False;
                    insertLetter('X', move)
                else:
                    print('Sorry, this space is occupied!')
            else:
                print("Please type a number within the range!")
        except:
            print('Please type a number!')


def compMove()):
    pass

def selectRandom(board):
    pass

def isBoardFull(board):
    return board.count() == 1


def main():
    print("Welcome to Tic Tac Toe!")
    printBoard()
    while not(isBoardFull()):
        if not(isWinner(board, 'O')):
            playerMove()
            printBoard()

        else:
            print('Sorry, O won this time!')
            break;

        if not(isWinner(board, 'X')):
            compMove()
            printBoard()

        else:
            print('X won this time! Good Job!')
            break;

    if isBoardFull(board):
        print("Tie Game!")

main()
