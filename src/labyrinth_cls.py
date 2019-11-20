from room_def import Room
from navigator_cls import Navigator


class Labyrinth:
    """
    Central graph-structure class for building the labyrinth. Contains room dictionary and central organization for
    game state. Also contains file parsing logic.

    :Date: 10-16-2019
    :Authors: qbp
    :Version: 1.2
    """

    def __init__(self, fpath, player):
        """
        Generates the labyrinth data structure from a file and instantiates the dictionary
        :param fpath: Filepath to data defining construction of labyrinth
        """
        self.roomDict = {}
        file = open(fpath, 'r')  # open, parse, and close data file
        self.parse(file)
        file.close()

        self.specials = [210]

        # setup for object fields
        self.player = player
        self.navigator = Navigator()

        # setup for data fields
        self.gameSolved = False  # catches game end

    def play(self):
        """
        Top level play function governing the game loop
        :return: None
        """
        while not self.gameSolved:
            coords = self.player.getPos()  # gets coords of player
            currentRoom = self.roomDict[coords]  # finds that room in the structure

            if coords in self.specials:  # handles special cases (puzzle rooms, etc)
                newLocation = self.runSpecial(currentRoom)
            else:  # standard case for navigation
                currentRoom.printRoom()  # print room to console
                # takes player input, resolves character actions (take, use), and returns a new location
                newLocation = self.navigator.takeInput(currentRoom, self.player)
            self.player.setPos(newLocation)  # assigns new coords to player

    def parse(self, file):
        """
        Generates the labyrinth dictionary from the given file
        :param file: File object representing labyrinth data structure
        :return: Dictionary<int, Room> representing the labyrinth
        """
        allrooms = dict()
        ln = 0
        for line_raw in file:
            ln += 1
            line = line_raw.split('/')
            line.pop()  # removes newling char from list

            if line:  # catches line breaks in file
                if line[0] == 'r':  # in this case line generates a new room
                    coordlist = []  # set coords in list
                    for n in line[1]:
                        n = int(n)
                        coordlist.append(n)

                    exitlist = []  # assign exits to given room
                    for n in line[2]:
                        exitlist.append(n)

                    r = Room(coordlist, exitlist)
                    allrooms[r.xyz] = r  # r.xyz is int repr of coords, r is room

                else:  # otherwise it modifies properties of existing room
                    r = allrooms[int(line[1])]  # get int rep of coords for matching
                    if line[0] == 't':
                        r.setText(line[2])
                    elif line[0] == 'c':
                        r.setContents(line[2:])
                    elif line[0] == 'at':
                        r.setAltStr(line[2])
                    elif line[0] == 'co':
                        continue  # pass by comment lines within the file
                    else:
                        print("Invalid at line " + str(ln) + ".")

        print("[DEBUG] Processed " + str(ln) + " lines for " + str(len(allrooms.keys())) + " rooms.")
        self.roomDict = allrooms

    def runSpecial(self, room):
        """
        Generates the labyrinth dictionary from the given file
        :param room: Room object representation of special state
        :return: Returns recurse to takeInput() -- new room coords
        """
        if room.getXyz() == 210:  # first floor end room TODO: break into handlers
            if 'lantern' in self.player.getInv():
                print("There is a staircase descending from this room. With the lantern in hand, you could take it.")
                response = input("Do you? (y/n) ")
                if response[0] == 'y':
                    print("\nDemo Completed! Thanks for playing PyLabyrinth!")
                    self.gameSolved = True
                    return 111  # entry condition for floor 2 (not yet implemented)
                else:
                    print("You decide against it.")
                    return self.navigator.takeInput(room, self.player)
            else:
                room.printRoom()
                return self.navigator.takeInput(room, self.player)
