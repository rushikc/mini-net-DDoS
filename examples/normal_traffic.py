from subprocess import call
import sys
import time

while True:
	# call(['ping','-c','1','-s','5',sys.argv[1]])
	call(['ping','-c','1','-s','5','10.0.0.7'])
	time.sleep(1.5)
