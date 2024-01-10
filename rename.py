import os
import re

folders = ["music", "sfx", "vocals"]
allFiles = []

def iterateFiles(folder):
  files = os.listdir(folder)

  for file in files:
    if not "." in file:
      iterateFiles("%s/%s" % (folder, file))

    else:
      allFiles.append("%s/%s" % (folder, file))

for folder in folders:
  iterateFiles(folder)

for originalFile in allFiles:
  newFile = re.sub("\[[^\]]+\] ", "", originalFile)
  newFile = re.sub(" ", "-", newFile)
  newFile = re.sub("-{3,}", "-", newFile)
  newFile = re.sub(",", "", newFile)
  newFile = re.sub("\(|\)", "", newFile)

  newFile = newFile.lower()

  # print(originalFile)
  # print(newFile)

  if ".mp3" in originalFile or ".asd" in originalFile:
    os.remove(originalFile)
  else:
    os.rename(originalFile, newFile)
