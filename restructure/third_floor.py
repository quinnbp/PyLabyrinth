from file_parser import parse, getRoom
from io_defs import takeInput


def thirdFloor(player, startroomstr):
    """
        Function taking character object through the third floor rooms and puzzle

        :param player: Character object, see char_def
        :param startroomstr: List of 3 ints, starting coordinates
        :return: Character object, see char_def
    """
    file = open('floor_files/thirdfloor.txt', 'r')  # parses file to generate rooms
    labrooms = parse(file)
    file.close()
    firstroom = getRoom(startroomstr, labrooms) 
    
    player.setPos(firstroom)  # puts player in first room
    
    end = False
    while not end:    # keeps offering inputs for nav
        current = player.getPos()  # current room
        
        if not current.enter:  # checks against past rooms
            current.entered()
            print('\n')
            
        else:
            if current.getCoords() != [2, 1, 2] and current.getCoords() != [2, 3, 2] and current.getCoords() != [3, 2, 2] and current.getCoords() != [1, 2, 2]:
                current.switchToAlt()
            print('\n')
            print("You have been in this room before.")
            
        if (current.getCoords() == [2, 3, 2]) and ('statue of hercules' in player.getInv()):
            current.switchToAlt()
        elif (current.getCoords() == [3, 2, 2]) and ('statue of odesseyus' in player.getInv()):
            current.switchToAlt()
        elif (current.getCoords() == [1, 2, 2]) and ('statue of perseus' in player.getInv()):
            current.switchToAlt()
        
        if (current.getCoords() == [2, 1, 2]) and (contains(player.getInv(), 'and', 'statue of hercules', 'statue of perseus', 'statue of odesseyus') == True):  # end condition
            current.switchToAlt()
            print(current.getText())
            
            userin = input("Do you try the puzzle?")
            
            if userin == 'y' or userin == 'yes':
                print("You try the puzzle...")
                puzres = heroPuzzle()
            
                if puzres == True:
                    current.addToExits('n')
                
                    player.inv = remove('Statue of Hercules', player.getInv())
                    player.inv = remove('Statue of Perseus', player.getInv())
                    player.inv = remove('Statue of Odesseyus', player.getInv())
                
                    print("The north wall rumbles open to reveal a doorway to the north.")
                
                    result = takeInput(current, player, 1)
                    newroom = getRoom(result, labrooms)
                    player.setPos(newroom)
                
                else:
                    print("Nothing happens. Perhaps that is not the answer.")
                    player.setPos(current)
                    
            else:
                print("You decide to come back later.")
                
                result = takeInput(current, player)  # eventual loop to new position
                newroom = getRoom(result, labrooms)
                player.setPos(newroom)
                
        elif current.getCoords() == [2, 2, 2]:
            result = takeInput(current, player, 1 )
            if result == [2, 3, 2]:
                end = True
                print("You descend to the floor below...")
                print("Congratulations! You have completed the demo of floors 1-3.")
            else:
                newroom = getRoom(result, labrooms)
                player.setPos(newroom)
            
        else: 
            result = takeInput(current, player)  # eventual loop to new position
            newroom = getRoom(result, labrooms)
            player.setPos(newroom)
            
    return player  # when floor is complete


def contains(alist, mod, *strings):
    """
    Function to check if an item appears in a list, mod for and/or

    :param alist: List to check
    :param mod: String, and/or
    :param strings: Strings to check
    :return: Boolean
    """
    if mod == 'and':
        for string in strings:
            if string not in alist:
                return False
        return True
    
    if mod == 'or':
        for string in strings:
            if string in alist:
                return True
        return False

 
def heroPuzzle():
    """
    Function allowing player to interact with and solve matching puzzle

    :return: Boolean
    """
    actual = {'Nemean Lion':'statue of hercules', 'Medusa':'statue of perseus', 'Cyclops':'statue of odesseyus'}
    actual2 = {'Nemean Lion':'hercules', 'Medusa':'perseus', 'Cyclops':'odesseyus'}
    playerdict = {'Nemean Lion':'init', 'Medusa':'init2', 'Cyclops':'init3'}
    
    for item in playerdict.keys():
        pair = input("Which statue do you pair with " + str(item) + "?")
        pair.lower()
        playerdict[item] = pair
    
    if playerdict == actual or playerdict == actual2:
        return True
    else:
        return False
    

def remove(item, alist):
    """
    Function to remove an item from a list

    :param item: Item to remove
    :param alist: List to remove from
    :return: List, modified list
    """
    newlist = []
    for thing in alist:
        if thing != item:
            newlist.append(thing)
    return newlist
