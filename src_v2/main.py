from labyrinth_cls import Labyrinth
from intro_help_defs import intro
from room_def import Room
from char_def import Character


def main():
    """
    Top-level function call for PyLabyrinth v1.2
    :return: None
    """

    # calls function to generate intro text from file
    charname = intro()

    # used for player initialization
    pre = Room('pre', [-1, -1, -1], [])

    # initializes character and empty notebook
    player = Character(charname, [], pre)

    labyrinth = Labyrinth('firstfloor.txt', player)


if __name__ == main():
    main()
