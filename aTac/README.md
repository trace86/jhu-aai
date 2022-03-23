# AlphaToe Neural Networks - Tic Tac Toe AI

The neural networks for 3x3 and 5x5 Tic Tac Toe (AlphaToe3 and AlphaToe5, respectively :nail_care:) have already been trained. 

AlphaToe3 has been trained for 100 epochs on a dataset of 1 million randomly played tic tac toe games and results in a 68% validation accuracy.

AlphaToe5 has been trained for 1000 epochs on a dataset of 100,000 randomly played tic tac toe games and results in a 57% validation accuracy. AlphaToe5 uses a neural network very similar in structure to AlphaToe3, but with the number of nodes and fraction of dropout nodes in some layers slightly increased to account for the larger game state of 5x5 tic tac toe vs. 3x3 tic tac toe.

The source code upon which aTac has been developed originates from Daniel Sauble - https://github.com/djsauble/tic-tac-toe-ai

## Running aTac
To run game simulations:
* Clone this repo
* In `aTac` directory, create a `.env` file populated as below
```.env
# Key Files
PORTSCAN_XML="nmap/portscan_out.xml"
ATTACK_PORTS_PK = "attack_ports/attack_ports.pickle"
COMMANDS_CSV="vulnerability_execute/commands2.csv"
VULNERABILITY_SCRIPTS_DIR = "vulnerability_scripts"
ROOT_PATH = "/opt/capstone/jhu-aai/aTac/io"
GAMEPLAY_5x5 = "gameplay/output_5x5.csv"
GAMEPLAY_3x3 = "gameplay/output_3x3.csv"
# Game Parameters
OUTPUT_DELAY=1  # python-dotenv does not parse boolean, so 1 == True and 0 == False
GENERATE_DATA=0 # python-dotenv does not parse boolean, so 1 == True and 0 == False
VERBOSE_OUTPUT=1 # python-dotenv does not parse boolean, so 1 == True and 0 == False
AI_VS_HUMAN=0 # python-dotenv does not parse boolean, so 1 == True and 0 == False
HUMAN_PLAYS=2 # 1 == ATTACK(X), 2 == DEFENSE(O)
NUMBER_OF_GAMES=3
LENGTH_OF_BOARD=3
# Chaos Agent
ATTACKER_SKILL_LEVEL=3 # ranges from 0 (state backed hacker) to 5
DEFENDER_SKILL_LEVEL=3
# Docker
ATTACK="kali-everything"
DEFENSE="metasploitable2"
DOCKER=0 # python-dotenv does not parse boolean, so 1 == True and 0 == False
```
* Update `NUMBER_OF_GAMES` and `LENGTH_OF_BOARD` variables as necessary
* Run `init_game.py`

## Running with Docker
To run code in Docker
* Clone this repo
* Add `.env` file to `aTac` directory, see above for content
* Update volume path to your local machine in `docker-compose.yml`
* Run `docker-compose up`
* Run `docker exec -it $container_name` and `cd` to `/opt/capstone/jhu-aai/aTac` directory and run `python init_game.py`

## Changelog
3/11/2022: SK refactored code to run everything with `init_game`
3/6/2022: added Samra's mapping into the 3x3 tic tac toe.

1) All the files herein should be in the same directory.
2) The intended vulnerability/exploit is specified in the 3x3_play.py script. Simply change the attack_id variable to the ID of the intended/vulnerability exploit (from commands.csv). Note that the commands.csv file is loaded into mapping.py and does not need to be loaded elsewhere.
3) In mapping.py, the IP address of the target machine can be changed in the parse() function. Currently it is set to the IP address of Nawal's Metasploitable 2 image.
4) Run 3x3_play.py