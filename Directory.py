import subprocess

# call system process to create directory
def create(genDir):
	
    # open a file for errors
	errorLog = open ('error.txt', 'a')

	# makes a new directory in directory 'backups' and changes permission	
	try:
		subprocess.call(['mkdir', genDir])
		subprocess.call(['chmod', '755', genDir])
	except Exception as e:
		errorLog.write('%s\n' %e)
		errorLog.write('File exists.\n')
	

def remove(genDir):
    # open a file for errors
	errorLog = open ('error.txt', 'a')

	# makes a new directory in directory 'backups' and changes permission	
	try:
		subprocess.call(['rm','-r', genDir])
	except Exception as e:
		errorLog.write('%s\n' %e)
		errorLog.write('File exists.\n')
	


