# 15 Puzzle Solver with Branch and Bound

## Description
A python program to solve 15-puzzles using branch and bound algorithm. The program accepts an initial configuration of a 15-puzzle board and determines whether it is solvable or not. If it is solvable, it then proceeds to perform branch and bound algorithm to find a solution.

## 15-Puzzle
The 15 puzzle (also called Gem Puzzle, Boss Puzzle, Game of Fifteen, Mystic Square and many others) is a sliding puzzle having 15 square tiles numbered 1–15 in a frame that is 4 tiles high and 4 tiles wide, leaving one unoccupied tile position. Tiles in the same row or column of the open position can be moved by sliding them horizontally or vertically, respectively. The goal of the puzzle is to place the tiles in numerical order. ([Wikipedia](https://en.wikipedia.org/wiki/15_puzzle))

## Input File Format
The input file is in `txt` file format which contains a 4x4 matrix of the initial board configuration. Each element/block is separated by space, and the empty block may be represented by '0', '-', '--', or '16'.  

Examples of correct format:
```
05 01 03 04        1 2 3 4            6 5 2 4
09 02 07 08        0 5 6 8            9 1 3 8
-- 06 15 11        9 10 7 11          10 - 7 15
13 10 14 12        13 14 15 12        13 14 12 11
```
## Program Requirements
You need `python 3` to run this program.

## Running the Program
To clone this repository:
```
git clone https://github.com/FelineJTD/15-Puzzle-Solver-with-Branch-and-Bound
```

Make sure you are in the directory of the cloned repository to run the program.  

To run the program with an input file:
```
python3 src/main.py [filename.txt]
```
To run the program with a randomly generated board:
```
python3 src/main.py
```
!!! The algorithm of this program is not suited for boards that require a lot of nodes to be raised, attempting to run the program with a randomly-generated board may result in the program running for a very long time.  

It is recommended to use one of the given test cases in the test folder. Use this command to try it out:
```
python3 src/main.py ./test/tc1.txt
```
You can also add more boards in the test folder to try and solve them.

## Status
Program is _completed_

## Author
Felicia Sutandijo - 13520050