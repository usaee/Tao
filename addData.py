from __future__ import absolute_import
import sys

debug = 0


#####################################
# Adds a new term without a 
# definition attached
#####################################
def main(t,df):
	t=t.lower()
	df=df.lower()
	if "?" in t:
		t = t.replace("?","")
	if "-" in t:
		t = t.replace("-","")
	msg = t + ":" + df + "\n"
	f=open("terms.txt","a")
	f.write(msg)
	f.close()
