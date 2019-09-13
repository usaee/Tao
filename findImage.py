
import photos
import ui
import time

debug = 0

def getIM(name):
	v = ui.View(frame=(200, 200, 300, 450))
	f=open("imageList.txt","r")
	rfl=f.readlines()
	for i in rfl:
		j=i.strip("\n")
		j=j.split(":")
		if name in j[0]:
			try:
				j=j[1]
				im = photos.get_asset_with_local_id(j)
				
				img_view = ui.ImageView(frame=(2 + 1 * 25, 50, 250, 250), flex='wh')
				
				img_view.content_mode = ui.CONTENT_SCALE_ASPECT_FILL
				
				img_view.image = im.get_ui_image(size=(500, 500), crop=False)
				
				v.add_subview(img_view)
				v.present()
				#time.sleep(5)
				#v.remove_subview(img_view)
				break
			except:
				print("Sorry, i couldnt get that image")
				print(j)
				break
	else:
		print("Sorry, i couldnt get that image")
				
"""
if debug == 1:
	n=input("Name of image to search for: ")
	n=n.strip()
	getIM(n)
	
else:
	# Add code here:
	# Make this part get an image name from
	# a voice command.
	# Example: "Tao, show me an arduino"
	# Tao then passes in the word "arduino"
	# to the function getIM(name)
	
	pass
"""
