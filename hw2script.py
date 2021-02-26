#chessboard size, size x size
boardSize = 4
# desired number of knights each piece is attacked by
attackingKnights = 1

fh = open("hw2_lp.txt", 'w')

# writing the objective function
#
# need to maximize the number of knights
objectiveString = 'max: '
for i in range(1, boardSize + 1):
    for j in range(1, boardSize + 1):
        # if not the last board position to check
        if (i + j) != (boardSize * 2):
            objectiveString += 'x_' + str(i) + '_' + str(j) + " + "
# printing the final board coordinate
objectiveString += 'x' + '_' + str(boardSize) + '_' + str(boardSize) + ';\n'
fh.write(objectiveString)

# writing the constraints
#
# each piece can only attack (attackingKnights) number of pieces
possibleMoves = [[1, 2],[1, -2],[-1, 2],[-1, -2],[2, 1],[2, -1],[-2, 1],[-2, -1]]
# looping through every board position
for i in range(1, boardSize + 1):
    for j in range(1, boardSize + 1):
        # constraint string for every board position
        knightAttackersString = ''
        # finding legal positions
        for x in possibleMoves:
            # is legal space, and not the last possible move to check
            if (i + x[0] >= 1) and (j + x[1] >= 1) and (i + x[0] <= boardSize) and (j + x[1] <= boardSize):
                knightAttackersString += '+' + 'x_' + str(i + x[0]) + '_' + str(j + x[1])
        # if there exist legal attacker spaces
        if knightAttackersString != '':
            # copying the LHS to handle the differing RHSs
            knightAttackersString2 = knightAttackersString
            knightAttackersString2 += ' <= ' + str(attackingKnights - 8) + '*' + 'x_' + str(i) + '_' + str(j) + ' +8'+ ';\n'
            knightAttackersString += ' >= ' + str(attackingKnights) + '*' + 'x_' + str(i) + '_' + str(j) + ';\n'
        fh.write(knightAttackersString2)
        fh.write(knightAttackersString)


# variable declarations
#
# One for each square of the board
# Binary, 0 for no piece on the square, 1 for piece on the square
var_string = 'bin '
for i in range (1, boardSize + 1):
    for j in range (1, boardSize + 1):
        # if on final board coordinate, don't print
        if (i + j) != (boardSize * 2):
            var_string += 'x_' + str(i) + '_' + str(j) + ', '
# printing the final board coordinate
var_string += 'x_' + str(boardSize) + '_' + str(boardSize) + ';'
fh.write(var_string)

fh.close()
