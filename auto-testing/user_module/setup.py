from configparser import ConfigParser
from utility.constants import PathConstants

config_parser = ConfigParser()
# Reading  property file.
config_parser.read('ConfigFile.ini')

# Fetching  values from sections.
config_parser.get('DatabaseSection', 'database.dbname')
config_parser.get('Path', PathConstants.ROOT_PATH)
