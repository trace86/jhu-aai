import os

from dotenv import load_dotenv

# ## run_command
#
# Runs a command in docker
#
# * **source**: Source docker instance name.
# * **target**: Target docker instance name.
# * **command**: command to operate from source to target
#
# **returns**: None.

load_dotenv()
attack = os.getenv('ATTACK')
defense = os.getenv('DEFENSE')

# In[1]:


def run_command_to_target(source: str, target: str, command: str):
    result = os.system(f"docker exec -ti {source} {command} {target}")
    return result
    

# %%


def run_command_to_self(source: str, command: str):
    print(source)
    result = os.system(f"docker exec -ti {source} {command}")
    return result


# %%
def cyber_move(player, command, verbose):
    if player == 1:
        result = run_command_to_target(attack, defense, command)
        if verbose:
            print("command ran to target complete ", result)
    elif player == 2:
        result = run_command_to_self(defense, command)
        if verbose:
            print("command ran to self with result ", result)

# %%
def start_game_docker():
    check_process = os.system("docker ps -a")
    if attack in check_process and defense in check_process:
        print("stopping all running containers")
        # stop_process = os.system("docker ps -q | xargs docker stop")
    print("start process...")
    # start_process = os.system(f"docker start {attack} {defense}")