from floor_def import Floor
from io_defs import takeInput
from file_parser import getRoom


class FirstFloor(Floor):
    """
    Class definition for the first floor of PyLabyrinth. Super: floor_def.py

    :authors: qbp
    :version: 1.0:
    :date: 26-1-2019
    """
    def __init__(self, player):
        fpath = "floor_files/firstfloor.txt"
        start_str = '110'
        specials = [[2, 1, 0]]

        super().__init__(fpath, player, start_str, specials)

    def runSpecial(self, coords, player):
        if coords == [2, 1, 0]:  # if in end room
            if 'lantern' in player.getInv():  # check for lantern
                player.getPos().switchToAlt()
                player.getPos().addToExits('e')  # add floor exit
                result = takeInput(player.getPos(), player)  # get input
                if result == [3, 1, 0]:  # if player leaves
                    self.end = True  # escapes the loop
                else:
                    newroom = getRoom(result, self.rooms)  # if player doesn't leave
                    player.setPos(newroom)
            else:
                newroom = getRoom(takeInput(player.getPos(), player), self.rooms)  # if player doesn't have lantern
                player.setpos(newroom)
