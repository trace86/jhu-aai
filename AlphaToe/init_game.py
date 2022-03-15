import os
import sys
import keras
import game_play as gp
from dotenv import load_dotenv
import random
from datetime import datetime
from script_launcher import ScriptLauncher
from docker_move import start_game_docker, end_game_docker

sys.path.insert(1, os.getcwd())


load_dotenv()
# load vales from .env
len_board = int(os.getenv("LENGTH_OF_BOARD"))
num_games = int(os.getenv("NUMBER_OF_GAMES"))
docker = int(os.getenv("DOCKER"))
delay_output = True if int(os.getenv("OUTPUT_DELAY")) == 1 else False
generate_date = True if int(os.getenv("GENERATE_DATA")) == 1 else False
verbose_output = True if int(os.getenv("VERBOSE_OUTPUT")) == 1 else False
human = True if int(os.getenv("AI_VS_HUMAN")) == 1 else False
human_player = int(os.getenv("HUMAN_PLAYS"))


def play_games(len_board=3, num_games=3):
    model_3x3 = keras.models.load_model("AlphaToe3")
    model_5x5 = keras.models.load_model("AlphaToe5")
    print("Loaded Keras models.")

    for i in range(1, num_games + 1):
        print(f"\nplaying game {i} of {num_games}...")
        # start with clean slate
        random.seed(datetime.now())
        rnd1, rnd2 = random.uniform(0, 1), random.uniform(0, 1)
        exploit_tracker = {
            "exploit_initiated": False,
            "set_initiated": False
        }
        launcher = ScriptLauncher()
        
        if len_board == 3:
            if human:
                print("Running AI vs Human 3x3 game play")
                winner, board = gp.ai_vs_human(model_3x3, rnd1=rnd1, rnd2=rnd2, len_board=len_board,
                                               verbose=verbose_output, delay=delay_output, generate_data=generate_date,
                                               human_plays=human_player, exploit_tracker=exploit_tracker,
                                               launcher=launcher, docker=docker)
            else:
                print("Running AI vs AI 3x3 game play")
                winner, board = gp.ai_vs_ai(model_3x3, rnd1=rnd1, rnd2=rnd2, len_board=len_board, verbose=verbose_output,
                                            delay=delay_output, generate_data=generate_date,
                                            exploit_tracker=exploit_tracker, launcher=launcher, docker=docker)

            gp.printWinner(winner)

        elif len_board == 5:
            if human:
                print("Running AI vs Human 5x5 game play")
                winner, board = gp.ai_vs_human(model_3x3, rnd1=rnd1, rnd2=rnd2, len_board=len_board,
                                               verbose=verbose_output, delay=delay_output, generate_data=generate_date,
                                               human_plays=human_player, exploit_tracker=exploit_tracker,
                                               launcher=launcher, docker=docker)
            else:
                print("Running AI vs AI 5x5 game play")
                winner, board = gp.ai_vs_ai(model_5x5, rnd1=rnd1, rnd2=rnd2, len_board=len_board, verbose=verbose_output,
                                            delay=delay_output, generate_data=generate_date,
                                            exploit_tracker=exploit_tracker, launcher=launcher, docker=docker)
                
            gp.printWinner(winner)

        else:
            raise ValueError(f"We can't run a {len_board}x{len_board} game")


play_games(num_games=num_games, len_board=len_board)
end_game_docker()
