import os
import sys

import keras

sys.path.insert(1, os.getcwd())
from functions3 import *
import random
from game_eval import show_intention

model = keras.models.load_model("AlphaToe3")
rnd1, rnd2 = random.uniform(0, 1), random.uniform(0, 1)

print(rnd1)
print(rnd2)
attack_id = 2

show_intention(attack_id)

winner, board = ai_vs_ai(model, rnd1=rnd1, rnd2=rnd2, verbose=True, attack_id=attack_id)
printWinner(winner)

