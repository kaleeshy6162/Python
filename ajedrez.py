#Las minusculas son las negras.
#Las mayusculas son las blancas.
#Los ceros son peones.
#r=torre, n=caballo. b=alfil, q=reina, k=rey.

chess_board = [
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
]
print(chess_board)
chess_board[7][1] = 0
#Casilla original del cabllo esta vacia. 
chess_board[5][3] = "N"
#Nueva posición del caballo.
print(chess_board[7][1])
print(chess_board[5][3])
