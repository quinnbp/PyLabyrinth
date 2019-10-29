from char_def import Character
from notebook_def import Notebook
from room_def import Room
from intro_help_defs import intro

from first_floor import firstFloor
from second_floor import secondFloor
from third_floor import thirdFloor


def main():
    """
    Top-level main function, initializes PyLabyrinth, and calls each floor function

    :return: None
    """
    # calls function to generate intro text from file
    charname = intro()

    # used for player initialization
    pre = Room('pre', [-1, -1, -1], [])

    # initializes character and empty notebook
    notebook = Notebook([], [], [], [])
    player = Character(charname, [], pre, notebook)

    # calls floor functions in order
    player = firstFloor(player, '110')  # TODO: update floor functions to inheritance structure
    player = secondFloor(player, '111')
    thirdFloor(player, '002')
    # further floors


main()
