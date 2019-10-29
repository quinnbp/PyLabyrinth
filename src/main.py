from labyrinth_cls import Labyrinth
from intro_help_defs import intro
from char_def import Character


def main():
    """
    Top-level function call for PyLabyrinth v1.2
    :return: None
    """

    # calls function to generate intro text from file
    charname = intro()

    # initializes character
    player = Character(charname, [], 110)  # puts player in start room

    labyrinth = Labyrinth('demo.txt', player)
    labyrinth.play()


main()
