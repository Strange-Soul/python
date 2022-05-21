# Tuples
"""
Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
"""
filename = "dataset/mbox-short.txt"
lst=list()
d=dict()
if len(filename) < 1:
    filename = "mbox-short.txt"
handle = open(filename)
for line in handle:
    if line.startswith("From:"):
         continue
    if line.startswith("From"):
         l=line.split()
         t=l[5]
         
         ft=t.split(":")
         lst.append(ft[0])
         lst.sort() 
"""for c in lst:
    d[c]=d.get(c,0)+1
    print(c,d[c])"""
         
for k in lst:
    if k not in d:
      d[k]=1
    else:
        d[k]+=1
print(d)