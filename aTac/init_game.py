import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import sys
import keras
import game_play as gp
from dotenv import load_dotenv
import random
from datetime import datetime
from script_launcher import ScriptLauncher
from docker_move import start_game_docker, end_game_docker
import logging
root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)

sys.path.insert(1, os.getcwd())

load_dotenv()
# load vales from .env
root_path = os.getenv('ROOT_PATH')
len_board = int(os.getenv("LENGTH_OF_BOARD"))
num_games = int(os.getenv("NUMBER_OF_GAMES"))
docker = int(os.getenv("DOCKER"))
delay_output = True if int(os.getenv("OUTPUT_DELAY")) == 1 else False
generate_date = True if int(os.getenv("GENERATE_DATA")) == 1 else False
verbose_output = True if int(os.getenv("VERBOSE_OUTPUT")) == 1 else False
human = True if int(os.getenv("AI_VS_HUMAN")) == 1 else False
human_player = int(os.getenv("HUMAN_PLAYS"))
attacker_skill_level = int(os.getenv("ATTACKER_SKILL_LEVEL"))
defender_skill_level = int(os.getenv("DEFENDER_SKILL_LEVEL"))


#disable urllib3 messages
urllib3_logger = logging.getLogger('urllib3')
urllib3_logger.setLevel(logging.CRITICAL)

#disable tensorflow messages
urllib3_logger = logging.getLogger('tensorflow')
urllib3_logger.setLevel(logging.CRITICAL)

#configuring logger
filename = datetime.now().strftime('%Y%m%d%H%M_container_log_file.log')
filepath = f'{root_path}/container_moves/{filename}'
handler = logging.FileHandler(filepath, 'w', 'utf-8')
formatter = logging.Formatter('%(name)s %(message)s') # or whatever
handler.setFormatter(formatter) # Pass handler as a parameter, not assign
root_logger.addHandler(handler)

def play_games(len_board=3, num_games=3):
    model_3x3 = keras.models.load_model("AlphaToe3")
    model_5x5 = keras.models.load_model("AlphaToe5")
    logging.info("Loaded Keras models.")

    for i in range(1, num_games + 1):
        logging.info(f"\nplaying game {i} of {num_games}...")
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
                logging.info("Running AI vs Human 3x3 game play")
                winner, board = gp.ai_vs_human(model_3x3, rnd1=rnd1, rnd2=rnd2, len_board=len_board,
                                               verbose=verbose_output, delay=delay_output, generate_data=generate_date,
                                               human_plays=human_player, exploit_tracker=exploit_tracker,
                                               launcher=launcher, docker=docker, attacker_skill=attacker_skill_level,
                                               defender_skill=defender_skill_level)
            else:
                logging.info("Running AI vs AI 3x3 game play")
                winner, board = gp.ai_vs_ai(model_3x3, rnd1=rnd1, rnd2=rnd2, len_board=len_board, verbose=verbose_output,
                                            delay=delay_output, generate_data=generate_date,
                                            exploit_tracker=exploit_tracker, launcher=launcher, docker=docker,
                                            attacker_skill=attacker_skill_level, defender_skill=defender_skill_level)

            gp.printWinner(winner)

        elif len_board == 5:
            if human:
                logging.info("Running AI vs Human 5x5 game play")
                winner, board = gp.ai_vs_human(model_3x3, rnd1=rnd1, rnd2=rnd2, len_board=len_board,
                                               verbose=verbose_output, delay=delay_output, generate_data=generate_date,
                                               human_plays=human_player, exploit_tracker=exploit_tracker,
                                               launcher=launcher, docker=docker, attacker_skill=attacker_skill_level,
                                               defender_skill=defender_skill_level)
            else:
                logging.info("Running AI vs AI 5x5 game play")
                winner, board = gp.ai_vs_ai(model_5x5, rnd1=rnd1, rnd2=rnd2, len_board=len_board, verbose=verbose_output,
                                            delay=delay_output, generate_data=generate_date,
                                            exploit_tracker=exploit_tracker, launcher=launcher, docker=docker,
                                            attacker_skill=attacker_skill_level, defender_skill=defender_skill_level)
                
            gp.printWinner(winner)

        else:
            raise ValueError(f"We can't run a {len_board}x{len_board} game")


play_games(num_games=num_games, len_board=len_board)
if docker == 1:
    end_game_docker()
