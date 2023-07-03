#!usr/bin/python

import os

msg = input('commit message:')
os.system('git add .')
os.system('git commit -m"{}"'.format(msg))
os.system('git push')