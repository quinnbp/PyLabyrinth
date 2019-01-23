def intro():
    file = open('resources/introfile.txt', 'r')
    printstr = ''
    for line in file:
        printstr = printstr + str(line)
    file.close()
    
    print(printstr)
        
    file2 = open('resources/directionsfile.txt', 'r')
    printstr2 = ''
    for line in file2:
        printstr2 = printstr2 + str(line)
    file2.close()
    
    print(printstr2)
    
    namein = str(input('Give your character a name? '))  # takes name or defaults to 'Theseus'
    
    if namein == '':
        charname = 'Theseus'
    else:
        charname = namein
        
    print("Welcome to the labyrinth, " + charname + ". \n")
    
    return charname

def directions():
    file2 = open('resources/directionsfile.txt', 'r')
    printstr2 = ''
    for line in file2:
        printstr2 = printstr2 + str(line)
    file2.close()
    
    print('\n' + printstr2 + '\n')
    