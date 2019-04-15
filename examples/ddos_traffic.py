from subprocess import call
import sys
import time

while True:
	# call(['ping','-c','1','-i','0.2',sys.argv[1]])
	call(['ping','-c','1','-i','0.2','10.0.0.7'])
