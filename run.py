"""Battleships terminal text game"""

import os
import sys
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

    # Unicodes for border. Key: T = top, L = left, R = right,
    #                           M = middle, B = bottom
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
        # Create board as a list or lists filled with empty cells
        self.board = [[Board.EMPTY_CELL] * self.width for x in range(self.height)]
        self.ships_left = 0

    def get_board_line(self, hide_ships=False):
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
                # actual line on the board starting and ending with borders
                # and spaced with white space + " ".join(chr(x) for x in self.board[i])
                # Indexing tuple with True/False is apparently not very
                # Pythonic but still better
                # than next ternary operator
                yield (chr(Board. BORDER_LM) + " "
                       + " ".join(chr(x) if x != Board.SHIP
                       else chr((Board.SHIP, Board.EMPTY_CELL)[hide_ships]) for x in self.board[i])
                       + " " + chr(Board.BORDER_RM)
                       )

    def __str__(self, hide_ships=False):
        """
        Returns visual string representation of the board
        for debuging purposes only, really.
        """
        return "\n".join(x for x in self.get_board_line(hide_ships))

    def is_cell_free(self, x_coord, y_coord):
        """
        Checks if a cell on board is free and returns True if so
        """

        return self.board[y_coord][x_coord] == Board.EMPTY_CELL

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
            x_coord = randint(0, self.width - 1)
            y_coord = randint(0, self.height -1)
            if self.is_cell_free(x_coord, y_coord):
                self.board[y_coord][x_coord] = Board.SHIP
                number -= 1
        return self.ships_left


def get_integer(min_value=1, max_value=10, message="Please enter a number [1-10]: "):
    """
    Prompt player to enter an integer within a range
    """
    while True:
        try:
            integer = int(input(message + "\n"))
            if integer < min_value or integer > max_value:
                raise ValueError(f"{integer} is out of range [{min_value}-{max_value}]")
            break
        except ValueError as error:
            print(f"*** {error} \n")

    return integer


def get_coordinates(opponent_board):
    """
    Prompt player to enter shot coordinates
    and return them as a tuple after verification
    function is ready for non-square boards in the future
    """
    min_x, max_x = 1, opponent_board.width
    min_y, max_y = 1, opponent_board.height
    message = f"Please enter your target's coorinates separated by comma,\
\nhorizontal first [1-{max_x}],[1-{max_y}]"

    while True:
        try:
            data = input(message + "\n").strip().replace(" ", "").split(",")
            if len(data) != 2:
                raise ValueError("Enter 2 numbers separated by comma")
            x_coord = int(data[0])
            y_coord = int(data[1])
            if x_coord < min_x or x_coord > max_x:
                raise ValueError(f"First coordinate must be between {min_x} and {max_x}")
            if y_coord < min_y or y_coord > max_y:
                raise ValueError(f"Second coordinate must be between {min_y} and {max_y}")
            break
        except ValueError as error:
            print(f"*** {error} \n")

    return x_coord, y_coord


def game_setup():
    """
    Set up game parameters and returns them as a tuple
    (board_size, ship_number)
    """
    clear_screen()
    print("Welcome to the Battleships game\n"
          + "-" * 31 + "\n\n"
          + "*** Game setup")

    # Find out what's the size of board player wants
    board_size = get_integer(2, 10, "\nPlease enter the board size [2-10]")

    # Find how many ships on the board the player wants
    number_of_ships = get_integer(1, board_size ** 2,
                                  f"\nHow many ships do you want? [1-{board_size ** 2}]")

    return (board_size, number_of_ships)


def game_instructions(plr_score, opp_score):
    """
    Display game instructions and current score
    p for player and o for opponent
    """
    clear_screen()
    print("Insructions:\n" + "-" * 12)
    print(f"{chr(Board.EMPTY_CELL)} is an empty cell")
    print(f"{chr(Board.SHIP)} is an ship")
    print(f"{chr(Board.HIT_CELL)} was already targeted")
    print(f"{chr(Board.SUNKEN_SHIP)} is a sunken ship\n")

    print("Your board is on left, opponent's on right")

    print(f"There {('are', 'is')[plr_score == 1]} "
          + f"still {plr_score} ship{('s', '')[plr_score == 1]} on your "
          + f"board and {opp_score} on oponent's")

    print("Top left corner coordinates are 1,1")


def game_display_boards(player_board, opponent_board):
    """
    Display both player and opponent board next to each other
    """
    for plr_line, opp_line in zip(player_board.get_board_line(),
                                  opponent_board.get_board_line(True)):
        print(plr_line + " " * 5 + opp_line)


def game_shot(brd, coords):
    """
    Place shot in coords on board brd and returns
    True if succesfull or False if cell already targeted
    and message to player
    """
    x_coord, y_coord = coords
    x_coord -= 1
    y_coord -= 1
    result = False
    message = ""
    cell = brd.board[y_coord][x_coord]

    if cell == Board.EMPTY_CELL:
        result = True
        brd.board[y_coord][x_coord] = Board.HIT_CELL
        message = "missed."
    elif cell == Board.HIT_CELL:
        message = "already targeted this coordinates"
    elif cell == Board.SUNKEN_SHIP:
        message = "already sunk this ship"
    else:
        result = True
        brd.board[y_coord][x_coord] = Board.SUNKEN_SHIP
        message = "hit a ship!"
        brd.ships_left -= 1

    return result, message


def main():
    """ main function runing game loop"""

    while True:
        # game loop including game setup
        board_size, number_of_ships = game_setup()

        player_board = Board(board_size, board_size)
        opponent_board = Board(board_size, board_size)
        player_board.fill(number_of_ships)
        opponent_board.fill(number_of_ships)

        while True:
            # game duel loop

            # Ask for coords untill a ship or empty cell is hit
            result = False
            message_player = ""
            while not result:
                clear_screen()
                game_instructions(player_board.ships_left,
                                opponent_board.ships_left)
                game_display_boards(player_board, opponent_board)
                if message_player:
                    print(f"You {message_player}")
                result, message_player = game_shot(opponent_board,
                                                get_coordinates(opponent_board))

            # Same procedure for computer opponent but only valid shots
            # need to display
            result = False
            while not result:
                result, message = game_shot(player_board,
                                            (randint(1, board_size),
                                            randint(1, board_size)))
            clear_screen()
            print(f"You {message_player}")
            print(f"Opponent {message}")
            game_display_boards(player_board, opponent_board)

            end_game = False

            # check if it's time to end the game
            if player_board.ships_left == 0 or opponent_board.ships_left == 0:
                end_game = True

            # Decide what message to diplay
            if player_board.ships_left == 0 and opponent_board.ships_left == 0:
                print("It's a draw!")
            elif player_board.ships_left == 0:
                print("You've lost!")
            elif opponent_board.ships_left == 0:
                print("You've won!")

            # Check if player wants to continue
            if input("Press ENTER / RETURN o type 'quit' to exit gamme\n") == "quit":
                print("Sorry to see you leave, bye!")
                sys.exit()

            # Breake out to main game loop if all ships gone
            if end_game:
                break


main()
