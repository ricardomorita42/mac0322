
#rodar easy_install prettytable no terminal para instalar esta lib
from prettytable import PrettyTable

#pega o set e desenha num table
def draw(board):
    max_row = 0
    max_col = 0

    #determina o tamanho da board
    for cell in board:
        if cell[0] > max_row:
            max_row = cell[0]
        if cell[1] > max_col:
            max_col = cell[1]

    #cria um array de 0s com tamanho [max_col+1,max_row+1]
    drawn_board = [[0 for col in range(max_col+1)] for row in range(max_row+1)]

    #Se tiver uma celular, vira 1
    for cell in board:
        drawn_board[cell[0]][cell[1]] = 1

    #desenha bonitinho
    p = PrettyTable()
    for row in drawn_board:
        p.add_row(row)

    print p.get_string(header=False, border=False)
