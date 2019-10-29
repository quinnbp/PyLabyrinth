from room_def import Room

"""
File parsing functions for PyLabyrinth as used by floor functions

:authors: qbp
:version: 1.0
:date: 23-1-2019
"""

def parse(file):
    """
    Parses file into a list of Room objects, see room_def

    :param file: File to be parsed into rooms
    :return: List of Room objects
    """
    allrooms = []
    ln = 0; passcount = 0
    for line_raw in file:
        ln = ln + 1
        line = line_raw.split('/')
        line.pop()
        
        if not line:
            passcount += 1
        elif line[0] == 'r':
            r = roomParse(line[1:])
            allrooms.append(r)
        elif line[0] == 't':
            t = getRoom(line[1], allrooms)
            t.setText(line[2])
        elif line[0] == 'c':
            q = getRoom(line[1], allrooms)
            q.setContents(line[2:])
        elif line[0] == 'at':
            s = getRoom(line[1], allrooms)
            s.setAltStr(line[2])
        elif line[0] == 'm':
            p = getRoom(line[1], allrooms)
            p.setMsg(line[2])
        else:
            print("Invalid at line " + str(ln) + ".")
            
    return allrooms


def roomParse(line):
    """
    Generates a single room from one line of the file

    :param line: String line of file
    :return: Room object, see room_def
    """
    name = line[0]
    
    coordlist = []
    for n in line[1]:
        n = int(n)
        coordlist.append(n)

    exitlist = []
    for n in line[2]:
        exitlist.append(n)
 
    return Room(name, coordlist, exitlist)


def getRoom(coords, roomlist):
    """
    Gets a room by coordinates for modification

    :param coords: List of three ints, room coordinates
    :param roomlist:
    :return:
    """
    if isinstance(coords, str):
        coordinates = []
        for item in coords:
            coordinates.append(int(item))
    else:
        coordinates = coords
    
    for room in roomlist:
        if room.getCoords() == coordinates:
            return room
        
    return False
