
import hear
import sys
import console
import AiAnswer
import time

#print("""Quick Commands
print("""a. add image
b. add term/data
c. add item
d. find image
e. find item
f. find term
g. list of image names
q. Quit/Exit This Program Loop
cc. Reset The Prompt
""")

def strt():
	#print("""Quick Commands
	print("""a. add image
b. add term/data
c. add item
d. find image
e. find item
f. find term
g. list of image names
q. Quit/Exit This Program Loop
cc. Reset The Prompt
""")

while(1):
	v = input("User: ")
	if v == "q":
		AiAnswer.response("""
Goodbye sir or madam, and may you farewell in all of your journeys!

              (^‿^)
""")

		#time.sleep(10)
		break
		#console.clear()
		#sys.exit()

	elif v == 'cc':
		console.clear()
		strt()

	elif v == 'a':
		v = "add image"
		print()
		hear.stimAction(v)
		print()
		console.clear()
		strt()

	elif v == 'b':
		v = "add term"
		print()
		hear.stimAction(v)
		print()
		console.clear()
		strt()

	elif v == 'c':
		v = "add item"
		print()
		hear.stimAction(v)
		print()
		console.clear()
		strt()

	elif v == 'd':
		v2 = input("\tImage name: ")
		v = "show image " + v2
		print()
		hear.stimAction(v)
		print()

	elif v == 'e':
		v2 = input("\tItem name: ")
		speak = input("Would you like for me to read this out loud?")
		
		if 'y' in speak:
			speak = 1
		else:
			speak = 0
		v = "find item " + v2
		print()
		hear.stimAction(v,speak)
		print()

	elif v == 'f':
		v2 = input("\tTerm name: ")
		v = "what is " + v2
		print()
		hear.stimAction(v)
		print()
		
	elif v == 'g':
		console.clear()
		v = "show list"
		print()
		hear.stimAction(v)
		print()

	else:
		print()
		hear.stimAction(v)
		print()
