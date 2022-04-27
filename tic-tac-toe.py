### Author: Chris Bitsch
### Assignement: Week 2 Solo Submission: Tic-Tac-Toe

def main():
    # Print the starting board, and initialize starting variables
    grid = [1,2,3,4,5,6,7,8,9]
    print_board(grid)
    game_won = False

    # Initalize the loop
    while (game_won == False):
        
        # Define player X's turn
        x_input = int(input("X's turn to choose a square (1-9): "))
        input_map('X', x_input, grid)
        print_board(grid)
        if test_win(grid) == True:
            game_won == True
            print("X wins!")
            exit()

        # Define player O's turn
        o_input = int(input("O's turn to choose a square (1-9): "))
        input_map('O', o_input, grid)
        print_board(grid)
        if test_win(grid) == True:
            game_won == True
            print("O wins!")
            exit()

def print_board(board):
    # Prints the array that stores board values with some formatting
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print("-----")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print("-----")
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()

def input_map(symbol, value, board):
    # Checks to see if the specified location is already occupied with a symbol, and if not, it places the appropriate symbol down
    if board[value - 1] != 'X' or 'O':
        board[value - 1] = symbol
    else:
        print("There's already a symbol there, you lost your turn")

def test_win(board):
    # Checks if there is a winning match, there is probably a better way to do this, but this is all by brain could 
    # think of, and it works so hey, if it aint broke don't fix it
    if (board[0] is board[1] is board[2]) or (board[3] is board[4] is board[5]) or (board[6] is board[7] is board[8]) or \
        (board[0] is board[3] is board[6]) or (board[1] is board[4] is board[7]) or (board[2] is board[5] is board[8]) or \
        (board[0] is board[4] is board[8]) or (board[2] is board[4] is board[6]):
        return True

if __name__ == "__main__":
    main()