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
    print(source, target)
    result = os.system(f"docker exec -ti {source} {command} {target}")
    print("command ran to target complete ", result)

# %%


def run_command_to_self(source: str, command: str):
    print(source)
    result = os.system(f"docker exec -ti {source} {command}")
    print("command ran to self with result ", result)

# %%
def cyber_move(player, command):
    if player == 1:
        run_command_to_target(attack, defense, command)
    elif player == 2:
        run_command_to_self(attack, command)