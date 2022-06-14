# Dictionaries

"""
9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
"""        
'''file_name="dataset/mbox-short.txt"
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
#print(spt[1],d[spt[1]])'''

email_s=dict()
file='dataset/mbox-short.txt'
file_open=open(file)
for line in file_open:
  if line.startswith('From '):
    line=line.rstrip().split()
    email=line[1]
    email_s[email]=email_s.get(email,0)+1
print(email,email_s[email])