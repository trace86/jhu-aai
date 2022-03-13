import os
import sys
import keras
import game_play as gp
import random
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
delay_output = True if int(os.getenv("OUTPUT_DELAY")) == 1 else False
generate_date = True if int(os.getenv("GENERATE_DATA")) == 1 else False
verbose_output = True if int(os.getenv("VERBOSE_OUTPUT")) == 1 else False
human = True if int(os.getenv("AI_VS_HUMAN")) == 1 else False
human_player = int(os.getenv("HUMAN_PLAYS"))


def play_games(state_mapping_files, len_board=3, num_games=3):
    model_3x3 = keras.models.load_model("AlphaToe3")
    model_5x5 = keras.models.load_model("AlphaToe5")
    print("Loaded Keras models.")

    for i in range(1, num_games + 1):
        print(f"\nplaying game {i} of {num_games}...")
        # start with clean slate
        for f in state_mapping_files:
            if os.path.exists(f):
                os.remove(f)
            else:
                print(f"File {f} does not exist.")
        rnd1, rnd2 = random.uniform(0, 1), random.uniform(0, 1)
        if len_board == 3:
            if human:
                print("Running AI vs Human 3x3 game play")
                winner, board = gp.ai_vs_human(model_3x3, rnd1=rnd1, rnd2=rnd2, len_board=len_board, verbose=verbose_output,
                                        delay=delay_output, generate_data=generate_date, human_plays=human_player)
            else:
                print("Running AI vs AI 3x3 game play")
                winner, board = gp.ai_vs_ai(model_3x3, rnd1=rnd1, rnd2=rnd2, len_board=len_board, verbose=verbose_output,
                                            delay=delay_output, generate_data=generate_date)
            gp.printWinner(winner)

        elif len_board == 5:

            if human:
                print("Running AI vs Human 5x5 game play")
                winner, board = gp.ai_vs_human(model_3x3, rnd1=rnd1, rnd2=rnd2, len_board=len_board,  verbose=verbose_output,
                                        delay=delay_output, generate_data=generate_date, human_plays=human_player)
            else:
                print("Running AI vs AI 5x5 game play")
                winner, board = gp.ai_vs_ai(model_5x5, rnd1=rnd1, rnd2=rnd2, len_board=len_board, verbose=verbose_output,
                                            delay=delay_output, generate_data=generate_date)
            gp.printWinner(winner)

        else:
            raise ValueError(f"We can't run a {len_board}x{len_board} game")


play_games(state_mapping_files, num_games=num_games, len_board=len_board)
