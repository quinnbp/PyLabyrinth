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
        file = open(fpath, 'r')  # open, parse, and close data file
        self.roomDict = self.parse(file)
        file.close()

        # TODO: handle specials
        self.specials = []
        # TODO: implement direction handler (simple)

        # setup for object fields
        self.player = player
        self.navigator = Navigator()

        # setup for data fields
        self.gameSolved = False  # catches game end
        self.reenterstr = "You have been here before."

    def play(self):
        """
        Top level play function governing the game loop
        :return: None
        """
        while not self.gameSolved:
            coords = self.player.getPos()  # gets coords of player
            currentRoom = self.roomDict[coords]  # finds that room in the structure

            # print room to screen
            # TODO: functionalize this?
            if currentRoom.enter:
                print(self.reenterstr)
            else:
                currentRoom.entered()  # TODO: implement alt text better
            print()
            print(currentRoom.getText())
            print(currentRoom.declareExits())

            if coords in self.specials:  # handles special cases (puzzle rooms, etc)
                self.runSpecial(coords)
            else:  # standard case for navigation
                newLocation = self.navigator.takeInput(currentRoom)  # pass room object, get player input
                self.player.setPos(newLocation)  # assigns new coords to player

    @staticmethod
    def parse(file):
        """
        Generates the labyrinth dictionary from the given file

        :param file: File object representing labyrinth data structure
        :return: Dictionary<int, Room> representing the labyrinth
        """
        allrooms = {}
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
                    elif line[0] == 'm':
                        r.setMsg(line[2])
                    elif line[0] == 'co':
                        continue  # pass by comment lines within the file
                    else:
                        print("Invalid at line " + str(ln) + ".")

        print("[DEBUG] Processed " + str(ln) + " lines for " + str(len(allrooms.keys())) + " rooms.")
        print()
        return allrooms

    def runSpecial(self, coords):
        pass

