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
    EMPTY_CELL = 0x2b1e
    HIT_CELL = 0x0058
    SUNKEN_SHIP = 0x002a
    SHIP = 0x25a0

    def __init__(self, width, height):
        self.width = width
        self.height = height
        # Note that the reference to board is y coorinate first
        self.board = []

        for y in range(height):
            row = []
            for x in range(width):
                row.append(Board.EMPTY_CELL)
            self.board.append(row)

    def __str__(self):
        """
        Returns string representation of the board
        for debuging purposes only, really.
        """
        
        # this draws top of the boarder taking extra spaces into consideration
        ret = chr(0x2554) + chr(0x2550) * (self.width * 2 + 1) + chr(0x2557) + "\n"

        for y in range(self.height):
            # below adds border at the beggining of the line
            ret += chr(0x2551) + " "
            for x in range(self.width):
                ret += chr(self.board[y][x]) + " "
            # adds border at the end of a line plus next line
            ret += chr(0x2551) + "\n"
        
        # and this draws the final line at the bottom of the board
        ret += chr(0x255a) + chr(0x2550) * (self.width * 2 + 1) + chr(0x255d) + "\n"
        return ret

    def is_cell_free(self, x, y):
        """
        Checks if a cell on board is free and returns True if so
        or False if not
        """

        return self.board[y][x] == Board.EMPTY_CELL

    
    def fill(self, number):
        """
        Fills the board randomly with number ships and sets
        ships property of an instance. returns True if success
        or False if not
        """

        if number > self.width * self.height:
            return False

        while number > 0:
            x = randint(0, self.width - 1)
            y = randint(0, self.height -1) 
            if self.is_cell_free(x, y):
                self.board[y][x] = Board.SHIP
                number -= 1

    # def target(self, x, y):
    #     """
    #     process a shot at the board returning False if invalid
    #     i.e. out of range or already shot at or True if valid
    #     """

    #     if x >= self.width or y >= self.height:
    #         return "False - out of range"

    #     cell = ord(self.board[y][x])
    #     if cell != Board.EMPTY_CELL:
    #         return f"Not empty: {chr(cell)}"
    #     elif cell == Board.EMPTY_CELL:
    #         self.board[y][x] = chr(Board.HIT_CELL)
    #         return f"Okay: {chr(cell)}"

        
clear_screen()

player_board = Board(10,10)
player_board.fill(10)
print(player_board)