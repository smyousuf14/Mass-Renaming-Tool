#python 3 code to rename files on mass

#imports
import os

#A function that renames all files in a specified folder
def renameFiles(currentDirectoryName, newFileConstant, startingIncrement, fileExtension):
	
	# Now rename each file in the current directory in the following manner
	# newFileConstant-increment
	for fileName in os.listdir(currentDirectoryName):
		
		dst = newFileConstant + "-" + str(startingIncrement) + fileExtension
		src = currentDirectoryName + "/" + fileName
		dst = currentDirectoryName + "/" + dst
		
		#rename the new file.
		os.rename(src, dst)
		
		#increment
		startingIncrement += 1



#Driver code
if __name__ == '__main__':
	
	currentDir = input("Enter current directory: ")
	fileConstant = input("Enter the file constant: " )
	startingIncrement = input("Enter the starting increment number: ")
	fileExtension = input("Enter the extension type: ")
	
	#Processing
	print("Processing .... ")
	renameFiles(currentDir, fileConstant, startingIncrement, fileExtension)
	
	#Done
	print("Done...")