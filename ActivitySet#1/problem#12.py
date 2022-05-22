# Regular Expressions
# https://www.py4e.com/lessons/regex
import re
filename=input("Enter the file name: ")
fopen=open(filename)
for line in fopen:
  line=line.rstrip()
  if re.search('^F..m',line):
  
   print(line)