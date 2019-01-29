class Notebook:
    """
    Notebook class for PyLabyrinth
    
    :authors: qbp
    :version: 1.0
    :date: 23-1-2019
    """
    def __init__(self, inv_list, msg_list, mark_list, plyr_notes):
        """
        Initializes new notebook object with given parameter lists

        :param inv_list: List of Strings, current player inventory
        :param msg_list: List of Strings, current player messages
        :param mark_list: List of Strings, current player marks
        :param plyr_notes: List of Strings, current player notes
        """
        self.invlist = inv_list  # list of items
        self.msglist = msg_list  # list of messages
        self.marklist = mark_list  # list of marks left
        self.notes = plyr_notes  # list of notes
        
        self.setInv()   # these create 'pretty' versions of the above
        self.setMsgs()  # stored under invpage, msgpage, markpage, notepage
        self.setMarks()
        self.setNotes()
        
        self.state = [self.invlist, self.marklist, self.msglist, self.notes]  # for save function

    def __str__(self):
        """
        Creates string representation of notebook for diagnostics

        :return: String
        """
        return '\n' + self.invpage + self.msgpage + self.markpage + self.notepage + '\n'
    
    def applychanges(self):
        """
        Updates player-facing version of notebook based on data structure changes

        :return: None
        """
        self.setInv() 
        self.setMsgs() 
        self.setMarks()
        self.setNotes()
        
    def setInv(self):
        """
        Generates a player-facing version of the Inventory to display

        :return: None
        """
        if self.invlist == []:
            self.invpage = "Your bag is empty."
        else:
            string = "Your bag contains:"
            for item in self.invlist:
                string = string + '\n - ' + item
            self.invpage = string

    def setMsgs(self):
        """
        Generates a player-facing version of the Messages to display

        :return: None
        """
        if self.msglist == []:
            self.msgpage = "You haven't seen any messages."
        else:
            string2 = "You have seen these writings:"
            for item2 in self.msglist:
                string2 = string2 + '\n - ' + item2
            self.msgpage = string2

    def setMarks(self):
        """
        Generates a player-facing version of the Marks to display

        :return: None
        """
        if self.marklist == []:
            self.markpage = "You haven't left any marks."
        else:
            string3 = "You have left these marks:"
            for item3 in self.marklist:
                string3 = string3 + '\n - ' + item3
            self.markpage = string3
            
    def setNotes(self):
        """
        Generates a player-facing version of the Notes to display

        :return: None
        """
        if self.notes == []:
            self.notepage = "You haven't made any notes."
        else:
            string4 = "You have made these notes:"
            for item4 in self.notes:
                string4 = string4 + '\n - ' + item4
            self.notepage = string4
            
    def getInv(self):  # accessor functions
        """
        Gets a back-end representation of the player inventory list

        :return: String, inventory
        """
        self.setInv()
        return self.invpage
    
    def getMsgs(self):
        """
        Gets a back-end representation of the player messages list

        :return: String, inventory
        """
        self.setMsgs()
        return self.msgpage
    
    def getMarks(self):
        """
        Gets a back-end representation of the player marks list

        :return: String, inventory
        """
        self.setMarks()
        return self.markpage
    
    def getNotes(self):
        """
        Gets a back-end representation of the player notes list

        :return: String, inventory
        """
        self.setNotes()
        return self.notepage
    
    def addToInv(self, item):  # mutator functions
        """
        Adds an item to the notebook list of player inventory

        :param item: String, item to add
        :return: None
        """
        self.invlist.append(str(item))
        self.setInv()
        
    def addMsg(self, item):
        """
        Adds an item to the notebook list of player messages

        :param item: String, item to add
        :return: None
        """
        self.msglist.append(str(item))
        self.setMsgs()
        
    def addMark(self, item):
        """
        Adds an item to the notebook list of player marks

        :param item: String, item to add
        :return: None
        """
        self.marklist.append(str(item))
        self.setMarks()
        
    def addNote(self, item):
        """
        Adds an item to the notebook list of player notes

        :param item: String, item to add
        :return: None
        """
        self.notes.append(str(item))
        self.setNotes()
