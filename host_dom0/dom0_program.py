#!/usr/bin/env python3

from dom0_client import *
from dom0_sql import *
import time

session = Dom0_session('192.168.217.21', 3001)


print('Waiting for 10 seconds...')
i=0
while i<1:
	#session.live(script_dir + 'log.xml')
	session.read_tasks(script_dir + 'tasks.xml')
	session.send_descs()
	session.send_bins()
	
	time.sleep(1)
	session.optimize(script_dir + 'opt.xml')

	session.start()
	time.sleep(3)
	i=i+1

while i<10:
	session.live(script_dir + 'log.xml')
	time.sleep(3)
	i=i+1
session.stop()


while i<15:
	session.live(script_dir + 'log.xml')
	time.sleep(3)
	i=i+1



#session.profile(script_dir + 'log.xml')
xml2sql(script_dir + 'log.xml', script_dir + 'dom0.db')

help()
code.interact(local=locals())
