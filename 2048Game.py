import random
import os

def initialize_game(size=4):
    """Initialize a new game board."""
    board = [[0] * size for _ in range(size)]
    add_new_tile(board)
    add_new_tile(board)
    return board

def add_new_tile(board):
    """Add a new tile (2 or 4) to the board."""
    size = len(board)
    empty_tiles = [(i, j) for i in range(size) for j in range(size) if board[i][j] == 0]
    if empty_tiles:
        i, j = random.choice(empty_tiles)
        board[i][j] = random.choice([2, 4])

def print_board(board):
    """Print the game board."""
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in board:
        print("\t".join(str(num) if num != 0 else '.' for num in row))
    print()

def compress(board):
    """Compress the board to the left."""
    new_board = [[0] * len(board) for _ in range(len(board))]
    for i in range(len(board)):
        pos = 0
        for j in range(len(board)):
            if board[i][j] != 0:
                new_board[i][pos] = board[i][j]
                pos += 1
    return new_board

def merge(board):
    """Merge the board tiles."""
    for i in range(len(board)):
        for j in range(len(board) - 1):
            if board[i][j] == board[i][j + 1] and board[i][j] != 0:
                board[i][j] *= 2
                board[i][j + 1] = 0
    return board

def reverse(board):
    """Reverse the board."""
    new_board = []
    for row in board:
        new_board.append(row[::-1])
    return new_board

def transpose(board):
    """Transpose the board (swap rows and columns)."""
    return [list(row) for row in zip(*board)]

def move_left(board):
    """Move the tiles to the left."""
    board = compress(board)
    board = merge(board)
    board = compress(board)
    return board

def move_right(board):
    """Move the tiles to the right."""
    board = reverse(board)
    board = move_left(board)
    return reverse(board)

def move_up(board):
    """Move the tiles up."""
    board = transpose(board)
    board = move_left(board)
    return transpose(board)

def move_down(board):
    """Move the tiles down."""
    board = transpose(board)
    board = move_right(board)
    return transpose(board)

def is_game_over(board):
    """Check if the game is over."""
    for row in board:
        if 2048 in row:
            print("You win!")
            return True
        if 0 in row:
            return False
    for i in range(len(board)):
        for j in range(len(board) - 1):
            if board[i][j] == board[i][j + 1]:
                return False
            if board[j][i] == board[j + 1][i]:
                return False
    print("Game Over!")
    return True

def main():
    board = initialize_game()
    while True:
        print_board(board)
        if is_game_over(board):
            break
        move = input("Enter move (W/A/S/D for up/left/down/right): ").strip().upper()
        if move in ['W', 'A', 'S', 'D']:
            if move == 'W':
                board = move_up(board)
            elif move == 'A':
                board = move_left(board)
            elif move == 'S':
                board = move_down(board)
            elif move == 'D':
                board = move_right(board)
            add_new_tile(board)

if __name__ == "__main__":
    main()