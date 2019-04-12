from subprocess import call
import sys
import time

while True:
	call(['ping','-c','1','-s','5',sys.argv[1]])
	time.sleep(4)
