# Super Pong
## Overview
This repository is an example of a simple game made with PyGame for the 2023 ACC Coding Challenge. This is a simple recreation of classic "Pong" that illustrates a basic architecture for creating games in PyGame. This README serves as a documentation sample that can be replicated for challenge submissions.

## Running the Code
This project was developed using [Python 3.10.1](https://www.python.org/downloads/release/python-3101/). "main.pyw" serves as the entrypoint to the application. The "requirements.txt" file includes all dependencies required in this project - to install all dependencies listed in this file, run the following command from command line:
```bash
py -m pip install -r requirements.txt
```
(See [this article](https://learnpython.com/blog/python-requirements-file/) for more information about generating and using requirements files)

## Building a Self-Contained Executable
The final submission for this challenge should be a single, self-contained .exe file that can be built with the "pyinstaller" library. Included in this repo is a "build_exe.bat" file that can be used to generate a self-contained .exe. The command within is as follows:
```bash
pyinstaller main.pyw --name "My Game" --onefile
```
This command builds the python project with a specified entrypoint file ("main.pyw"), names the output file with "--name", and indicates that all dependencies should be merged into a single .exe file with the "--onefile" flag.

## Design
### Main
The "Main" class serves as the primary orchestrator for game startup and the main execution loop. The "GameState" tracks which view we are currently on, and the "active game state mgr" child contains a manager component for the active view. The 3 game state managers are:
* Start Screen
* Gameplay
* End Screen

The main game loop at this level has three roles:
1. Pull events off of the event queue (e.g. exit, mouse input, game state change) and handle
2. Tell current active game state mgr to update for the current frame (more on that below)
3. Sleep for the specified FPS amount

### Start Screen Manager
This game state manager simply manages the start screen view and listens for it's "start" button to be clicked. On click, we push a custom "ON_START_GAME" event into the PyGame event queue for Main to handle on the next loop iteration and transition its active game state.

### Gameplay Manager
This manager is in charge of the actual game activity. It contains a "player_paddle" component, "ai_paddle" component, and "ball" component and controls activity around each. On each loop iteration, this manager executes the following actions:
1. Update:
    1. Update ball and paddle positions
    2. Detect and handle ball collisions
    3. Detect and handle ball passing bounds and updating score
    4. Detect and handle score passing max score threshold (triggering end of game event)
2. Draw:
    1. Trigger each component's drawing logic, based on its updated positioning
  
### End Screen Manager
Similar to Start Screen, this shows up after the end of a game with a single button to trigger returning to main game screen.

