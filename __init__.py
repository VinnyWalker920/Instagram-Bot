import os
import time
import random
from os import listdir
from os.path import isfile, join
from random import randint
from InstagramAPI import InstagramAPI


#Long list of hashtags, could put it in a txt file
Tags = "\n-\n-\n-\n-\n-\n-\n-\n-\n-\n-\n#animals #nature #animal #pets #love #wildlife #cute #pet #photography #cats #dogs #dog #instagram #cat #naturephotography #photooftheday #of #dogsofinstagram #instagood #love #catsofinstagram #animallovers #art #petstagram #petsofinstagram #wildlifephotography #puppy #happy #cuteanimals #bhfyp"

CaptionFile = 'Captions.txt'
caption_list = []
# open output file for reading
with open(CaptionFile, 'r') as filehandle:
    for line in filehandle:
        # remove linebreak which is the last character of the string
        currentLine = line[:-1]
        # add item to the list
        caption_list.append(currentLine)


#Credentials and PhotoPath
PhotoPath = "/Users/OneDrive/Content"  # Change Directory to Folder with Pics that you want to upload
IGUSER = "cutestcuddles_"  # Change to your Instagram USERNAME
PASSWD = "*****"  # Change to your Instagram Password

#first time it initiates
os.chdir(PhotoPath)
ListFiles = sorted([f for f in listdir(PhotoPath) if isfile(join(PhotoPath, f))])
print(ListFiles)
print("Total Photo in this folder:" + str(len(ListFiles)))

#Start Login and Uploading Photo
igapi = InstagramAPI(IGUSER, PASSWD)
igapi.login()  # login

def Create_Post():

	os.chdir(PhotoPath)
	ListFiles = sorted([f for f in listdir(PhotoPath) if isfile(join(PhotoPath, f))])
	print(ListFiles)
	print("Total Photo in this folder:" + str(len(ListFiles)))

	for i, _ in enumerate(ListFiles):		
		print("Debug:Upload")
		IGCaption = random.choice(caption_list)
		photo = ListFiles[i]
		print("Progress :" + str([i + 1]) + " of " + str(len(ListFiles)))
		print("Now Uploading this photo to instagram: " + photo)
		igapi.uploadPhoto(photo, caption="Follow @cutestcuddles_ //" +IGCaption + Tags, upload_id=None)
		os.remove(photo)
	    #sleep for random between 60 - 120s
		n = randint(900,1200)
		print("Sleep upload for seconds: " + str(n))
		time.sleep(n)
		Scan()

#Scans for images in folder
def Scan():
	x = True
	while x is True:
		ListFiles = sorted([f for f in listdir(PhotoPath) if isfile(join(PhotoPath, f))])
		if len(ListFiles) > 0:
			print("Debug:Call Func")
			Create_Post()
			x =False


Scan()
