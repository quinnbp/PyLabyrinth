def navigate(string, char):
    room = char.getPos()
    posdirect = room.getExits()
    coords = room.getCoords()
    x = coords[0]
    y = coords[1]
    z = coords[2]

    if string == 'north': ## converts all inputs to single letter
        string2 = 'n'
    elif string == 'west':
        string2 = 'w'
    elif string == 'east':
        string2 = 'e'
    elif string == 'south':
        string2 = 's'
    else:
        string2 = string
        
    if string2 not in posdirect: ## check against available exits
        return "The room has no door in that direction."
    else: ## generates new coords based on direction on grid
        if string2 == 'n':
            newcoords = [x, (y + 1), z]
        elif string2 == 'e':
            newcoords = [(x+1), y, z]
        elif string2 == 'w':
            newcoords = [(x-1), y, z]
        elif string2 == 's':
            newcoords = [x, (y-1), z]
            
        return newcoords
            
        