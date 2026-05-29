# Tic-Tac-Toe AI using Search Algorithms
## Overview

This project implements different AI algorithms for playing Tic-Tac-Toe.

## Algorithms implemented:  

Minimax  
Alpha-Beta Pruning  
Heuristic Alpha-Beta  
Monte-Carlo Tree Search (MCTS)  

Player X is the maximizing player and Player O is the minimizing player.

Empty cells are represented using .

Board positions:

0 | 1 | 2
3 | 4 | 5
6 | 7 | 8

## Test Case 1 — Winning Move

Initial Board:

X X .
O O .
. . .

Expected Best Move:

2

because placing X at position 2 gives an immediate win.

## Test Code
state = TicTacToe(  
    board=['X','X','.',  
           'O','O','.',  
           '.','.','.'],  
    current_player='X'  
)

print("Initial Board")
state.display()

minimax_agent = MinimaxAgent()
print("Minimax move:", minimax_agent.best_move(state))

ab_agent = AlphaBetaAgent()
print("AlphaBeta move:", ab_agent.best_move(state))

heuristic_agent = HeuristicAlphaBetaAgent()
print("Heuristic AlphaBeta move:", heuristic_agent.best_move(state))

mcts_agent = MCTSAgent()  
print("MCTS move:", mcts_agent.best_move(state, 2000)) 

## Expected Output  
Minimax move: 2  
AlphaBeta move: 2  
Heuristic AlphaBeta move: 2  
MCTS move: 2 


# AI Based Travel Planner Using Ontology
## Overview

This project implements a simple AI-based Travel Planner using Ontology.

The system stores knowledge about:

Places
Foods
Hotels
Tourist Places

using Protégé ontology and accesses them using Python and Owlready2.

The AI recommends places, foods, and hotels based on relationships stored in the ontology.

Tools Used  
Protégé  
Python  
Owlready2  
VS Code  
Ontology Structure  

## Classes created:  

Place  
Food  
Hotel  
Tourist_Place  
Transport  

## Example Individuals:  

Darjeeling  
Momo  
Tiger_Hill  
Mayfair  

## Example Relationships:  

Momo → famousin → Darjeeling  
Tiger_Hill → locatedIn → Darjeeling  
Mayfair → nearTo → Tiger_Hill  
Working  

The ontology is created in Protégé and saved as:  

# travel.owl  

The main python file for all the implementation is saved as:  

# main.py  

Python loads the ontology using Owlready2 and reads:  

places  
foods  
hotels  
relationships  

The AI then recommends travel information based on user input.  

## Sample Output  
Enter a place name: Darjeeling  

Recommended Foods:  
- Momo  

Tourist Places:  
- Tiger_Hill  

Hotels:  
- Mayfair  

