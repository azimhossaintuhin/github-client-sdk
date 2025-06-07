import pathlib
import os
def get_env_file_location():    
    return pathlib.Path(__file__).parent.parent.parent.parent / ".env"


def load_env():
    if not os.path.exists(get_env_file_location()):
        get_env_file_location().touch()
    with open(get_env_file_location(), "r") as f:
        for line in f:
            key, value = line.strip().split("=")
            os.environ[key] = value
env = load_env()
