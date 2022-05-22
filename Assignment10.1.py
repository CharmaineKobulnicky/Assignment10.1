import os #import the OS library
filePath = 'C:/Users/marie/AppData/Local/Programs/Python/Python310/python.exe'
fileName = 'testFile.txt'
completePath = filePath+fileName
if os.path.isfile(fileName) : #check if file exists
    print('File Exists')
if os.path.isdir(filePath) : #check if file path exists
    print('Directory Exists')
if os.path.exists(completePath) : #check if complete path exists
    print('Complete path exists')
print('Complete Path',completePath)
with open(completePath, 'w') as fileHandle: #open file for writing
    fileHandle.write("I love programming and Python.") #write data to file
with open(completePath, 'r') as fileHandle: #open same file for reading
    data = fileHandle.read() #read data from the file
    print(data)

