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

# In[1]:


def run_command(source: str, target: str, command: str):
    result = os.system(f"docker exec -ti {source} {command} {target}")
    print("command ran to target with result ", result)
