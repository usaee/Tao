from __future__ import absolute_import
import sys

debug = 0

#####################################
# Adds a new term without a 
# definition attached
#####################################
def main(item,loc):
	item=item.lower()
	msg=item + ":" + loc + "\n"
	f=open("items.txt","a")
	f.write(msg)
	f.close()
