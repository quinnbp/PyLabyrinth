from intro_help_defs import directions
from room_def import Room


class Navigator:
    """
    Navigator class handles taking and sanitizing user input, and delegating input
    """
    def __init__(self):
        # data references for display prompts
        self.prompt = "How would you like to proceed? "
        self.invalid = "That's not a valid option."
        self.badexit = "There is no exit in that direction."

        # valid verb choices
        self.directionacts = ['n', 'e', 's', 'w', 'north', 'east', 'south', 'west']  # TODO: add down/up?
        self.takeacts = ['take']
        self.dropacts = ['drop']
        self.useacts = ['use']
        self.lookacts = ['look']
        self.helpacts = ['help']

    def takeInput(self, currentRoom):
        """
        Takes player input and delegates to appropritate handler
        :param currentRoom: Room object represeting current position
        :return: Int representation of coordinates of new room
        """
        usrin = input(self.prompt).split()  # creates list of user input

        if usrin[0] == 'go':  # strip 'go' as direction act
            usrin = usrin[1:]

        # switch for all valid verb cases
        if usrin[0] in self.directionacts:
            return self.navigate(currentRoom, usrin[0])  # returns new room coords
        elif usrin[0] in self.takeacts:
            pass
            # TODO: process take
        elif usrin[0] in self.dropacts:
            pass
            # TODO: process drop
        elif usrin[0] in self.useacts:
            pass
            # TODO: process use
        elif usrin[0] in self.helpacts:
            directions()  # print help and recurse
            return self.takeInput(currentRoom)
        else:
            print(self.invalid)  # catch for bad inputs
            return self.takeInput(currentRoom)

    def navigate(self, currentRoom, direction):
        if len(direction) > 1:  # reduce 'north' to 'n', etc
            direction = direction[0]

        if direction not in currentRoom.getExits():  # catch for player input bad exit
            print(self.badexit)
            return self.takeInput(currentRoom)

        newcoords = currentRoom.xyz  # int representation of coords
        if direction == 'n':  # modify coords to represent travel
            newcoords += 10
        elif direction == 's':
            newcoords -= 10
        elif direction == 'e':
            newcoords += 100
        elif direction == 'w':
            newcoords -= 100

        return newcoords


