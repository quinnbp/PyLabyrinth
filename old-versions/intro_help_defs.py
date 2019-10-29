def intro():
    """
    Function to parse and display introduction text file and get player name

    :return: String, name
    """
    file = open('resources/intro.txt', 'r')
    printstr = ''
    for line in file:
        printstr = printstr + str(line)
    file.close()
    
    print(printstr)
        
    file2 = open('resources/directions.txt', 'r')
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
    """
    Function to parse and display help text file

    :return: None
    """
    file2 = open('resources/directions.txt', 'r')
    printstr2 = ''
    for line in file2:
        printstr2 = printstr2 + str(line)
    file2.close()
    
    print('\n' + printstr2 + '\n')
