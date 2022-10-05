import functions as func

print('Игра Крестики-нолики для 2-х игроков.')
board = list(range(1, 10))
game_over = False
player1 = True
while game_over == False:
    func.print_board(board)
    if player1 == True:
        symbol = '\u001B[34mX\u001b[0m'
        move = int(input('Ход \u001B[34mигрока 1\u001b[0m: ')) # ANSI .NET color blue \u001B[34m
    else:
        symbol = '\u001B[31mO\u001b[0m'
        move = int(input('Ход \u001B[31mигрока 2\u001b[0m: ')) # ANSI .NET color red \u001B[31m
    func.make_move(move, symbol, board)
    win = func.find_winner(board)
    if win != '':
        game_over = True
        func.print_board(board)
    else:
        game_over = False
    player1 = not(player1)
    print(f'Победил', func.find_winner(board))
