# libs
import os, datetime
from random import randrange
from utils.utils import Utils
from watcher import Watcher

# draw header
Utils.draw_header()

# log 'Initializing'
Utils.draw_log(status=True, datetime=Utils.get_current_datetime(), message='Initializing system.')

# how many async instances to launch
irand = randrange(1, 2)
instances = irand

# init watcher with instances
Watcher(instances)

# draw system end
Utils.draw_system_end()
