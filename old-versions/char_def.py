class Character:
    """
    Character class for PyLabyrinth.

    :authors: qbp
    :version: 1.0
    :date: 23-1-2019
    """
    def __init__(self, name, inventory, room, notebook):
        """
        Initializes new character instance

        :param name: User-given character name
        :param inventory: String list of objects currently held
        :param room: Current position in the maze
        :param notebook: Player's associated Notebook object (see notebook_def)
        """
        self.name = name
        self.inv = inventory
        self.pos = room
        self.note = notebook
            
    def __str__(self):
        """
        Basic string method for diagnostics
        :return: String, character name and position
        """
        return 'Character(' + str(self.name) + " : " + str(self.pos.xyz) + ")"
    
    def getName(self):
        """
        Gets character's name
        :return: String, name
        """
        return self.name
    
    def getInv(self):
        """
        Gets character's inventory
        :return: List of strings, inventory
        """
        return self.inv
    
    def getRoom(self):
        """
        Gets characters current room position
        :return: Room object, see room_def
        """
        return self.pos
    
    def getPos(self):
        """
        Duplicate of getRoom
        :return: Room object, see room_def
        """
        return self.pos
    
    def getNotebook(self):
        """
        Gets character's current notebook state
        :return: Notebook object, see notebook_def
        """
        return self.note
    
    def getState(self):
        """
        Gets current character state
        :return: List of String name, List inventory, Room r
        """
        return self.state
    
    def setName(self, string):
        """
        Mutator for character name
        :param string: String, new name
        :return: None
        """
        self.name = string
        
    def setInv(self, newinvlist):
        """
        Total mutator for character inventory
        :param newinvlist: List, new inventory
        :return: None
        """
        self.inv = newinvlist
        
    def setRoom(self, room):
        """
        Mutator for character position
        :param room: Room, new position
        :return: None
        """
        self.pos = room
    
    def setPos(self, room):
        """
        Duplicate of setRoom
        :param room: Room, new position
        :return: None
        """
        self.pos = room
        
    def addToInv(self, item):
        """
        Adds an item to the player inventory and notebook
        :param item: String showing item to add
        :return: None
        """
        self.inv.append(str(item))
        self.note.addToInv(item)
        
    def printNotebook(self):
        """
        Prints formatted notebook to sys out, see notebook_def
        :return: None
        """
        print('\n')
        print(self.note.getInv())
        print(self.note.getMsgs())
        print(self.note.getMarks())
        print(self.note.getNotes())
        print('\n')
        
    def printInv(self):
        """
        Prints formatted inventory to sys out, see notebook_def
        :return: None
        """
        print('\n')
        print(self.note.getInv())
        print('\n')
        
    def printMsgs(self):
        """
        Prints formatted message string to sys out, see notebook_def
        :return: None
        """
        print('\n')
        print(self.note.getMsgs())
        print('\n')

    def printMarks(self):
        """
        Prints formatted mark string to sys out, see notebook_def
        :return: None
        """
        print('\n')
        print(self.note.getMarks())
        print('\n')

    def printNotes(self):
        """
        Prints formatted notes to sys out, see notebook_def
        :return: None
        """
        print('\n')
        print(self.note.getNotes())
        print('\n')



