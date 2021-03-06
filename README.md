# Mars Rover
## 🤔 The Problem
A squad of robotic rovers are to be landed by NASA on a plateau on Mars. This plateau, which is curiously rectangular, must be navigated by the rovers so that their on-board cameras can get a complete view of the surrounding terrain to send back to Earth.

A rover's position and location is represented by a combination of x and y co-ordinates and a letter representing one of the four cardinal compass points. The plateau is divided up into a grid to simplify navigation. An example position might be 0, 0, N, which means the rover is in the bottom left corner and facing North.

In order to control a rover, NASA sends a simple string of letters. The possible letters are 'L', 'R' and 'M'. 'L' and 'R' makes the rover spin 90 degrees left or right respectively, without moving from its current spot. 'M' means move forward one grid point, and maintain the same heading.

Assume that the square directly North from (x, y) is (x, y+1).

The first line of input is the upper-right coordinates of the plateau, the lower-left coordinates are assumed to be 0,0. The rest of the input is information pertaining to the rovers that have been deployed. Each rover has two lines of input. The first line gives the rover's position, and the second line is a series of instructions telling the rover how to explore the plateau.

The position is made up of two integers and a letter separated by spaces, corresponding to the x and y coordinates and the rover's orientation.

Each rover will be finished sequentially, which means that the second rover won't start to move until the first one has finished moving.

The output for each rover should be its final coordinates and heading.

Input:
5 5
1 2 N
LMLMLMLMM
3 3 E
MMRMMRMRRM

Output:
1 3 N
5 1 E

## 💡 Solution
This solution created using python 3.10.4

### ⬇ installing dependencies
First create the virtual environment, then install the dependencies. For that you can use virtualenv and pip:
```bash
python -m venv venv

source venv/bin/activate

pip install -r requirements.txt
```
Or you can use [Poetry](https://python-poetry.org):
```bash
poetry shell

poetry install
```

### ▶️ Running the code
To run, just run the main.py file as a module.
```bash 
python -m src.main
```

### 🧪 Running Cucumber BDD tests
To run the Cucumber tests, run the following command:
```bash
behave
```
