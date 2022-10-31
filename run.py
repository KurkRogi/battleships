# Battleships terminal text game
import os
import math
from random import randint

def clear_screen():
    """
    Clears screen. Solution from # https://stackoverflow.com/a/2084628
    """
    os.system('cls' if os.name == 'nt' else 'clear')

class Board:
    """
    Class for a playing board.
    """
    
    # Unicodes for the board cells
    # Alternative empty cell is 0x2b1e - a dot
    EMPTY_CELL = 0x223c
    HIT_CELL = 0x0058
    SUNKEN_SHIP = 0x002a
    SHIP = 0x25a0
    
    # Unicodes for border: T = top, L = left, R = right, M = middle, B = bottom
    BORDER_TL = 0x2554 
    BORDER_TM = 0x2550
    BORDER_TR = 0x2557
    BORDER_BL = 0x255a
    BORDER_BM = 0x2550
    BORDER_BR = 0x255d
    BORDER_LM = 0x2551
    BORDER_RM = 0x2551

    def __init__(self, width, height):
        self.width = width
        self.height = height
        # Note that the reference to board is y coorinate first
        self.board = []
        self.ships_left = 0

        # Create empty game board
        for y in range(height):
            row = []
            for x in range(width):
                row.append(Board.EMPTY_CELL)
            self.board.append(row)

    def get_board_line(self):
        """
        Generator funtion returning a string representation of a single line
        of the board
        """
        for i in range(-1, self.height + 1):
            if i == -1:
                # top border line of the board
                yield (chr(Board.BORDER_TL) 
                    + chr(Board.BORDER_TM) * (self.width * 2 + 1)
                    + chr(Board.BORDER_TR)
                    )
            elif i == self.height:
                # bottom border line
                yield (chr(Board.BORDER_BL) 
                    + chr(Board.BORDER_BM) * (self.width * 2 + 1)
                    + chr(Board.BORDER_BR)
                    )
            else:
                # actual line on the board starting and ending with borders and spaced with white space
                yield (chr(Board. BORDER_LM) + " "
                    + " ".join(chr(x) for x in self.board[i])
                    + " " + chr(Board.BORDER_RM)
                    )

    def __str__(self):
        """
        Returns visual string representation of the board
        for debuging purposes only, really.
        """
        return "\n".join(x for x in self.get_board_line())
        

    def is_cell_free(self, x, y):
        """
        Checks if a cell on board is free and returns True if so
        """

        return self.board[y][x] == Board.EMPTY_CELL
    
    def fill(self, number):
        """
        Fills the board randomly with number ships and sets
        ships_left property of an instance. returns number of ships if success
        or False if not
        """

        if number > self.width * self.height:
            return False

        self.ships_left = number
        while number > 0:
            x = randint(0, self.width - 1)
            y = randint(0, self.height -1) 
            if self.is_cell_free(x, y):
                self.board[y][x] = Board.SHIP
                number -= 1
        return self.ships_left

def get_integer(min = 1, max = 10, message = "Please enter a number [1-10]: "):
    """
    Prompt player to enter an integer within a range
    """
    while True:
        try:
            integer = int(input(message + "\n"))
            if integer < min or integer > max:
                raise ValueError(f"{integer} is out of range [{min}-{max}]")
            break
        except ValueError as error:
            print("***", end = " ")
            print(error, end = "\n\n")
    
    return integer


def main():
    
    while True:
        clear_screen()
        print("Welcome to the Battleships game")
        print("-" * 31 + "\n")
        
        board_size = get_integer(2, 10, "Please enter the board size [2-10]")
        player_board = Board(board_size, board_size)
        opponent_board = Board(board_size, board_size)
        
        number_of_ships = get_integer(1, board_size ** 2, f"How many ships do you want? [1-{board_size ** 2}]")
        player_board.fill(number_of_ships)
        opponent_board.fill(number_of_ships)

        print(player_board)

        check = get_integer()
        print(check)
        break
main()
