# chessKnightAttack

Let's ask the question: what is the maximal number of knights that we can place on an n by n chessboard such that each knight is attacking exactly m knights?

For example, on a 3x3 board, we can put at most 8 knights with each knight attacking 2 other knights:

KKK
K.K
KKK

On a 4x4 board, we can put at most 8 knights with each knight attacking one other knight:

KKKK
KKKK
....
....

This program generates a txt file which contains a linear program written in the necessary format
for LPSolve, which is the supplemental software that can solve this linear program.
The board size can be set. 
