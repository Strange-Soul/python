# Dictionaries

"""
9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
"""        
filename = "dataset/mbox-short.txt"
fhand=open(filename)
lst=list()
sec=dict()

for line in fhand:
  if line.startswith('From:'):
    continue
  if line.startswith('From') :
    words=line.split()
    words=words[1]
    sec[words]=sec.get(words,0)+1
print(words,sec[words])
"""for line in fhand:
  if line.startswith("From:") or not line.startswith('From'):
    continue
    word=line.split
    lst.append(word[1])
print(lst)
for word in lst:
  sec[word]=word.get(word,0)+1

bigcount=None
bigword=None
for k,v in sec.items():
  if bigcount is None or v>bigcount:
    bigcount=v
    bigword=w
print(bigword,bigcount)"""
  
  


   

  
    