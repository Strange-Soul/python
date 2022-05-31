# Regular Expressions
#https://www.py4e.com/lessons/regex

import re
sum=0
file_name=input("Enter the filename:")
file_open=open(file_name,"r")
for line in file_open:
  line =line.rstrip()
  #find_num=re.findall("[0-9]+",line)
  find_num=re.findall('\d+',line)
  for num in find_num:
    y=float(num)
    sum=sum+y
print(sum)