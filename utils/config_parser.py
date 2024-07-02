from pathlib import Path
from configparser import ConfigParser

# filename = inspect.getframeinfo(inspect.currentframe()).filename
# print(filename)
# path = os.path.dirname(os.path.abspath(filename))

cwd = Path.cwd()
config_path = cwd / 'config.ini'

parser = ConfigParser()
parser.read(config_path)
print(config_path)


def get_config(section, key):
    return parser[section][key]
