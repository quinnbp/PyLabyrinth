class Character:
    """ Character class for Labyrinth. Arguments - inventory, room, notebook, room history """
    def __init__(self, name, inventory, room, notebook):
        self.name = name ## perm var from player
        self.inv = inventory ## current items
        self.pos = room ## current room
        self.note = notebook ## storage for notebook object
        
        self.state = [self.name, self.inv, self.pos] ## for save function
        
    def __str__(self):
        return 'Character(' + str(self.name) + " : " + str(self.pos.xyz) + ")"
    
    def getName(self):
        return self.name
    
    def getInv(self):
        return self.inv
    
    def getRoom(self):
        return self.pos
    
    def getPos(self):
        return self.pos
    
    def getNotebook(self):
        return self.note
    
    def getState(self):
        return self.state
    
    def setName(self, string):
        self.name = string
        
    def setInv(self, newinvlist):
        self.inv = newinvlist
        
    def setRoom(self, room):
        self.pos = room
    
    def setPos(self, room):
        self.pos = room
        
    def addToInv(self, item):
        self.inv.append(str(item))
        self.note.addToInv(item)
        
    def printNotebook(self):
        print('\n')
        print(self.note.getInv())
        print(self.note.getMsgs())
        print(self.note.getMarks())
        print(self.note.getNotes())
        print('\n')
        
    def printInv(self):
        print('\n')
        print(self.note.getInv())
        print('\n')
        
    def printMsgs(self):
        print('\n')
        print(self.note.getMsgs())
        print('\n')
        
    def printMarks(self):
        print('\n')
        print(self.note.getMarks())
        print('\n')
        
    def printNotes(self):
        print('\n')
        print(self.note.getNotes())
        print('\n')
    
    
        
        