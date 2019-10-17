from room_def import Room


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
        file = open('demo.txt', 'r')  # open, parse, and close data file
        self.roomDict = self.parse(file)
        file.close()

        # TODO: handle specials
        # TODO: implement direction handler (simple)

        self.player = player

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

        print("Processed " + str(ln) + " lines for " + str(len(allrooms.keys())) + " rooms.")
        return allrooms
