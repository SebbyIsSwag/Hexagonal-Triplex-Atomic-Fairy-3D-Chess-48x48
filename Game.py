import numpy as np

# Define functions and classes here...

class HexagonalTriplexAtomicFairy3DChessBoard:
    """
    Represents the game board for Hexagonal Triplex Atomic Fairy 3D Chess.
    """
    def __init__(self):
        """
        Initializes the game board with starting positions for all pieces.
        """
        self.board = [[[None for _ in range(48)] for _ in range(48)] for _ in range(48)]
        # Set up the starting positions of all pieces
        board[0, :, :] = ['k', 'z', 'h', 'L', 'F', 'h', 'z', 'k'] * 6
        board[-1, :, :] = ['K', 'Z', 'H', 'L', 'F', 'H', 'Z', 'K'] * 6
        board[1, :, :] = ['s'] * 48
        board[-2, :, :] = ['S'] * 48
        board[2, :, :] = ['p'] * 48
        board[-3, :, :] = ['P'] * 48
        board[3, :, :] = ['W'] * 48
        board[-4, :, :] = ['w'] * 48
        board[4, :, :] = ['A'] * 48
        board[-5, :, :] = ['a'] * 48
        board[5, :, :] = ['m'] * 48
        board[-6, :, :] = ['M'] * 48
        board[6, :, :] = ['g'] * 48
        board[-7, :, :] = ['G'] * 48
        board[7, :, :] = ['c'] * 48
        board[-8, :, :] = ['C'] * 48
        board[8, :, :] = ['e'] * 48
        board[-9, :, :] = ['E'] * 48
        board[9, :, :] = ['d'] * 48
        board[-10, :, :] = ['D'] * 48
        board[10, :, :] = ['u'] * 48
        board[-11, :, :] = ['U'] * 48
        board[11, :, :] = ['s'] * 24 + ['x'] * 24
        board[-12, :, :] = ['S'] * 24 + ['X'] * 24
        board[12, :, :] = ['p'] * 24 + ['y'] * 24
        board[-13, :, :] = ['P'] * 24 + ['Y'] * 24
        board[13, :, :] = ['s'] * 24 + ['k'] * 24
        board[-14, :, :] = ['S'] * 24 + ['K'] * 24
        board[14, :, :] = [' '] * 48
        board[-15, :, :] = [' '] * 48
        board[15, :, :] = ['L'] * 24 + ['w'] * 24
        board[-16, :, :] = ['l'] * 24 + ['W'] * 24

        # ...
    
    def is_legal_move(self, piece, start_pos, end_pos):
        """
        Checks whether a given move is legal on the current board.
        """
        # Implement the rules for legal moves
        # ...
    
    def make_move(self, piece, start_pos, end_pos):
        """
        Updates the board with the given move, assuming it is legal.
        """
        # Make the move
        # ...
    
    def is_capture(self, start_pos, end_pos):
        """
        Checks whether a move results in a capture.
        """
        # Check whether the end position is occupied by an opposing piece
        # ...
    
    def is_check(self, color):
        """
        Checks whether the given player is in check.
        """
        # Check whether any of the opponent's pieces can attack the player's king
        # ...
    
    def is_checkmate(self, color):
        """
        Checks whether the given player is in checkmate.
        """
        # Check whether the player's king is in check and has no legal moves
        # ...
    
    def is_stalemate(self, color):
        """
        Checks whether the given player is in stalemate.
        """
        # Check whether the player has no legal moves and is not in check
        # ...
    
    def is_draw(self):
        """
        Checks whether the game is a draw due to threefold repetition or the
        50-move rule.
        """
        # Check for threefold repetition and the 50-move rule
        # ...


class Player:
    """
    Represents a player in the game.
    """
    def __init__(self, color):
        """
        Initializes a player with the given color (either "white" or "black").
        """
        self.color = color
    
    def get_move(self, board):
        """
        Prompts the player to enter a move and returns it.
        """
        # Get input from the player
        # ...
        return move


def create_board():
    """
    Creates a new game board with the starting positions of all pieces.
    """
    board = HexagonalTriplexAtomicFairy3DChessBoard()
    # Set up the starting positions of all pieces
    # ...
    return board


def print_board(board):
    """
    Prints the current state of the game board.
    """
    # Print the board to the console
    # ...


def make_move(board, move):
    """
    Makes the given move on the board.
    """
    # Check if move is legal
    # ...
    # Move piece
    # ...
    # Check for capture
    # ...
    return True


def checkmate(board, color):
    """
    Checks whether the given player is in checkmate.
    """
    # Check whether the player is in checkmate
    # ...
    return False


def checkmate_capture(board, color):
    """
    Checks whether the given player is in checkmate-capture.
    """
    # Check whether the player is in checkmate-capture
    # ...
    return False
 
 
 def capture_made(board):
    """
    Checks if a capture was made in the last move.
    """
    last_move = get_last_move(board)
    if last_move is None:
        return False
    start_pos, end_pos = last_move
    start_piece = board.get_piece(start_pos)
    end_piece = board.get_piece(end_pos)
    if end_piece is None or end_piece.color == start_piece.color:
        return False
    return True
def in_check(board, color):
    """
    Checks whether the given player is in check.
    """
    # Get the position of the player's king
    king_pos = get_king_pos(board, color)
    
    # Check whether any of the opponent's pieces can attack the king
    opponent_moves = get_all_moves(board, get_opponent_color(color))
    for start_pos, end_pos in opponent_moves:
        if end_pos == king_pos:
            return True
    
    return False

