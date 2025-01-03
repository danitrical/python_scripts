def openAndReadFile(fileName):
  file = open(fileName,'r')
  content = file.read()
  file.close()
  return content

fileInfo = openAndReadFile('text_file.txt')

print(fileInfo)