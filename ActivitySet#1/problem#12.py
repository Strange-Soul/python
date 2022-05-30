# Regular Expressions
#https://www.py4e.com/lessons/regex

import re
file_name=input("Enter the filename:")
file_open=open(file_name,"r+")
for line in file_open:
  line =line.rstrip()
  if re.search("",line):
    print(line)
  