from functions5 import *
import random

model = keras.models.load_model("AlphaToe5")
rnd1, rnd2 = random.uniform(0, 1), random.uniform(0, 1)
print(rnd1, rnd2)
winner, board = ai_vs_ai(model, rnd1=rnd1, rnd2=rnd2)
printWinner(winner)
