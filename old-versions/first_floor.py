from file_parser import parse, getRoom
from io_defs import takeInput


def firstFloor(player, startroomstr):
    """
    Function taking character object through the first floor rooms

    :param player: Character object, see char_def
    :param startroomstr: List of 3 ints, starting coordinates
    :return: Character object, see char_def
    """
    file = open('floor_files/firstfloor.txt', 'r')  # parses file to generate rooms
    labrooms = parse(file)
    file.close()
    firstroom = getRoom(startroomstr, labrooms)  # sets initial room
    
    player.setPos(firstroom)  # sets player in initial room
    
    end = False
    while not end:  # Loops to keep offering inputs to new rooms
        current = player.getPos()  # current room
        
        if not current.enter:   # check if the room has been entered before
            current.entered()
            print('\n')
        else:
            if current.getCoords() != [2, 1, 0]:
                current.switchToAlt()
            print('\n')
            print("You have been in this room before.")
        
        if (current.getCoords() == [2, 1, 0]) and ('lantern' in player.getInv()):  # End condition
            current.switchToAlt()
            current.addToExits('e')
            result = takeInput(current, player)
            if result == [3, 1, 0]:
                end = True  # escapes the loop
            else:
                newroom = getRoom(result, labrooms)
                player.setPos(newroom)
        else: 
            result = takeInput(current, player)  # Loop eventually navigates to new room
            newroom = getRoom(result, labrooms) 
            player.setPos(newroom)
            
    return player  # when floor is completed

