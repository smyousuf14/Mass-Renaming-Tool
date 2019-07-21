#python 3 code to rename files on mass

#imports
import os

#A function that renames all files in a specified folder
def renameFiles(currentDirectoryName, newDirectory, newFileConstant, startingIncrement, fileExtension):
	
	# Now rename each file in the current directory in the following manner
	# newFileConstant-increment
	for fileName in os.listdir(currentDirectoryName):
		
		newDirectory = newDirectory + "/" + newFileConstant + "-" + str(startingIncrement) + fileExtension
		
		#rename the new directory.
		os.rename(currentDirectoryName, newDirectory)
		
		#increment
		startingIncrement += 1



#Driver code
if __name__ == '__main__':
	
	currentDir = input("Enter current directory: ")
	newDir = input("Enter new directory: ")
	fileConstant = input("Enter the file constant: " )
	startingIncrement = input("Enter the starting increment number: ")
	fileExtension = input("Enter the extension type: ")
	
	#Processing
	print("Processing .... ")
	renameFiles(currentDir, newDir, fileConstant, startingIncrement, fileExtension)
	
	#Done
	print("Done...")