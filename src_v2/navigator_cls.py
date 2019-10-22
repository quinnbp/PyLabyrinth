from intro_help_defs import directions
from room_def import Room


class Navigator:
    """
    Navigator class handles taking and sanitizing user input, and delegating input
    """
    def __init__(self):
        # error responses
        self.invalid = "That's not a valid option."

        # navigation fail responses
        self.prompt = "How would you like to proceed? "
        self.badexit = "There is no exit in that direction."

        # take fail responses
        self.room_noitem = "There is no such item in this room."
        self.char_noitem = "You don't have that item."
        self.goodtake = "You take the "
        self.gooddrop = "You drop the "

        # valid verb choices
        self.directionacts = ['n', 'e', 's', 'w', 'north', 'east', 'south', 'west']  # TODO: add down/up?
        self.takeacts = ['take']
        self.dropacts = ['drop']
        self.useacts = ['use']
        self.lookacts = ['look']
        self.helpacts = ['help']

    def takeInput(self, currentRoom, player):
        """
        Takes player input and delegates to appropritate handler
        :param player: Character representation of the player object (see char_def)
        :param currentRoom: Room object represeting current position
        :return: Int representation of coordinates of new room
        """
        usrin = input(self.prompt).split()  # creates list of user input

        if usrin[0] == 'go':  # strip 'go' as direction act
            usrin = usrin[1:]

        # switch for all valid verb cases
        if usrin[0] in self.directionacts:
            return self.navigate(currentRoom, player, usrin[0])  # returns new room coords
        elif usrin[0] in self.takeacts:
            return self.playerTake(currentRoom, player, usrin[1:])
        elif usrin[0] in self.dropacts:
            return self.playerDrop(currentRoom, player, usrin[1:])
        elif usrin[0] in self.useacts:
            pass
            # TODO: process use
        elif usrin[0] in self.helpacts:
            directions()  # print help and recurse
            return self.takeInput(currentRoom, player)
        elif usrin[0] in self.lookacts:
            currentRoom.printRoom()
            return self.takeInput(currentRoom, player)
        else:
            print(self.invalid)  # catch for bad inputs
            return self.takeInput(currentRoom, player)

    def navigate(self, currentRoom, player, direction):
        if len(direction) > 1:  # reduce 'north' to 'n', etc
            direction = direction[0]

        if direction not in currentRoom.getExits():  # catch for player input bad exit
            print(self.badexit)
            return self.takeInput(currentRoom, player)

        newcoords = currentRoom.getXyz()  # int representation of coords
        if direction == 'n':  # modify coords to represent travel
            newcoords += 10
        elif direction == 's':
            newcoords -= 10
        elif direction == 'e':
            newcoords += 100
        elif direction == 'w':
            newcoords -= 100

        return newcoords

    def playerTake(self, currentRoom, player, objectList):  # TODO: condense take/drop to one fxn
        if len(objectList) == 0:  # fail case, invalid input
            print(self.invalid)
        else:  # if there is an item, assign it
            item = objectList[0]

            if item not in currentRoom.getContents():  # fail case, unknown object
                print(self.room_noitem)
            else:  # success case, object in room
                print(self.goodtake + item + ".")  # respond to player
                currentRoom.removeItem(item)
                player.addToInv(item)

        return self.takeInput(currentRoom, player)

    def playerDrop(self, currentRoom, player, objectList):
        if len(objectList) == 0:  # fail case, invalid input
            print(self.invalid)
        else:  # if there is an item, assign it
            item = objectList[0]

            if item not in player.getInv():  # fail case, unknown object
                print(self.char_noitem)
            else:  # success case, object in player inv
                print(self.gooddrop + item + ".")  # respond to player
                player.dropFromInv(item)
                currentRoom.addToContents(item)  # this may not work?

        return self.takeInput(currentRoom, player)





