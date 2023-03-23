board = [['', '', '', '', '', '', ''],
         ['', '', '', '', '', '', ''],
         ['', '', '', '', '', '', ''],
         ['', '', '', '', '', '', ''],
         ['', '', '', '', '', '', ''],
         ['', '', '', '', '', '', '']]

def print_board(board):
    # Create the board with | as a seperator
    for row in board:
        print('|' + '|'.join([f' {cell} ' if cell else '   ' for cell in row]) + '|')

def check_win(board, player):
    # Check horizontal
    for row in board:
        if ''.join(row).count(player * 4) >= 1:
            return True
    # Check vertical
    for col in range(7):
        if ''.join([board[row][col] for row in range(6)]).count(player * 4) >= 1:
            return True
    # Check diagonal (top-left to bottom-right)
    for row in range(3):
        for col in range(4):
            if ''.join([board[row+i][col+i] for i in range(4)]).count(player * 4) >= 1:
                return True
    # Check diagonal (top-right to bottom-left)
    for row in range(3):
        for col in range(3, 7):
            if ''.join([board[row+i][col-i] for i in range(4)]).count(player * 4) >= 1:
                return True
    return False

def get_move(player):
    while True:
        try:
            col = int(input(f'Player {player}, choose a column (1-7): ')) - 1
            if col < 0 or col > 6:
                raise ValueError
            return col
        except ValueError:
            print('Invalid input. Please enter a number between 1 and 7.')

def main():
    player = 'X'
    while True:
        print_board(board)
        col = get_move(player)
        for row in range(5, -1, -1):
            if board[row][col] == '':
                board[row][col] = player
                break
        else:
            print('That column is already full. Please choose another column.')
            continue
        if check_win(board, player):
            print_board(board)
            print(f'Player {player} wins!')
            break
        if all(cell != '' for row in board for cell in row):
            print_board(board)
            print('It\'s a tie!')
            break
        player = 'O' if player == 'X' else 'X'

main()
