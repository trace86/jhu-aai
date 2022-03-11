import os
import sys
import keras
import game_play as gp
import random
from game_eval import show_intention
from dotenv import load_dotenv

sys.path.insert(1, os.getcwd())


load_dotenv()
# load vales from .env
exploit_3x3_file = f"{os.getenv('ROOT_PATH')}/{os.getenv('EXPLOIT_3x3')}"
exploit_5x5_file = f"{os.getenv('ROOT_PATH')}/{os.getenv('EXPLOIT_5x5')}"
set_5x5_file = f"{os.getenv('ROOT_PATH')}/{os.getenv('SET_5x5')}"
state_mapping_files = [exploit_5x5_file, exploit_3x3_file, set_5x5_file]
len_board = int(os.getenv("LENGTH_OF_BOARD"))
num_games = int(os.getenv("NUMBER_OF_GAMES"))


def play_games(state_mapping_files, len_board=3, num_games=3):
    for i in range(1, num_games + 1):
        print(f"\nplaying game {i} of {num_games}...")
        # start with clean slate
        for f in state_mapping_files:
            if os.path.exists(f):
                os.remove(f)
            else:
                print(f"File {f} does not exist.")

        if len_board == 3:
            model = keras.models.load_model("AlphaToe3")
            rnd1, rnd2 = random.uniform(0, 1), random.uniform(0, 1)
            attack_id = 2
            show_intention(attack_id)
            winner, board = gp.ai_vs_ai(model, len_board=len_board, rnd1=rnd1, rnd2=rnd2, verbose=True, delay=True)
            gp.printWinner(winner)

        if len_board == 5:
            model = keras.models.load_model("AlphaToe5")
            rnd1, rnd2 = random.uniform(0, 1), random.uniform(0, 1)
            winner, board = gp.ai_vs_ai(model, len_board=len_board, rnd1=rnd1, rnd2=rnd2, verbose=True, delay=True)
            gp.printWinner(winner)


play_games(state_mapping_files, num_games=num_games, len_board=len_board)
