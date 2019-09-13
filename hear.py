

import searchAlg

import addData

import addImage

import addItem

import addMemory

import findImage  # .getIM(str)

import findStuff

import AiAnswer

import sys

import time

import voiceSynth

#####################################
debug = 0  # general debug.

debug2 = 0 # shows the stim section
#            that was triggered.


def handle_not_found(ans):
	if "no" in ans or "na" in ans:
		print("Woops, sorry")
	else:
		print("Awesome!")


def stimAction(stim,speak):
	found = 0
	L = ["Yes sir, i am here","next response"]
	
	stim=stim.strip()
	stim=stim.lower()
	if "tao" in stim:
		if debug == 1:
			print(stim)
		stim=stim.replace("tao ","")
		if debug == 1:
			print(stim)
	if "please " in stim:
		stim = stim.replace("please ","")
#####################################
#              WHO
#####################################
	if "who " in stim or "whos " in stim or "who's " in stim:
		found = 1
		if " is " in stim:
			pass
		elif " are " in stim:
			pass

#####################################
#              WHAT
#####################################
	elif "what " in stim or "whats " in stim or "what's " in stim:
		
		found = 2
		
		refine,got = searchAlg.main(stim,3)
		
		speak = input("Would you like for me to read this out loud?")
		
		if 'y' in speak:
			voiceSynth.speak(refine)
		else:
			AiAnswer.response(refine)
		
		if got == 0 and debug == 1:
			ans = input("\nUser: ")
			ans = ans.lower()
			handle_not_found(ans)
			
#####################################
#              WHERE
#####################################
	elif "where " in stim or "wheres " in stim or "where's " in stim or "find " in stim:

		found = 3

		refine,got = searchAlg.main(stim,2)
		
		if speak == 1:
			voiceSynth.speak(refine)
		else:
			AiAnswer.response(refine)

#####################################
#              WHEN
#####################################
	elif "when " in stim or "whens " in stim or "when's " in stim:
		found = 4
		
		if " did " in stim:
			pass
		elif " was " in stim:
			pass
		elif " do " in stin:
			pass
		elif " is " in stim:
			pass

#####################################
#              WHY
#####################################
	elif "why " in stim or "whys " in stim or "why's " in stim:
		found = 5
		if " is " in stim:
			pass
		elif " did " in stim:
			pass
		elif " are " in stim:
			pass

#####################################
#              SHOW
#####################################
	elif "show" in stim:
		
		found = 6
		
		refine,got = searchAlg.main(stim,1)
		
		if got == 0 and debug == 1:
			fi = findImage.getIM(refine)
			ans = input("\nUser: ")
			ans = ans.lower()
			handle_not_found(ans)
		elif got == 2:
			for i in refine:
				print(i)
				time.sleep(0.05)
		else:
			findImage.getIM(refine)
			
#####################################
#              HOW
#####################################
	elif "how " in stim or "hows " in stim or "how's " in stim:
		found = 7
		if " do " in stim:
			pass
		elif " does " in stim:
			pass
		elif " can " in stim:
			pass
		elif " many " in stim:
			pass
		
#####################################
	elif "open " in stim:
		found = 8
		pass
#####################################

	#elif "send " in stim:
#		found = 9
#		pass

#####################################
	elif "search " in stim:
		found = 10
		refine,got = searchAlg.main(stim,3)
		
		AiAnswer.response(refine)
		#print(refine)
		
		if got == 0 and debug == 1:
			ans = input("\nUser: ")
			ans = ans.lower()
			handle_not_found(ans)
#####################################

	elif "get " in stim:
		found = 11
		pass

#####################################
	elif "add " in stim:
		sp = stim.split()
		if debug == 1:
			print(sp)
		if "term" in sp or "data" in sp:
			tr = input("\tTerm: ")
			print()
			df = input("\tDefinition: ")
			addData.main(tr,df)
		if "image" in sp:
			found = 12
			addImage.add()
		if "item" in sp:
			found = 12
			itm = input("Item: ")
			location = input("Location: ")
			itm = itm.lower()
			location = location.lower()
			
			if itm == 'q' or location == 'q':
				sys.exit()
			
			addItem.main(itm,location)
			
#####################################
	elif "you" in stim:
		found = 14
		if "there" in stim:
			AiAnswer.response(L[0])
#####################################

	else:
		found = 15
			# this section is for asking
			# tao personal/social questions
		pass

	if debug2 == 1:
		print(found)
	

















