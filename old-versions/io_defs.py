from nav_defs import navigate
from intro_help_defs import directions

noteacts = ['note', 'write', 'writes'] 
markacts = ['mark', 'mark room', 'marks', 'marks room']
directionacts = ['n', 'north', 'e', 'east', 'w', 'west', 's', 'south']
takeacts = ['take', 'get', 'obtain']
dropacts = ['drop', 'leave']

fileact = 'start'


def takeInput(room, char, r=0):  # TODO: Migrate to class structure
    """
    Function to take and apply player input to navigation, room contents, and character.
    See room_def, notebook_def, char_def

    :param room: Room, current player position
    :param char: Character, player character
    :param r: Int modifier for rerolls on input
    :return: Recursive, Room
    """
    exitstring = room.declareExits()
           
    if r == 0:
        print(room.getText())  # print basic room text iff not a reroll
    
    if room.getMark() != '':  # if mark exists, print
        exitstring = exitstring + " The room is marked " + str(room.getMark()) + "."
        
    if (room.getMsg() != '') and (room.getMsg() not in char.note.msglist):
        char.note.addMsg(room.getMsg())  # if msg exists, add to player notebook
        
    if room.getContents() != [] and room.getContents() != ['plinth']:
        invstr = " This room contains: "
        
        if len(room.getContents()) > 1:
            for item in room.getContents():
                invstr = invstr + "a " + str(item) + ", "
            invstr = invstr[0:len(invstr)-2]
            invstr = invstr + "."
        else:
            invstr = invstr + "a " + str(room.contents[0]) + "."
            
        exitstring = exitstring + invstr
        
    print(exitstring)  # prints exits, mark, and contents
    
    act = ''
    while act == '':
        act = input('How do you proceed? ')
    
    act = act.lower()
    act = act.split()
    
    if act[0] == 'help':  # parser for help text
        directions()
        return takeInput(room, char, 1)
    
    elif act[0] == 'look':  # parser for room text
        return takeInput(room, char)
                
    elif act[0] == 'notebook':  # parser for notebook check
        char.printNotebook()
        return takeInput(room, char, 1)  # reroll
    
    elif act[0] == 'inventory':
        char.printInv()
        return takeInput(room, char, 1)  # reroll
    
    elif act[0] == 'messages':
        char.printMsgs()
        return takeInput(room, char, 1)  # reroll
    
    elif act[0] == 'messages':
        char.printMarks()
        return takeInput(room, char, 1)  # reroll
    
    elif act[0] == 'notes':
        char.printNotes()
        return takeInput(room, char, 1)  # reroll
      
    elif act[0] == 'go' and act[1] in directionacts:  # parser for input form 'go north'
        result = navigate(act[1], char)
        if isinstance(result, str):  # if navigate fails
            print(result)
            return takeInput(room, char, 1)  # reroll
        else:
            return result
    
    elif act[0] in noteacts:  # parser for taking notes
        takeNote(char)
        return takeInput(room, char, 1)  # reroll
    
    elif act[0] in directionacts:  # parser for navigation
        result = navigate(act[0], char)
        if isinstance(result, str):
            print(result)
            return takeInput(room, char, 1)  # reroll
        else:
            return result
        
    elif act[0] in markacts:  # parser for marking rooms
        markRoom(room, char)
        return takeInput(room, char, 1)  # reroll
    
    elif act[0] in takeacts:  # parser for picking up objects
        result = takeObject(act[1:], char, room)
        print(result)
        return takeInput(room, char, 1)  # reroll

    elif act[0] in dropacts:  # parser for dropping objects
        result = dropObject(act[1:], char, room)
        print(result)
        return takeInput(room, char, 1)  # reroll

    else:  # if all else fails
        print("You can't do that.")
        return takeInput(room, char, 1)  # reroll


def takeNote(char):
    """
    Function allowing player to note things in any room

    :param char: Character, see char_def
    :return: None
    """
    note = input('You decide to note down... ')
    nb = char.getNotebook()
    nb.addNote(note)

    
def takeObject(actionlist, char, room):
    """
    Function allowing player to pick up objects

    :param actionlist: List of Strings, remainder of input string
    :param char: Character, see char_def
    :param room: Room, current room, see room_def
    :return: String, result of action
    """
    cont = room.getContents()
    
    string = actionlist[0]
    for item in actionlist[1:]:
        string = string + ' ' + str(item)
    
    if cont == [] or cont == ['plinth']:  # checks for available objects (excludes plinth)
        return "There is nothing to take in this room"
    
    item = 0
    newcont = []
    for n in range(len(cont)):  # regenerates room contents and sets to room
        if cont[n] != string:   # will be identical unless item is valid
            newcont.append(cont[n])
        elif cont[n] == string:
            item = string
    room.setContents(newcont)
    
    if item != 0:  # if item is valid, adds to inv
        char.setInv(char.inv + [string])
        char.note.invlist = char.inv
        return "You pick up the " + string + "."
    else:
        return "There is no " + string + " in this room."
    
    
def dropObject(actionlist, char, room):
    """
    Function allowing player to drop objects

    :param actionlist: List of Strings, remainder of input string
    :param char: Character, see char_def
    :param room: Room, current room, see room_def
    :return: String, result of action
    """
    res = 0
    newinvlist = []
    for item in char.inv:
        if item != actionlist:
            newinvlist.append(item)
        else:
            res = 1

    char.setInv(newinvlist)
    char.note.invlist = char.inv
    
    if res != 0:
        contlist = room.getContents()
        newcontlist = contlist + [actionlist]
        room.setContents(newcontlist)
        return "You drop the " + actionlist + "."
    else:
        return "You have no " + actionlist + "."


def markRoom(room, char):
    """
    Function allowing a player to mark a room

    :param room: Room, current room, see room_def
    :param char: Character, see char_def
    :return: Recursive, None
    """
    mark = input("What mark would you like to leave in this room? ")
    
    if mark in char.note.marklist:  # prevent confusing duplicates
        print("You have already used that mark.")
        return markRoom(room, char)
    
    if room.getMark() != '':
        currmark = room.getMark()
        newmarknote = []
        for item in char.note.marklist:
            if item != currmark:
                newmarknote.append(item)
        char.note.marklist = newmarknote
                   
    room.setMark(char, mark)
