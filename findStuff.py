from six.moves import zip
from six.moves import input
import sys
import time
import console

debug = 0
debug2 = 0
debug3 = 0

def main(u_in):
  global debug,debug2,debug3
  print("\nSearching for: "+u_in)
  match=0
  match2=0
  match3=0
  li=[]
  
  u_in.lower()
  u_in = u_in.strip()
  
  if "?" in u_in: # Removes any (?)
    u_in = u_in.replace("?","")
  if "-" in u_in: # Removes any (-)
    u_in = u_in.replace("-","")
  if "what is " in u_in:
    u_in = u_in.replace("what is","")
  elif "where is " in u_in:
  	u_in = u_in.replace("where is","")
  elif "where are " in u_in:
  	u_in = u_in.replace("where are","")
  if "the " in u_in:
  	u_in=u_in.replace("the","")
  if "my " in u_in:
  	u_in=u_in.replace("my","")
  
  d = {}
  
  f=open("items.txt","r")
  rfl=f.readlines()
  for i in rfl:
	  i=i.lower()
	  j=i.strip("\n")
	  k=j.split(":")
	  d[k[0]]=k[1]

  pick = {}
  match = 0
  perc = 0
  c=0
  cc=0
  cntr=0
  wordP=0
  word_guess=0

  u_in = u_in.split()
  for i in u_in:
    c += 1

  l = (len(d))

  for i in d:
    a = i.split()
    for num in a:
    	cc+=1
    a2 = c
    for k in a:
        for j in u_in:
          if j == k:
            match += 1
    match = float(match)
    c = float(c)
    match2=int((match/cc)*100)
    if c == 1 and match2 < 50:
    	kk=""
    	jj=""
    	list2=[]
    	list3=[]
    	l2=0
    	l3=1
    	mm=0
    	u2 = u_in[0]
    	for ii in u2:
    		list2.append(ii)
    	l2=len(list2)
    	if cc < 3:
    		for k in a[0]:
    			list3.append(k)
    		l3=len(list3)
    	for i5 in range(20):
    		try:
    			x=list2[i5]
    			for aa in list3:
    				if aa == x:
    					mm += 1
    					#print(aa)
    		except:
    			break
    	wordP=int((mm/l3)*100)
    	if wordP > 50:
    		word_guess=1
    if word_guess == 1:
    	pick[a[0]]=wordP
    	word_guess=0
    	li.append(wordP)
    else:
    	pick[i] = match2
    	li.append(match2)
    match = 0
    cc=0
  best = max(list(zip(list(pick.values()),list(pick.keys()))))
  pm=0
  for i in d:
  	if i==best[1]:
  		pm=(li[cntr])
  	cntr+=1
  if(pm < 50):
  	print("Answer:\nNo match found with certainy above 50%...")
  else:
  	print('{} should be located at: {}'.format(best[1],d.get(best[1])))
#############################

if debug == 1:
	while(1):
		ui=str(input("> "))
		if(ui == 'q'):
		  sys.exit()
		else:
			main(ui)
		
#else:
	#console.clear()
	#main(sys.argv[1])




