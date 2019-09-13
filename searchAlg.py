from six.moves import zip
from six.moves import input
import sys
import time
import console

deb    = 0
debug  = 0
debug2 = 0
debug3 = 0


def image(u_in,req):
  global debug,debug2,debug3
  if debug == 1:
    print("\nSearching for: "+u_in)
  match=0
  match2=0
  match3=0
  li=[]
    
  d = {}
  d2 = {}
  
  f=open("imageList.txt","r")
  rfl=f.readlines()
  for i in rfl:
    i=i.lower()
    j=i.strip("\n")
    k=j.split(":")
    d[k[0]]=k[1]
    d2[k[0]]=k[1]

  pick = {}
  match = 0
  perc = 0
  c=0
  cc=0
  cntr=0
  wordP=0
  word_guess=0

  userN = u_in
  u_in = u_in.split()
  for i in u_in:
    c += 1

  l = (len(d))
  
  imList = []
  for i in d2:
    a5 = i.split(":")
    a5 = str(a5[0])
    imList.append(a5)

  for i in d:
    line = i
    a = i.split() # splits the line

    for num in a: # gets number of 
                  # words in the line
      cc+=1

    a2 = c # gets the number of words
           # input by the user

    for k in a: # for each word 
                # in the term

        for j in u_in: # for each
                       # word in the
                       # user input
                       
          if j == k: # does user word
                     # match the word
                     # in the term?
            match += 1

    match = float(match)
    c = float(c)
    match2=int((match/cc)*100)
    if c == 1 and match2 < 50:
    #if match2 < 50:
    	kk=""
    	jj=""
    	list2=[]
    	list3=[]
    	l2=0
    	l3=1
    	mm=0
    	u2 = u_in[0] # get the first 
    	             # word of the user
    	             
    	#list2 = [ch for ch in userN]
    	#lineL = [ch for ch in i]
    	             
    	for ii in u2: # get each char
    		list2.append(ii)
    	l2=len(list2)
    	if cc < 3:
    		for k in a[0]:
    		#for k in lineL:
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
  if debug2 == 1:
    print("\nCertainty: {}%\n".format(pm))



  match2=int(match2)


#  if debug == 1:
#    print(u_in)
  if req == 2:
    return(imList,2)
  else:
	  if pm >= 50:
	    return(best[1],1)
	  else:
	    return(best[1],1)

#############################






def main(u_in,req):
  global debug,debug2,debug3
  if debug == 1:
    print("\nSearching for: "+u_in)
  match=0
  match2=0
  match3=0
  li=[]
  
  u_in.lower()
  u_in = u_in.strip()
  
  if "?" in u_in: # Removes any (?)
    u_in = u_in.replace("?","")
  if "where " in u_in:
    u_in = u_in.replace("where","")
  if "show " in u_in:
    u_in = u_in.replace("show ","")
  
  if " are " in u_in:
    u_in = u_in.replace(" are","")
  if " the " in u_in:
    u_in = u_in.replace(" the","")
  if " is " in u_in:
    u_in = u_in.replace(" is","")
  if " did" in u_in:
    u_in = u_in.replace(" did","")
  if " I " in u_in:
    u_in = u_in.replace(" I","")
  if " it" in u_in:
    u_in = u_in.replace(" it","")
  if " to" in u_in:
    u_in = u_in.replace(" to","")
  if " be" in u_in:
    u_in = u_in.replace(" be","")
  if " put " in u_in:
    u_in = u_in.replace(" put","")
  if " can " in u_in:
    u_in = u_in.replace(" can","")
  if "find" in u_in:
    u_in = u_in.replace(" find","")
  if " an " in u_in:
    u_in = u_in.replace(" an","")
  if "-" in u_in: # Removes any (-)
    u_in = u_in.replace("-","")
  if "what " in u_in: # Removes any (what is)
    u_in = u_in.replace("what","")
  if " does " in u_in:
    u_in = u_in.replace(" does","")
  if "mean " in u_in or " mean" in u_in:
    u_in = u_in.replace("mean","")
    
  d = {}


  if req == 1:
    if "list" in u_in:
      retr,nrt = image(u_in,2)
      return(retr,nrt)
    else:
      r2,r3 = image(u_in,1)
      return(r2,r3)
  	


  elif req == 2:
    #image(u_in,2)
    f=open("items.txt","r")
    rfl=f.readlines()
    for i in rfl:
      i=i.lower()
      j=i.strip("\n")
      k=j.split(":")
      d[k[0]]=k[1]


  elif req == 3:
    f=open("terms.txt","r")
    rfl=f.readlines()
    for i in rfl:
      i=i.lower()
      j=i.strip("\n")
      k=j.split(":")
      d[k[0]]=k[1]

  if req != 1:
  	#return(["Sorry sir, you have not yet been granted access to this part of my code. I can only help you add to and retrieve images from your database","Sorry sir, you have not yet been granted access to this part of my code. I can only help you add to and retrieve images from your database"])


	  d = {}
	  pick = {}
	  match = 0
	  perc = 0
	  c = 0
	  cc = 0
	  cntr = 0
	  wordP = 0
	  word_guess = 0
	  cnt = 0
	  lst = []
	  got_one = 0
	  cnt2 = 0
	  total1 = 0
	  total2 = 0
	  pm = 0
		
	  userN = u_in
	  u_in = u_in.split()
	  
		
	  for i in u_in:
	      c += 1
		
	  l = (len(d))
		
	  for i in rfl:
	      i = i.lower()
		
	      j = i.strip("\n")
		
	      k = j.split(":")
		
	      d[k[0]] = k[1]
		
	  for i in rfl:
	      a = i.split(":")
	      a2 = a[0].split()
	      cc = len(a2)
		
	  cnt = 0
	  for i in rfl:
	      a = i.split(":")
	      a2 = a[0].split()
	      cc = len(a2)
	      cc2 = len(u_in)
	      for j in a2:
	          list1 = [ch for ch in j]
	          for k in u_in:
	              for x in list1:
	                  cnt += 1
	                  if x in k:
	                      cnt2 += 1
	              perc = int((cnt2 / cnt) * 100)
	              total1 += perc
	              lst.append(perc)
		
	      for j in u_in:
	          list1 = [ch for ch in j]
	          for k in a2:
	              for x in list1:
	                  cnt += 1
	                  if x in k:
	                      cnt2 += 1
	              perc = int((cnt2 / cnt) * 100)
	              total2 += perc
	              lst.append(perc)
	
	      #print(pick)
	
	      tt = int((total1+total2)/cc2)
	      #tt = int((total)/cc2)
	      if(cc == cc2):
	          tt = tt*2
	      else:
	          tt = tt/2
		
	      if (tt) > 50:
	          pick[a[0]] = (tt)
	      cnt2 = 0
	      cnt = 0
	      total1 = 0
	      total2 = 0
	  try:
	      best = max(list(zip(list(pick.values()),list(pick.keys()))))
	#      print()
	#      print('"{}" should be located at: {}'.format(best[1],d.get(best[1])))
	  except:
	      print('Sorry, nothing found...')
			
		
	  match2=int(match2)
		
		
		
	  if req == 3:
	    #print(u_in)
	#    if(pm >= 50):
	    return('Closest matching data: "{}"\n\n"{}": "{}"'.format(best[1],best[1],d.get(best[1])),1)
		
	#    else:
	#      return('No match found with certainy above 50%, But is this what you were looking for? "{}"\n\n"{}": "{}"'.format(best[1],best[1],d.get(best[1])),0)
		
		
		
	  elif req == 2:
	#    if pm >= 50:
	      return('"{}" should be located at: {}'.format(best[1],d.get(best[1])),1)
		
	#    else:
	#      return('No match found with certainy above 50%, But is this what you were looking for?\n\n"{}" should be located at: {}'.format(best[1],d.get(best[1])),0)
		
		
		
	  elif req == 1:
	    if debug == 1:
	#      print(u_in)
	#        if pm >= 50:
	      return(best[1],1)
	#    else:
	#      print("No match found with certainy above 50%, But is this what you were looking for?")
	#      return(best[1],0)
	
	
	
	
	#############################

if deb == 1:
	while(1):
		ui=str(input("> "))
		if(ui == 'q'):
		  sys.exit()
		else:
			#f2 = int()
			f = main(ui,1)
			print(f)
		
#else:
	#console.clear()
	#main(sys.argv[1])




