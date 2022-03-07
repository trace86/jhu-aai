import os
import sys
sys.path.insert(1, os.getcwd())
from typing import List
import mapping as mp

from nmap_parser import parse_nmaprun_xml

from dotenv import load_dotenv
import os #provides ways to access the Operating System and allows us to read the environment variables
import pandas as pd


load_dotenv()
xml_file = f"{os.getenv('ROOT_PATH')}/{os.getenv('PORTSCAN_XML')}"
commands_csv = f"{os.getenv('ROOT_PATH')}/{os.getenv('COMMANDS_CSV')}"
attacks = pd.read_csv(commands_csv)

metasploit = {
    0: "scan_command",
    1: "use_command",
    2: "set_command",
    3: "exploit_command",
    4: "kill_process_command",
    5: "kill_daemon_command",
    6: "nop_command",
}

def show_intention(attack_id, attacks=pd.read_csv(commands_csv)):
    print(f"using vulnerability/exploit: {attacks.iloc[attack_id]['exploit_name']} "
          f"(linked port {attacks.iloc[attack_id]['linked_port']}")

# ## eval_move
#
# Main method for the graph traversal program. Takes in a previous and current state and returns the action performed in the cyber realm.
# * **prev_state**: The previous state of the game board.
# * **current_state**: The current state of the game board.
# * **debug**: Bool flag to print debug statements.
#
# **returns**: str.

# In[22]:


def eval_move(prev_state: List[List[int]], current_state: List[List[int]], attack_id: int = 0000, debug: bool = False) -> List[str]:
    exploit_file_3x3 = "exploit_3x3"
    exploit_file_5x5 = "exploit_5x5"
    set_file_5x5 = "set_5x5"
    mp.write_logging_files(exploit_file_3x3, exploit_file_5x5, set_file_5x5)
    move = mp.get_latest_move(prev_state, current_state)
    i = move[0]
    j = move[1]
    if current_state[i][j] == 1:  # attacker
        if debug: print("attacker move")
        if len(current_state) == 3:
            command = mp.eval_attacker_3x3(i, j, current_state, exploit_file_3x3, debug)
        if len(current_state) == 5:
            command = mp.eval_attacker_5x5(i, j, current_state, exploit_file_5x5, set_file_5x5, debug)
    elif current_state[i][j] == 2:  # defender
        if debug: print("defender move")
        if len(current_state) == 3:
            command = mp.eval_defender_3x3(i, j, current_state, exploit_file_5x5, debug)
        if len(current_state) == 5:
            command = mp.eval_defender_5x5(i, j, current_state, exploit_file_5x5, set_file_5x5, debug)
    else:
        raise ValueError(f"unexpected game value: ({i}, {j})")  # ruh roh
    # return command
    for c in command:
        print(c)
        print(metasploit[c])

        if c == 0:
            ports = parse_nmaprun_xml(xml_file)
        attacks.iloc[attack_id][metasploit[c]]
    return [metasploit[c] for c in command]


board_old = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 2, 2, 0, 0],
    [0, 0, 0, 0, 0]]
board_new = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1],
    [0, 2, 2, 0, 0],
    [0, 0, 0, 0, 0]]
assert eval_move(board_old, board_new, debug=False) == ["set_command"]

# In[23]:


board_old = [
    [0, 0, 1],
    [0, 1, 0],
    [0, 0, 2]]
board_new = [
    [0, 0, 1],
    [0, 1, 0],
    [2, 0, 2]]
# assert eval_move(board_old, board_new, debug=False) == ["kill_process_command"]
