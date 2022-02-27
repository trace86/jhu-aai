# AlphaToe - Tic Tac Toe AI

The neural networks for 3x3 and 5x5 Tic Tac Toe (AlphaToe3 and AlphaToe5, respectively :nail_care:) have already been trained. 

AlphaToe3 has been trained for 100 epochs on a dataset of 1 million randomly played tic tac toe games and results in a 68% validation accuracy.

AlphaToe5 has been trained for 1000 epochs on a dataset of 100,000 randomly played tic tac toe games and results in a 57% validation accuracy. AlphaToe5 uses a neural network very similar in structure to AlphaToe3, but with the number of nodes and fraction of dropout nodes in some layers slightly increased to account for the larger game state of 5x5 tic tac toe vs. 3x3 tic tac toe.

The following files are in this directory:
* AlphaToe3 and AlphaToe5 Keras Neural Network Models (sub-directories)
* 3x3_play.py and 5x5_play.py which simulate a Tic Tac Toe game between two AIs
* functions3.py and functions5.py which contain supporting functions for the AIs to play

The source code upon which AlphaToe has been developed originates from Daniel Sauble - https://github.com/djsauble/tic-tac-toe-ai
