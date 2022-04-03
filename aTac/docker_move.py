import os
import docker
from time import sleep 
import logging

from datetime import datetime
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

def run_command_to_target(source: str, target: str, command: str):
    logging.info(f"operating container: {source.name}")
    result = source.exec_run( f"bash -c '{command}; sleep 10 ; exit'", stdout=True)
    logging.info(f"operation_result: {result}")
    return result
    

# %%


def run_command_to_self(source: str, command: str):
    logging.info(f"operating container: {source.name}")
    result = source.exec_run( f"{command}", stdout=True)
    logging.info(f"kill_process_result: {result}")
    result = source.exec_run( f"netstat -tulnp | grep LISTEN", stdout=True)
    logging.info(f"validation_result: {result}")
    return result


# %%
def cyber_move(player, command, attack, defense, verbose):
    if player == 1:
        result = run_command_to_target(attack, defense, command)
        if verbose:
            logging.info(f"command ran to target complete {result}")
    elif player == 2:
        result = run_command_to_self(defense, command)
        if verbose:
            logging.info(f"command ran to self with result {result}")

# %%
def start_game_docker(docker):
    if docker != 1:
        return "attack", "defense"
    logging.info("stopping existing containers...")
    for container in client.containers.list():
        container.stop()
    client.containers.prune()
    client.networks.prune()
    logging.info("start process...")
    docker_network = client.networks.create(network_name)
    attack_container = client.containers.run(attack, detach=True, auto_remove=True, network=docker_network.id, stdin_open=True, name=attack)
    defense_container = client.containers.run(defense, detach=True, auto_remove=True, network=docker_network.id, stdin_open=True, name=defense, cap_add=["SYS_PTRACE"], security_opt=["apparmor:unconfined"])
    logging.info("setup done")

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