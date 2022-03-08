import os
import sys
import keras
sys.path.insert(1, os.getcwd())
from functions3 import *
import random
from game_eval import show_intention
from dotenv import load_dotenv


load_dotenv()
exploit_5x5_file = f"{os.getenv('ROOT_PATH')}/{os.getenv('EXPLOIT_5x5')}"
exploit_3x3_file = f"{os.getenv('ROOT_PATH')}/{os.getenv('EXPLOIT_3x3')}"
set_5x5_file = f"{os.getenv('ROOT_PATH')}/{os.getenv('SET_5x5')}"
rf_3x3_csv = f"{os.getenv('ROOT_PATH')}/{os.getenv('RF_3x3_CSV')}"

state_mapping_files = [exploit_5x5_file, exploit_3x3_file, set_5x5_file]
num_games = 5000

for game in range(0, num_games):
    for f in state_mapping_files:
        if os.path.exists(f):
            os.remove(f)
        else:
            print("Can not delete the file as it doesn't exists")

    model = keras.models.load_model("AlphaToe3")
    rnd1, rnd2 = random.uniform(0, 1), random.uniform(0, 1)

    attack_id = 2

    show_intention(attack_id)

    winner, board = ai_vs_ai(model, rnd1=rnd1, rnd2=rnd2, verbose=True, attack_id=attack_id)
    printWinner(winner)

