
import time
import sys
import random
import emotionValues as feel

def response(s):
	print()
	sys.stdout.write("Tao: \n")
	for c in s:
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.005)
	print()
	print()
	
def emotion(s):
	if "you feeling" in s:
		feel.main(s)