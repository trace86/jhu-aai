import os
import subprocess

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
network_name = "adversarial"
# In[1]:


def run_command_to_target(source: str, target: str, command: str):
    result = subprocess.check_output(f"docker exec -ti {source} {command} {target}", shell=True)
    return result
    

# %%


def run_command_to_self(source: str, command: str):
    print(source)
    result = subprocess.check_output(f"docker exec -ti {source} {command}", shell=True)
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
    check_process = subprocess.check_output("docker ps -a", shell=True)
    print(check_process)
    print(type(check_process))
    print(type(attack))
    if attack in check_process and defense in check_process:
        print("stopping all running containers")
        # stop_process = subprocess.check_output("docker ps -q | xargs docker stop", shell=True)
        # remove_network_process = subprocess.check_output(f"docker network rm {network_name}")
    print("start process...")
    # start_process = subprocess.check_output(f"docker start {attack} {defense}", shell=True)
    # network_process = subprocess.check_output(f"docker network create {network_name}")