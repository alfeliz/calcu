#! /usr/bin/python
# python 2.7
# Calcu.py - Checks the contents of the '04-Calculations' folder and present them nicely.

import os


calcufolder = '/home/gonzalo/Documents/04-Calculations' #Real value

folderlist = os.walk(calcufolder)
#os.walk returns an structure with the files, directories and fles inside the directories of a given path,
#   ordered as triplets, with the order used later.



htmlfile = open('/home/gonzalo/Documents/04-Calculations/read-me.html','w') #Real value


for dirpath,dirnames,filenames in folderlist:
	dirnames.sort() #This command sort the directory structure by alphabetical order.
	for files in filenames: #This is the structure of an iterator on the objects of filenames, that I name files
		if "readme" in files:
			htmlfile.write("<h1>" + '<a href = "' + dirpath + '/' + '">' +  dirpath.strip('./')+ '/' +files + "</a>" + "</h1>\n")
			for lines in open(os.path.join(dirpath,files)).readlines():
				htmlfile.write( lines + "<br>\n" )

htmlfile.close()
			
#print('Job finished. HTML file with 04-Calculations contains made.')


#And that.. that... that's all folks!
