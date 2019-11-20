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

        self.visited = False
        
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

    def getAltText(self):
        # returns alt if nonempty, otherwise text (so we only have to set for rooms where it matters)
        if self.alt == "":
            return self.text
        else:
            return self.alt

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

    def switchText(self):  # swap to alternate text after first visit
        temp = self.text
        self.text = self.alt
        self.alt = temp
        
    def entered(self):
        self.visited = True
        
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
                
        exitstring += '.'
        
        if len(self.exits) > 1:
            return "There are exits to the" + exitstring
        else:
            return "There is an exit to the" + exitstring

    def declareContents(self):
        if len(self.contents) == 0:  # check if room empty
            return ""

        contentstring = "This room contains: "
        for item in self.contents[:-1]:  # list items in room
            contentstring += item + ", "
        contentstring += self.contents[len(self.contents) - 1] + "."
        return contentstring

    def addToContents(self, item):
        self.contents.append(item)

    def removeItem(self, objectStr):
        self.contents.remove(objectStr)
        
    def addToExits(self, string):  # add a new exit to the list
        self.exits.append(string)

    def printRoom(self, enableReenter=True):
        print()  # newline
        if self.visited:
            if enableReenter:
                print(self.reenterstr)  # tell player revisit
            print(self.getAltText())  # print alternate text if visited
        else:
            self.entered()  # otherwise set visited
            print(self.text)  # print first text

        print(self.declareExits())  # print contents and exits to console
        print(self.declareContents())
