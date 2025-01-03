import re
import readFileFromSystem 

fileInfo = readFileFromSystem.openAndReadFile('text_file.txt')

def findNumbers(fileInfo):
  return re.findall(r'\d+', fileInfo)

print(findNumbers(fileInfo))
