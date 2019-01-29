from file_parser import parse, getRoom
from io_defs import takeInput


class Floor:
    """
    Updated floor structure. Parent class for individual floor classes.

    :authors: qbp
    :version: 1.0:
    :date: 26-1-2019
    """
    def __init__(self, fpath, player, start_str, specials):
        f = open(fpath, 'r')  # parse rooms
        self.rooms = parse(f)
        f.close()

        self.specials = specials

        self.start = getRoom(self.rooms, start_str)  # init player on floor
        player.setpos(self.start)

        self.end = False
        self.run(player)

    def run(self, player):
        while not self.end:
            current = player.getPos()  # current room

            if not current.enter():
                current.entered()
                print('\n')
            else:
                print("You have been in this room before.\n")

            if self.isSpecial(current.getCoords()):
                self.runSpecial(current.getCoords(), player)
            else:
                player.setpos(getRoom(takeInput(current, player), self.rooms))

    def isSpecial(self, coords):  # check for important rooms
        if coords in self.specials:
            return True
        return False

    def runSpecial(self, coords, player):  # to be overwritten by subclasses
        pass