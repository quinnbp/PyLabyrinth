class Room:
    """
    Room class for PyLabyrinth.

    :Date: 23-1-2019
    :Authors: qbp
    :Version: 1.1
    """
    def __init__(self, name, room_coords, room_exits, contents=[], room_str='', alternate_str='', mark='', message='',
                 special_str=''):
        """
        Initializes a new room.

        :param name: String, identification for points of interest
        :param room_coords: List of ints, coordinates for the room within the maze
        :param room_exits: List of chars, directional exits from the room
        :param contents: List of strings, items contained within room
        :param room_str: String, text to display on first entry
        :param alternate_str: String, text to display on subsequent entries
        :param mark: String, mark left by player in room, default ''
        :param message: String, message left for player, default ''
        :param special_str: String, special additional text switch for interactable rooms, default ''
        """
        self.name = str(name)
        self.contents = contents
        self.mark = str(mark)
        self.exits = room_exits
        self.msg = message

        self.text = str(room_str)
        self.alt = str(alternate_str)
        self.special = str(special_str)
        
        self.xyz = room_coords  # list

        self.enter = False
        
    def __str__(self):
        return "Room(" + str(self.name) + " : " + str(self.xyz) + " : " + str(self.exits) + " : " + str(self.contents) + ")"
    
    def getName(self):  # accessor functions
        return self.name
    
    def getCoords(self):
        return self.xyz
    
    def getFloor(self):
        return self.xyz[2]
    
    def getExits(self):
        return self.exits
    
    def getMark(self):
        return self.mark

    def getContents(self):
        return self.contents
    
    def getText(self):
        return self.text
    
    def getMsg(self):
        return self.msg

    def setContents(self, newinvlist):  # mutator functions
        self.contents = newinvlist

    def setText(self, string):
        strlist = string.split('BRK')
        newstring = strlist[0]
        for item in strlist[1:]:
            newstring = newstring + '\n' + str(item) 
        self.text = newstring

    def setMark(self, char, string):
        self.mark = string
        char.note.addMark(string)
        
    def setAltStr(self, string):
        strlist = string.split('BRK')
        newstring = strlist[0]
        for item in strlist[1:]:
            newstring = newstring + '\n' + str(item) 
        self.alt = newstring
        
    def setMsg(self, string):
        strlist = string.split('BRK')
        newstring = strlist[0]
        for item in strlist[1:]:
            newstring = newstring + '\n' + str(item) 
        self.msg = newstring
        
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
    
    def switchToAlt(self):  # switch from initial room text to secondary
        self.text = self.alt
        
    def addToExits(self, string):  # add a new exit to the list
        self.exits.append(string)
