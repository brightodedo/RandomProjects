def display_board(x):
    """
    This function displays the board for the X and O game before and after each turn.
"""
    #prints the game table 
    print('|',x[0],'|',x[1],'|',x[2],'|')
    print('|',x[3],'|',x[4],'|',x[5],'|')
    print('|',x[6],'|',x[7],'|',x[8],'|')
    

def turn(y):
    """
    Decides whose turn it is and allows them to play.
    returns True if game is over
"""
    #X's turn
    if (y.count('x') == y.count('o')):
        #x inputs and check x's input
        value = valid_location('X',y)
        #add x's table to data
        y[value] = 'x'
        #display table
        display_board(y)
        #check if X won
        checker = check_board(y)
        #returns value to stop game
        if checker == True:
            return checker
    #check if game is a draw
    elif y.count('x') == 5:
        print('   Game is a draw')
        return True
    #O's turn
    elif (y.count('x') > y.count('o')):
        #o inputs and check o's input
        value = valid_location('O',y)
        #add o's table to data
        y[value] = 'o'
        #display table
        display_board(y)
        #check if O won
        checker = check_board(y)
        #returns value to stop game
        if checker == True:
            return checker

def check_board(a):
    """
    This function checks if the game is won.
    displays the winner of the game
    returns True if game is won.
"""
    #check horizontal rows
    if (a[0] == a[1] == a[2] == 'x') or (a[0] == a[1] == a[2] == 'o'):
        print(a[0], 'WINS')
        return True 
    if (a[3] == a[4] == a[5] == 'x') or (a[3] == a[4] == a[5] == 'o'):
        print(a[3], 'WINS')
        return True
    if (a[6] == a[7] == a[8] == 'x') or (a[6] == a[7] == a[8] == 'o'):
        print(a[6], 'WINS')
        return True
    #check vertical rows
    if (a[0] == a[3] == a[6] == 'x') or (a[0] == a[3] == a[6] == 'o'):
        print(a[0], 'WINS')
        return True
    if (a[1] == a[4] == a[7] == 'x') or (a[1] == a[4] == a[7] == 'o'):
        print(a[1], 'WINS')
        return True
    if (a[2] == a[5] == a[8] == 'x') or (a[2] == a[5] == a[8] == 'o'):
        print(a[2], 'WINS')
        return True
    #check diagnoals
    if (a[0] == a[4] == a[8] == 'x') or (a[0] == a[4] == a[8] == 'o'):
        print(a[0], 'WINS')
        return True
    if (a[2] == a[4] == a[6] == 'x') or (a[2] == a[4] == a[6] == 'o'):
        print(a[2], 'WINS')
        return True

def play(z):
    """
    starts the game
"""
    #if cont is True game is over
    cont = turn(z)
    #if cont is None then game isn't over
    while cont == None:
        cont = turn(z)

def valid_location(j,b):
    """
    takes in j as player and b as list.
    checks if input is valid
    returns valide input
"""
    validity = False
    while not False:
        value = int(input(j+"'s turn to play, choose location: "))
        value -= 1
        if b[value] == '-':
            validity = True
            return value
        else:
            continue

def main():
    affirm = False
    while not affirm:
        #defines board values
        board_values = ['-','-','-','-','-','-','-','-','-']
        #displays board
        display_board(board_values)
        #game plays
        play(board_values)
        #check if game wants to continue
        answer = input("Do you want to play again {y is yes, anything else is no}: ")
        if answer != 'y':
            affirm = True
            

if __name__ == "__main__":
    main()
