from functions import *

model_name = "model_epochs=1000_batch=100"
model = keras.models.load_model(model_name)

simulate_games = [simulateGame(p1=model, p2=model, rnd=0.6) for _ in range(1000)]
gameStats(simulate_games, player=1, save=True, filename="{0}.results".format(model_name))



board = initBoard()
# rnd parameter can be used as a "seed" so there is some randomness in the AIs moves
play_game(board, model, rnd=0.0)