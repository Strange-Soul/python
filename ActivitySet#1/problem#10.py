# Dictionaries

"""
9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
"""        
"""filename=input("Enter the file name to open :")
fopen=open(filename)
dt=dict()
for line in fopen:
  print(line)"""
file_name=input("Enter the FileName to open:")
fhandle=open(file_name)
lst=list()
d=dict()
for line in fhandle:
  if line.startswith("From:"):
   continue
  if line.startswith("From"):
    spt=line.split()
    sp=spt[1]
    d[sp]=d.get(sp,0)+1
    #d[spt[1]]=d.get(spt[1],0)+1
print(sp,d[sp])
#print(spt[1],d[spt[1]])
   
"""file_name=input('Enter the file name to open:')
fhandle=open(file_name)
lst=list()
dt=dict()
for line in fhandle:
  if line.startswith("From:"):
   continue
  if line.startswith('From'):
   spt=line.split()
   lst.append(spt[1])
for key in lst:
  dt[key]=dt.get(key,0)+1
print(dt)
for key,value in dt.items():
 print(key,value)"""