from functions3 import *
import random

attacks = pd.read_csv("commands.csv")

model = keras.models.load_model("AlphaToe3")
rnd1, rnd2 = random.uniform(0, 1), random.uniform(0, 1)

attack_id = 2

print("Using vulnerability/exploit: {0} (linked port {1})...".format(attacks.iloc[attack_id]["exploit_name"], attacks.iloc[attack_id]["linked_port"]))

winner, board = ai_vs_ai(model, rnd1=rnd1, rnd2=rnd2, verbose=True, attack_id=attack_id)
printWinner(winner)

