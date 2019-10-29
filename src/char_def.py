class Character:
    """
    Character class for PyLabyrinth.

    :authors: qbp
    :version: 1.0
    :date: 23-1-2019
    """
    def __init__(self, name, inventory, currentcoords):
        """
        Initializes new character instance

        :param name: String, user given character name
        :param inventory: String list of objects currently held
        :param currentcoords: Room object representing position in maze
        """
        self.name = name
        self.inv = inventory
        self.pos = currentcoords

        self.threadHistory = []
            
    def __str__(self):
        """
        Basic string method for diagnostics
        :return: String, character name and position
        """
        return 'Character(' + str(self.name) + " : " + str(self.pos.xyz) + ")"
    
    def getThreadHistory(self):
        """
        Returns entire thread history
        :return: List<int> of thread history
        """
        return self.threadHistory

    def getLastThread(self):
        """
        Pops from the thread history and returns it
        :return: Int representation of the coordinates of most recent room in thread history
        """
        return self.threadHistory.pop()

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
    
    def getPos(self):
        """
        Duplicate of getRoom
        :return: Int representation of location coords
        """
        return self.pos
    
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

    def dropFromInv(self, item):
        """
        Drops an item from the player's inventory
        :param item: String of item to drop
        :return: None
        """
        self.inv.remove(item)



