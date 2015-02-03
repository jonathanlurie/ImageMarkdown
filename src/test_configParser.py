from ConfigParser import *


parser = SafeConfigParser()
parser.read('settings.ini')

try:
    print parser.get('config', 'tempFolder')
    print parser.get('config', 'localImageFolder')
    print parser.get('config', 'pouet')
except NoOptionError as e:
    print e
