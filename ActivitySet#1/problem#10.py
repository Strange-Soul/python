# Dictionaries

"""
9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
"""        
file_name="dataset/mbox-short.txt"
fhandle=open(file_name)
d=dict()
for line in fhandle:
  if line.startswith("From:"):
   continue
  if line.startswith("From"):
    spt=line.split()
    email=spt[1]
    d[email]=d.get(email,0)+1
print(email,d[email])
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