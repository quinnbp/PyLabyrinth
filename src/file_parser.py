from room_def import *

## file = open('indata.txt', 'r') ## Global vars

def parse(file): ## Takes data file
    allrooms = []
    ln = 0; rg = 0
    for eachline in file:
        ln = ln + 1
        line = eachline.split('/')
        line.pop()
        
        if line == [] and rg == 0: ## Tests of file parsing
            ## print('Rooms generated.')
            rg = 1
        elif line == [] and rg == 1:
            ## print('Text generated.')
            rg = 2
        elif line == [] and rg == 2:
            ## print('Contents generated.')
            rg = 3
        elif line == [] and rg == 3:
            ## print('Alternates generated.')
            rg = 4
        elif line == [] and rg == 4:
            ## print('Messages generated.')
            rg = 5
                        
        elif line[0] == 'r':
            r = roomParse(line[1:])
            allrooms.append(r)
        elif line[0] == 't':
            t = getRoom(line[1], allrooms)
            t.setText(line[2])
        elif line[0] == 'c':
            q = getRoom(line[1], allrooms)
            q.setContents(line[2:])
        elif line[0] == 'at':
            s = getRoom(line[1], allrooms)
            s.setAltStr(line[2])
        elif line[0] == 'm':
            p = getRoom(line[1], allrooms)
            p.setMsg(line[2])
        else:
            print("Invalid at line " + str(ln) + ".")
            
#     for room in allrooms: ## show rooms on startup
#         print(str(room))
            
    return allrooms

def roomParse(line): ## Takes line and generates room
    name = line[0]
    
    coordlist = []
    for n in line[1]:
        n = int(n)
        coordlist.append(n)

    exitlist = []
    for n in line[2]:
        exitlist.append(n)
 
    return Room(name, coordlist, exitlist)

def getRoom(coords, roomlist): ## Takes coords (list or str) and roomlist and finds room with property coords
    if isinstance(coords, str):
        coordinates = []
        for item in coords:
            coordinates.append(int(item))
    else:
        coordinates = coords
    
    for room in roomlist:
        if room.getCoords() == coordinates:
            return room
        
    return False
        
