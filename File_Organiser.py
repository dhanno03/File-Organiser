import os, glob, shutil

# TO-DO
# Make script work regardless of where it lives
# Add support for folders and subfolders. Currently only working for files

#Get path of directory needed to be organized
# '/*' added after the path to ensure glob gets
# every files and folder in the directory
path = str(os.getcwd())
print path
files = glob.glob(path + '/*')
print files

#File extensions related to specific function/folder
docs = ['txt', 'pdf', 'doc', 'docx', 'ppt', 'pptx', 'odt']
pics = ['jpeg', 'jpg', 'gif', 'png', 'svg', 'bat', 'bmp']
music = ['mp3', 'ogg', 'wav', 'wma']
code = ['py', 'h', 'cpp', 'cc', 'js', 'ts', 'html', 'css', 'scss', 'pyc', 'C']
misc = ['zip' , 'rar']
video = ['mp4', 'avi', 'flv', 'wmv', 'mov', 'webm', 'vob', 'mng','qt', 'mpg', 'mpeg', '3gp','mkv']

#Destination Directory for Specified File Types
# FORMAT : {{VAR_NAME_IN_CAPS}} = DESTINATION + '/{{directory_name}}'
DESTINATION = '/home/dhanno/trial'
DOCUMENTS = DESTINATION + '/Docs'
PICTURES = DESTINATION + '/Pics'
MUSIC = DESTINATION + '/Music'
CODE = DESTINATION + '/Code_Dump'
MISC = DESTINATION + '/Misc'
VIDEO = DESTINATION + '/Video'

for file in files:
	#We don't want the python file to be moved
	print file
	if file == (path + '/1.py'):
		print "FOUND"
		continue
	file_extension = file.split(".")[-1]
	if file_extension in docs:
		shutil.move(file, DOCUMENTS)
		continue
	if file_extension in pics:
		shutil.move(file, PICTURES)
		continue
	if file_extension in music:
		shutil.move(file, MUSIC)
		continue
	if file_extension in code:
		shutil.move(file, CODE)
		continue
	if file_extension in misc:
		shutil.move(file, MISC)
		continue
	if file_extension in video:
		shutil.move(file,VIDEO)
		continue
	print file_extension
