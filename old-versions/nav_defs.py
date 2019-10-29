def navigate(direction, char):
    """
    Function allowing the player to change rooms, checks for bad exits

    :param direction: String, player input for direction choice
    :param char: Character, see char_def
    :return: List of Ints, new current room coordinates
    """
    room = char.getPos()
    posdirect = room.getExits()
    coords = room.getCoords()
    x = coords[0]
    y = coords[1]
    z = coords[2]

    if direction == 'north':  # converts all inputs to single letter
        direct_a = 'n'
    elif direction == 'west':
        direct_a = 'w'
    elif direction == 'east':
        direct_a = 'e'
    elif direction == 'south':
        direct_a = 's'
    else:
        direct_a = direction
        
    if direct_a not in posdirect:  # check against available exits
        return "The room has no door in that direction."
    else:  # generates new coords based on direction on grid
        if direct_a == 'n':
            newcoords = [x, (y + 1), z]
        elif direct_a == 'e':
            newcoords = [(x+1), y, z]
        elif direct_a == 'w':
            newcoords = [(x-1), y, z]
        else:  # string2 == 's'
            newcoords = [x, (y-1), z]
            
        return newcoords
