
import photos
import sys

debug = 0

def add():
	f=open("imageList.txt","a")
	
	fail = 0
	
	id = photos.pick_asset(title='Pick some assets', multi=False)

	try:
		if id == None:
			fail = 1
	except:
		pass
		
	if fail == 0:
		if debug == 1:
			print(id)
			
		g=str(id)
		g=g.strip()
		g=g.strip("<Asset")
		g=g.split("image")
		g2=g[0]
		g2=g2.strip(" - ")
		
		if debug == 1:
			print("\n")
			
		if debug == 1:
			print(g2)
			
		d=input("Name of this image: ")
		d=d.strip()
		d=d.lower()
		name=d+":"+g2
		name+="\n"
		f.write(name)
	
		
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
