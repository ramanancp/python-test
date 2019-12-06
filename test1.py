#!/usr/bin/python

import sys

try:
   file = open(file_name,'w')
except IOError:
   print ("There was an error writing to file", file_name)
   sys.exit()

print ("Enter file_finish when finished..")

while file_text != file_finish:
   file_text = raw_input("Enter text: ")
   if file_text == file_finish:
      #close the file
      file.close()
      break
   file.write(file_text)
   file.write("\n")
file.close()
file_name = raw_input("Enter file name: ")
if len(file_name) == 0:
   print ("Next time enter something:")
   sys.exit()
try:
   file = open(file_name,"r")
except IOError:
   print ("There was an error reading the file")
   sys.exit()
file_text = file.read()
file.close()
print file_text

   

   
   