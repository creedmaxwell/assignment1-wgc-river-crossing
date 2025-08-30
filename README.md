# Wolf, Goat, and Cabbage River Crossing Puzzle Solver

This project implements a solver for the classic Wolf, Goat, and Cabbage river crossing puzzle using different search algorithms (BFS and IDS).

## Problem Description

A farmer needs to transport a wolf, a goat, and a cabbage across a river. The farmer can only carry one item at a time in the boat. If left unattended:
- The wolf will eat the goat
- The goat will eat the cabbage

The goal is to find the shortest sequence of moves to get everything safely across the river.

## Implementation

The project implements two search algorithms:
- Breadth-First Search (BFS)
- Iterative Deepening Search (IDS)

States are represented as tuples of 4 boolean values (farmer, wolf, goat, cabbage), where:
- 0 represents the left bank
- 1 represents the right bank

## Project Structure

```
assignment1-wgc-river-crossing/
├── domains/
│   ├── __init__.py
│   └── wgc.py           # Wolf, Goat, Cabbage domain implementation
├── search_core.py       # Search algorithms implementation
└── run.py              # Main script to run the solver
```

## Usage

To run the solver with BFS:
```bash
python -m run.py --algo bfs
```

To run the solver with IDS:
```bash
python -m run.py --algo ids
```

## Output Format

The program outputs:
- Solution cost and depth
- Number of nodes generated and expanded
- For BFS: maximum frontier size
- Complete solution path with each move

Example output:
```
Domain: WGC | Algorithm: BFS
Solution cost: 7 | Depth: 7
Nodes generated: 23 | Nodes expanded: 15 | Max frontier: 6
Path:
  1) Move Goat    (L,L,L,L) -> (R,L,R,L)
  2) Return alone (R,L,R,L) -> (L,L,R,L)
  ...
```