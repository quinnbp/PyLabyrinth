class Room:
    """
    Room class for PyLabyrinth.

    :Date: 23-1-2019
    :Authors: qbp
    :Version: 1.1
    """
    def __init__(self, room_coords, room_exits, contents=[], room_str='NO TEXT', alternate_str=''):
        """
        Generates new room object

        :param room_coords: List of ints, coordinates for the room within the maze
        :param room_exits: List of chars, directional exits from the room
        :param contents: List of strings, items contained within room
        :param room_str: String, text to display on first entry
        :param alternate_str: String, text to display on subsequent entries
        """

        self.reenterstr = "You have been here before."

        self.contents = contents
        self.exits = room_exits

        self.text = str(room_str)  # for first visit
        self.alt = str(alternate_str)  # after first visit, switch to alt
        
        self.coords = room_coords  # list representation
        self.xyz = self.coords[0] * 100 + self.coords[1] * 10 + self.coords[2]  # int representation

        self.enter = False
        
    def __str__(self):
        return "Room(" + str(self.xyz) + " : " + str(self.exits) + " : " + str(self.contents) + ")"

    def getCoords(self):
        return self.coords

    def getXyz(self):
        return self.xyz
    
    def getFloor(self):
        return self.coords[2]
    
    def getExits(self):
        return self.exits

    def getContents(self):
        return self.contents
    
    def getText(self):
        return self.text

    def setContents(self, newinvlist):  # mutator functions
        self.contents = newinvlist

    def setText(self, string):
        strlist = string.split('&')
        newstring = strlist[0]
        for item in strlist[1:]:
            newstring = newstring + '\n' + str(item) 
        self.text = newstring
        
    def setAltStr(self, string):
        strlist = string.split('&')
        newstring = strlist[0]
        for item in strlist[1:]:
            newstring = newstring + '\n' + str(item) 
        self.alt = newstring
        
    def entered(self):
        self.enter = True
        
    def declareExits(self):  # returns 'pretty' exit string to show player
        exitstring = ''
        for n in range(len(self.exits)):  # converts exit list to words
            if self.exits[n] == 'n':
                exitstring = exitstring + ' North'
            elif self.exits[n] == 'w':
                exitstring = exitstring + ' West'
            elif self.exits[n] == 'e':
                exitstring = exitstring + ' East'
            elif self.exits[n] == 's':
                exitstring = exitstring + ' South'
            
            if n < (len(self.exits) - 2):  # grammar parser
                exitstring = exitstring + ','
            elif n == (len(self.exits) - 2):
                exitstring = exitstring + ' and'
                
        exitstring = exitstring + '.'
        
        if len(self.exits) > 1:
            return "There are exits to the" + exitstring
        else:
            return "There is an exit to the" + exitstring

    def addToContents(self, item):  # for some reason, this doesn't work
        self.contents.append(str(item))

    def removeItem(self, objectStr):
        self.contents.remove(objectStr)
        
    def addToExits(self, string):  # add a new exit to the list
        self.exits.append(string)

    def printRoom(self):
        if self.enter:
            print(self.reenterstr)
        else:
            self.entered()  # TODO: implement alt text better
        print()
        print(self.getText())
        print(self.declareExits())
        print(self.contents)  # TODO: implement fancy
