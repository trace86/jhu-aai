import os
import subprocess
import docker
from time import sleep 

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
root_path = os.getenv('ROOT_PATH')
portscan_full_path = os.getenv('PORTSCAN_XML')
network_name = "adversarial"
client = docker.from_env()


# In[1]:

def wait_for_container_to_start(container):
    
    timeout = 120
    stop_time = 3
    elapsed_time = 0

    while container.status != 'running' and elapsed_time < timeout:
        print(container.status)
        sleep(stop_time)
        elapsed_time += stop_time
        print("waiting...", container.name)
        continue
    
    if elapsed_time >= timeout:
        return False
    
    return True


def run_command_to_target(source: str, target: str, command: str):
    print(source.name)
    result = source.exec_run( f"bash -c '{command}; sleep 10 ; exit'", stdout=True)
    print(result)
    return result
    

# %%


def run_command_to_self(source: str, command: str):
    print(source.name)
    result = source.exec_run( f"{command}", stdout=True)
    result = source.exec_run( f"netstat -tulnp | grep LISTEN", stdout=True)
    print(result)
    return result


# %%
def cyber_move(player, command, attack, defense, verbose):
    if player == 1:
        result = run_command_to_target(attack, defense, command)
        if verbose:
            print("command ran to target complete ", result)
    elif player == 2:
        result = run_command_to_self(defense, command)
        if verbose:
            print("command ran to self with result ", result)

# %%
def start_game_docker(docker):
    if docker != 1:
        return "attack", "defense"
    print("stopping existing containers...")
    for container in client.containers.list():
        container.stop()
    client.containers.prune()
    client.networks.prune()
    print("start process...")
    docker_network = client.networks.create(network_name)
    attack_container = client.containers.run(attack, detach=True, auto_remove=True, network=docker_network.id, stdin_open=True, name=attack)
    defense_container = client.containers.run(defense, detach=True, auto_remove=True, network=docker_network.id, stdin_open=True, name=defense, cap_add=["SYS_PTRACE"], security_opt=["apparmor:unconfined"])
    print("setup done")

    return attack_container, defense_container
 
# %%
def end_game_docker():
    client.containers.prune()

# %%
def get_nmap(attack_container):
    container_name = attack_container.name
    portscan_path = portscan_full_path.split('/')[0]
    portscan_file_name = portscan_full_path.split('/')[1]
    attack_container.exec_run( f"nmap -oX {portscan_file_name} {defense}")
    os.system(f'docker cp {container_name}:/{portscan_file_name} {root_path}/{portscan_path}')