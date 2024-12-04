#! python3

import random, copy

coordinates = ['NW', 'N', 'NE', 'W', 'M', 'E', 'SW', 'S', 'SE']
winConditions = [
                ['NW', 'N', 'NE'],
                ['W', 'M', 'E'],
                ['SW', 'S', 'SE'],
                ['NW', 'W', 'SW'],
                ['N', 'M', 'S'],
                ['NE', 'E', 'SE'],
                ['NW', 'M', 'SE'],
                ['NE', 'M', 'SW']
                ]



def drawBoard(board):
    print(board['NW'] + '|' + board['N'] + '|' + board['NE'])
    print('-----')
    print(board['W'] + '|' + board['M'] + '|' + board['E'])
    print('-----')
    print(board['SW'] + '|' + board['S'] + '|' + board['SE'])

def choosePlayerChar():
    char = ''
    while not (char == 'X' or char == 'O'):
        print('Vil du spille X eller O?')
        char = input().upper()

    if char == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whosFirst():
    if random.randint(0,1) == 0:
        return 'computer'
    else:
        return 'player'

def playAgain():
    print('En runde til?')
    return not input().lower().startswith('n')

def occupySpace(board, char, space):
    board[space] = char

def isWinner(board, char):
    for row in winConditions:
        if all(board[space] == char for space in row):
            return True
    return False


def isEmptySpace(board, space):
    return board[space] == ' '

def playerChooseSpace(board):
    chosenSpace = ' '
    potentialSpaces = []
    for coord in coordinates:
        if isEmptySpace(board, coord):
            potentialSpaces.append(coord)
    while chosenSpace not in potentialSpaces:
        print('Hvor vil du legge neste brikke? Dine valg er:')
        print(*potentialSpaces)
        chosenSpace = input().upper()
    return chosenSpace


def computerChooseSpace(board, computerChar):
    if computerChar == 'X':
        playerChar = 'O'
    else:
        playerChar = 'X'

    winMove = primarySpaceBot(board, computerChar)
    if winMove is not None:
        return winMove
    blockMove = primarySpaceBot(board, playerChar)
    if blockMove is not None:
        return blockMove
    return secondarySpaceBot(board)

def primarySpaceBot (board, char):
    for space in coordinates:
        clone = copy.copy(board)
        if isEmptySpace(clone, space):
            occupySpace(clone, char, space)
            if isWinner(clone, char):
                return space

def secondarySpaceBot(board):
    #sjekk midten, så hjørner, så sidene?
    middle = 'M'
    corner = chooseRandomSpace(board, ['NW', 'NE', 'SW', 'SE'])
    side = chooseRandomSpace(board, ['N', 'E', 'S', 'W'])

    if isEmptySpace(board, middle):
        return middle
    elif corner is not None:
        return corner
    else:
        return side

def chooseRandomSpace(board, spaceList):
    potentialSpaces = []
    for space in spaceList:
        if isEmptySpace(board, space):
            potentialSpaces.append(space)
    if len(potentialSpaces) != 0:
        return random.choice(potentialSpaces)
    else:
        return None

def isBoardFilled(board):
    for space in coordinates:
        if isEmptySpace(board, space):
            return False
    return True


print('Nå skal vi spille tre på rad!!')

while True:
    board = {coord: ' ' for coord in coordinates}
    playerChar, computerChar = choosePlayerChar()
    if playerChar == 'X':
        playerTurn = True
        print('Du begynner')
    else:
        playerTurn = False
        print('Boten begynner')
    gameOngoing = True

    while gameOngoing:
        if playerTurn:
            drawBoard(board)
            space = playerChooseSpace(board)
            occupySpace(board, playerChar, space)
            if isWinner(board, playerChar):
                drawBoard(board)
                print('Grattis, du vant mot en 40-linjers bot')
                gameOngoing = not gameOngoing
            else:
                if isBoardFilled(board):
                    drawBoard(board)
                    print('Vel, du tapte ikke i alle fall')
                    break
                else:
                    playerTurn = not playerTurn
        else:
            space = computerChooseSpace(board, computerChar)
            occupySpace(board, computerChar, space)
            if isWinner(board, computerChar):
                drawBoard(board)
                print('Du tapte mot muligens verdens dummeste bot')
                gameOngoing = not gameOngoing
            else:
                if isBoardFilled(board):
                    drawBoard(board)
                    print('Så vidt du unngikk å tape')
                    break
                else:
                    playerTurn = not playerTurn
                    
    if not playAgain():
        break
            
