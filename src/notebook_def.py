class Notebook:
    """ Notebook class for Labyrinth. Arguments - inv_list, msg_list, mark_list, plyr_notes """
    def __init__(self, inv_list, msg_list, mark_list, plyr_notes):
        self.invlist = inv_list ## list of items
        self.msglist = msg_list ## list of messages
        self.marklist = mark_list ## list of marks left
        self.notes = plyr_notes ## list of notes
        
        self.setInv()  ## these create 'pretty' versions of the above
        self.setMsgs() ## stored under invpage, msgpage, markpage, notepage
        self.setMarks()
        self.setNotes()
        
        self.state = [self.invlist, self.marklist, self.msglist, self.notes] ## for save function
        
    def __str__(self):
        return '\n' + self.invpage + self.msgpage + self.markpage + self.notepage + '\n'
    
    def applychanges(self):
        self.setInv() 
        self.setMsgs() 
        self.setMarks()
        self.setNotes()
        
    def setInv(self): ## sort of replacer functions; generate 'pretty' versions
        if self.invlist == []:
            self.invpage = "Your bag is empty."
        else:
            string = "Your bag contains:"
            for item in self.invlist:
                string = string + '\n - ' + item
            self.invpage = string

    def setMsgs(self):
        if self.msglist == []:
            self.msgpage = "You haven't seen any messages."
        else:
            string2 = "You have seen these writings:"
            for item2 in self.msglist:
                string2 = string2 + '\n - ' + item2
            self.msgpage = string2

    def setMarks(self):
        if self.marklist == []:
            self.markpage = "You haven't left any marks."
        else:
            string3 = "You have left these marks:"
            for item3 in self.marklist:
                string3 = string3 + '\n - ' + item3
            self.markpage = string3
            
    def setNotes(self):
        if self.notes == []:
            self.notepage = "You haven't made any notes."
        else:
            string4 = "You have made these notes:"
            for item4 in self.notes:
                string4 = string4 + '\n - ' + item4
            self.notepage = string4
            
    def getInv(self): ## accessor functions
        self.setInv()
        return self.invpage
    
    def getMsgs(self):
        self.setMsgs()
        return self.msgpage
    
    def getMarks(self):
        self.setMarks()
        return self.markpage
    
    def getNotes(self):
        self.setNotes()
        return self.notepage
    
    def addToInv(self, item): ## adder functions (also call the replacer functions)
        self.invlist.append(str(item))
        self.setInv()
        
    def addMsg(self, item):
        self.msglist.append(str(item))
        self.setMsgs()
        
    def addMark(self, item):
        self.marklist.append(str(item))
        self.setMarks()
        
    def addNote(self, item):
        self.notes.append(str(item))
        self.setNotes()
    
    