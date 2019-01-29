# PyLabyrinth
PyLabyrinth is a prototype python rework of my earlier text-adventure project, Labyrinth. 

## Project Goals

This project has three overall goals:
   - Practice and improve with the Python programming language
   - Explore the mechanics of user interaction in a text-adventure structure
   - Develop an interesting and engaging text-adventure game
   
## Execution

`python3 main.py`

The most recent stable release will be give under src/. All other folders contain in-progress or unstable versions. 

## File Structure

### char_def.py

Contains the class definition for the player character object, including accessors and mutators.

### file_parser.py

Contains function definitions allowing the floor functions to parse their structure files into a list of Room objects.

### first_floor.py, second_floor.py, third_floor.py, etc

Contains a function definition for each floor (level) of the labyrinth. These functions contain similar main loops with
different checks for special conditions on rooms, as well as separate internal functions for puzzles or items. 

### intro_help_defs.py

Contains functions for parsing and displaying the intro text and help text. 

### io_defs.py

Contains functions to take and parse player input. 

### main.py

Top-level main file, initializes player and calls floor functions. 

### nav_defs.py

Contains the navigation loop function.

### notebook_def.py

Contains the class definition for the notebook object, with accessors and mutators. 

### room_def.py

Contains the class definition for the Room object, with accessors and mutators.
