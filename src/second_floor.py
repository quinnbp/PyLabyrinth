from file_parser import parse, getRoom
from io_defs import takeInput


def secondFloor(player, startroomstr):
    """
        Function taking character object through the second floor rooms

        :param player: Character object, see char_def
        :param startroomstr: List of 3 ints, starting coordinates
        :return: Character object, see char_def
    """
    file = open('floor_files/secondfloor.txt', 'r')  # parses file to generate rooms
    labrooms = parse(file)
    file.close()
    firstroom = getRoom(startroomstr, labrooms) 
    
    player.setPos(firstroom)  # puts player in first room
    
    end = False
    while not end:    # keeps offering inputs for nav
        current = player.getPos()  # current room
        
        if not current.enter:  # checks if room has been entered before
            current.entered()
            print('\n')
        else:
            if current.getCoords() != [1, 2, 1]:
                current.switchToAlt()
            print('\n')
            print("You have been in this room before.")
        
        if (current.getCoords() == [1, 2, 1]) and ('rope' in player.getInv()):  # end condition
            current.switchToAlt()
            current.addToExits('s')
            result = takeInput(current, player)
            if result == [1, 1, 1]:
                end = True  # escape from loop
                print("You rappel down the drop...")
                
            else:
                newroom = getRoom(result, labrooms)
                player.setPos(newroom)
        else: 
            result = takeInput(current, player)  # eventual loop to new position
            newroom = getRoom(result, labrooms)
            player.setPos(newroom)
            
    return player  # when floor is complete
