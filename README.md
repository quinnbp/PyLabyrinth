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

### main.py

Top-level main file, initializes player and builds labyrinth.

### labyrinth_cls.py

Contains the labyrinth class, responsible for both parsing the build file and tracking location and solved state. Also contains functionality to implement puzzles and 'special' rooms within the maze. Delegates to navigator to run central game loop.

### char_def.py

Contains the class definition for the player character object. This object maintains state data for the location of the player in the maze, as well as inventory and thread data. 

### room_def.py

Contains the class definition for the Room object, with accessors and mutators.

### intro_help_defs.py

Contains functions for parsing and displaying the intro text and help text. 

### navigator_cls.py

Contains the navigator class which parses and implements user input to take and use objects, and navigate in the maze.  Handles all room-recursive actions internally. 

### first_floor.py, second_floor.py, third_floor.py, etc  (deprecated)

Contains a function definition for each floor (level) of the labyrinth. These functions contain similar main loops with
different checks for special conditions on rooms, as well as separate internal functions for puzzles or items. (This design structure is deprecated from an older version, replaced by labyrinth_cls.)

### file_parser.py (deprecated)

Contains function definitions allowing the floor functions to parse their structure files into a list of Room objects. (This was deprecated from an older version, replaced by functionality in labyrinth_cls.)

### io_defs.py (deprecated)

Contains functions to take and parse player input. (This is deprecated from an earlier version and was replaced by navigator_cls.)

### nav_defs.py (deprecated)

Contains the navigation loop function. (This is deprecated from an earlier version and was replaced by navigator_cls.)

### notebook_def.py (deprecated)

Contains the class definition for the notebook object, with accessors and mutators. (This was deprecated from an earlier version and is currently not implemented).


